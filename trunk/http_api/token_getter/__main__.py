import sys
import json
import argparse
from os import path
from urllib.parse import urlencode
from token_getter import TokenGetter


parser = argparse.ArgumentParser()
parser.add_argument('tpath', help='Token file path')
args = parser.parse_args()


CUR_DIR = path.dirname(__file__)


# Auth params getter
#
AUTHPARAMS_FILENAME = 'params.json'
AUTHPARAMS_DIR = CUR_DIR
AUTHPARAMS_PATH = path.join(AUTHPARAMS_DIR, AUTHPARAMS_FILENAME)

try:
    with open(AUTHPARAMS_PATH) as f:
        authparams = json.load(f)
except OSError:
    print('Cannot find %s' % AUTHPARAMS_FILENAME)
    sys.exit()
except json.JSONDecodeError:
    print('%s is not valid' % AUTHPARAMS_FILENAME)
    sys.exit()


# VK token getter
#
AUTH_URL = 'https://oauth.vk.com/authorize?%s'
params = urlencode(authparams)
url = AUTH_URL % params

tg = TokenGetter()
tg.open_browser(url)

if not tg.success:
    print('Login to vk please')
    sys.exit()


# Token file writer
#
TOKEN_PATH = args.tpath

try:
    with open(TOKEN_PATH, 'w') as f:
        json.dump(tg.data, f)
except OSError:
    print('Cannot write data to file')
    print('Please make it manualy')
    print('Data:')
    print(json.dumps(tg.data))
except TypeError:
    print('Some problem with serialization')
    print('Here is your data:')
    print('{'
          '"access_token": %(access_token)s,'
          '"expires_in": %(expires_in)s,'
          '"user_id": %(user_id)s'
          '}', tg.data)
