from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


IP = "127.0.0.1"
PORT = 21

authorizer = DummyAuthorizer()

# full permissions for user=user and password=12345
authorizer.add_user("user", "12345", ".", perm="elradfmw")  

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((IP, PORT), handler)
server.serve_forever()