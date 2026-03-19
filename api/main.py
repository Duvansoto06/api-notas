from fastapi import FastAPI
from pydantic import BaseModel

from src.models.predict_model import predict

app = FastAPI(
    title="Notas predicción API",
    description ="API para predecir Notas según horas de estudio",
    version ="1.0"
)

class CalificacionInput(BaseModel): #Definición de clase con los atributos
    calificacion: float

@app.get("/")
def root():
    return {'message':'Api de predicción activa'}

@app.post("/predict")
def predict_sales(data: CalificacionInput):

    result = predict(data.calificacion)
    return {
        "Calificacion": data.calificacion,
        "Horas Estudiadas": result
    }
