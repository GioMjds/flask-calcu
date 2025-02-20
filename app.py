from flask import Flask, Blueprint
from calculator.__init__ import create_app

app = Flask(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)