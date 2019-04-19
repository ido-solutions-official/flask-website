from flask import Flask,send_from_directory,render_template,url_for,Blueprint

import os

# import config
import config.dev
import config.production

# import blue print
from app_home.route import app_home

def create_app(config='dev'):
    # create and configure the app
    app = Flask(__name__)
    app.register_blueprint(app_home,url_prefix='/home')


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
    def render_0_index():
      return render_template('index.html')      

    @app.errorhandler(404)
    def page_not_found(e):
    # note that we set the 404 status explicitly
      return render_template('404.html'), 404    

    return app

if __name__ == "__main__":
  app = create_app(config='dev')
  app.run()

     