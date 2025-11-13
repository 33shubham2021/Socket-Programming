from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#"C:\Users\33shu\Documents\Coding\FTP-Practice_Directory\user1"

COMPANY_PATH = "./FTP-Practice_Directory/user1"
BANK_PATH = "./FTP-Practice_Directory/user2"

IP = "127.0.0.1"
PORT = 21

authorizer = DummyAuthorizer()

# full permissions for user=user and password=12345
authorizer.add_user("company", "12345", COMPANY_PATH, perm="elradfmw")
authorizer.add_user("bank", "123456", BANK_PATH, perm="elradfmw")


handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((IP, PORT), handler)
server.serve_forever()