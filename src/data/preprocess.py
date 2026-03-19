def prepare_data(df): 
   X = df[['Horas_Estudio']]  
   y = df['Calificacion'] 
 
   return X, y