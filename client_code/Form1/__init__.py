from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print('Hi')
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    a = anvil.server.call('get_headers_from_pandas')
    print(a)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    
   

  
    

  
