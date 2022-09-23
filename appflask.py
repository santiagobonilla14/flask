from flask import Flask

server =Flask(__name__)

@server.route('/')
def hola():
    return 'pude instalar una app en la web'

if __name__ =='__main__':
    server.run()
