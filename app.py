from flask import Flask,send_from_directory

import os

import config.dev
import config.production

def create_app(config='dev'):
    # create and configure the app
    app = Flask(__name__)

    if config is 'dev':
        # load development config -- by default
        app.config.from_object('config.dev.Development')
    else:
        # load production config
        app.config.from_object('config.production.Production')

    @app.route('/favicon.ico')
    def favicon():
      return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon') 
      
    @app.route('/')
    def index_render():
      return 'Hello World: Flask is fun!'       

    return app

if __name__ == "__main__":
  app = create_app(config='dev')
  app.run()

     