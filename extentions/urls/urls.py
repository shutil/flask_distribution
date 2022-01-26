from extentions.server import app
from blueprints.index.views import index_blp 

def urls_path():
    return[
        app.register_blueprint(index_blp,path='/')
    ]

url = urls_path()