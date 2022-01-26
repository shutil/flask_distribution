from flask import Flask

def create_server():
    return Flask(__name__)


app = Flask(__name__)