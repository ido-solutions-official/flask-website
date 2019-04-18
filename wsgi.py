# EX location of app.py ==> contain app = Flask(__name__)
# /home/yourusername/mysite/flask_app.py

import sys
path = ''
if path not in sys.path:
   sys.path.insert(0, path)

from app import app as application