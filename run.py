from market import app
from livereload import Server

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0')
