from flask import Flask,send_from_directory

import os

# from sqlalchemy import create_engine
# from flask import render_template

# import Blueprint in a folder
# from app_home.route import app_home
# from app_prototype.route import app_prototype
# from myapp import config --> config.DATABASE_URI
# from myapp.views import frontend

# App name 
app = Flask(__name__,static_url_path='/static')
# app.register_blueprint(app_home,url_prefix='/home')
# app.register_blueprint(app_prototype,url_prefix='/prototype')

# set up your database
# app.engine = create_engine(database_uri)

# add your modules
# app.register_module(frontend)

@app.route('/')
def hello_world():
  return 'Hello World: Flask is fun!'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')  

if __name__ == "__main__":
  app.run(debug=True)

     