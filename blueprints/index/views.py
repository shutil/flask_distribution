from flask import Blueprint, jsonify

index_blp = Blueprint('index',__name__)

@index_blp.route('/')
def index_blp_index():
    return jsonify({'api':'index page api'})