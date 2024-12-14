import anvil.server
import pandas as pd
#url1 = "https://github.com/BlueSpirit48/Project-TK/blob/main/AppleStore.csv"
#url1 = "https://www.kaggle.com/datasets/ysf12ff/app-store-dataset/data"
#appstore_df = pd.read(url1)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
appstore_df = pd.DataFrame(data)

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
#def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
def explore():
  print("Hello")
  print(appstore_df.head())


class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    anvil.server.call('explore')

