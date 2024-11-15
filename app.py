# app.py

from flask import Flask  # type: ignore
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'The CI-CD pipeline been developed now yippeeee wowww mindblowing......Horrayy'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
