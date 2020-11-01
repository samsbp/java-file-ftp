import os
import sys
from hashlib import md5

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed


class DummyMD5Authorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        print("="*50)
        print("Sniffed java version :: "+password)
        print("="*50)

def main():
    # get a hash digest from a clear-text password
    authorizer = DummyMD5Authorizer()
    authorizer.add_user('user', '12345', os.getcwd(), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('', 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
