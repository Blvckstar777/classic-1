import anvil.server
#import pandas as pd
#url1 = "https://github.com/Blvckstar777/classic-1/blob/master/AppleStore.csv"
#url1 = "https://www.kaggle.com/datasets/ysf12ff/app-store-dataset/data"
#appstore_df = pd.read_html(url1)
#appstore_df = {'url':url1,
#              'name': 'appstore_data',
#              'load_func': lambda URL: pd.read_html(URL)[0]}
#
#df1 = appstore_df['load_func'](appstore_df['url'])
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
@anvil.server.callable
def say_hello(name):
   print("Hello, " + name + "!")
   return 42
#@anvil.server.callable
#def explore():
#  print(appstore_df.header())
  #type(df1)
   

