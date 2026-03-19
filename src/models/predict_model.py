import joblib 
import numpy as np 
 
model = joblib.load("models/modelo_regresion.pkl") 
 
def predict(calificacion): 
 
   data = np.array([[calificacion]]) 
 
   pred = model.predict(data) 
 
   return float(pred[0])