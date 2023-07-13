from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    urus = 'urus'
    huracan = 'huracan'
    revuelto = 'revuelto'


app = FastAPI()


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.urus:
        return {"model_name": model_name, "HorsePower": 657}
    if model_name == 'revuelto':
        return {"model_name": model_name, "HorsePower": '1000 ice+ee'}
    if model_name == ModelName.huracan.value:
        return {'model_name': model_name, "HorsePower": 630}
