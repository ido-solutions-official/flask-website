from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

app_home = Blueprint('app_home', __name__,template_folder='templates')

@app_home.route('/')
def render():
  try:
      return render_template('home_index.html') 
  except TemplateNotFound:
      abort(404) 


   

    