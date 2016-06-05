from PyQt4.QtCore import QUrl, QObject, SIGNAL
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView
import time


class TokenGetter:
    def __init__(self):
        self.app = QApplication([])
        self.data = None
        self.success = False

    def open_browser(self, url):
        self.webview = QWebView()
        QObject.connect(self.webview,
                        SIGNAL('urlChanged (const QUrl&)'),
                        self.on_redirect)
        self.webview.load(QUrl(url))
        self.webview.show()
        self.app.exec_()

    def data_from_fragment(self, fragment):
        params = dict(i.split('=') for i in fragment.split('&'))

        if 'access_token' not in params:
            return None

        params['expires_in'] = time.time() + int(params['expires_in'])
        params['user_id'] = int(params['user_id'])
        return params

    def on_redirect(self, url):
        if not url.hasFragment():
            return

        data = self.data_from_fragment(url.fragment())
        if data is None:
            return

        self.data = data
        self.success = True
        self.app.exit()
