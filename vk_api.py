from urllib.request import urlopen
from urllib.parse import urlencode
from os import remove, path
from api_errors import *
import subprocess
import time
import json
import sys


API_URL = 'https://api.vk.com/method/%s?%s'

TOKEN_FILENAME = 'token.json'
TOKEN_DIR = path.dirname(__file__)
TOKEN_PATH = path.join(TOKEN_DIR, TOKEN_FILENAME)



class Api:
    def __init__(self):
        self.token_info = self.get_token()
        if self.token_info is None or not self.check_correctness():
            self.upd_token_file()

    def get_token(self):
        if not path.exists(TOKEN_PATH):
            return None

        try:
            with open(TOKEN_PATH) as f:
                token_info = json.load(f)
        except OSError:
            return None
        except ValueError:
            return None

        if 'access_token' not in token_info:
            return None

        if 'user_id' not in token_info:
            return None

        if 'expires_in' not in token_info:
            return None

        return token_info

    def check_correctness(self):
        try:
            res = self.method('account.getInfo')
        except AuthFailedError:
            return False
        return True

    def check_expiration(self):
        if time.time() >= self.token_info['expires_in']:
            self.upd_token_file()

    def upd_token_file(self):
        if path.exists(TOKEN_PATH):
            remove(TOKEN_PATH)

        cmd = sys.executable, 'token_getter', TOKEN_PATH
        subprocess.call(cmd)

        self.token_info = self.get_token()
        if self.token_info is None:
            print('Cannot get token')
            print('You can make %s file manualy' % TOKEN_FILENAME)
            sys.exit()

    def check_error(self, res):
        if res.get('error') is None:
            return

        raise ERR_CODES.get(res['error']['error_code'], 1)(res)

    def method(self, method, **kwargs):
        self.check_expiration()

        kwargs.setdefault('access_token', self.token_info['access_token'])
        kwargs.setdefault('user_id', self.token_info['user_id'])
        params = urlencode(kwargs)

        url = API_URL % (method, params)
        with urlopen(url) as p:
            res = json.loads(p.readall().decode())
        
        self.check_error(res)
        return res['response']
