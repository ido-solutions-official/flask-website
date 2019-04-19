class Development(object):
  """
  config for development process
  """

  ENV = 'development';
  DEBUG = True;
  TESTING=True; 
  static_url_path='/static';
  template_folder='templates'

  def __init__(self):
    pass;

  
       