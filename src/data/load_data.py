import pandas as pd 
 
def load_data(path):
   df = pd.read_csv('horas_estudio.csv')
   return df