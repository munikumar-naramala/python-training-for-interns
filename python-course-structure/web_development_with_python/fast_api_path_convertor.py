from fastapi import FastAPI

app = FastAPI()

Cars = {
    'Porsche': "911 Carreras",
    'Pagani': 'Zonda',
    'Ferrari': 'f40',
    'BMW': 'M5 competition',
    'Aston Martin': 'Ventura',
    'Lamborghini': 'Urus'
}


@app.get("/cars/{car_name}")
async def read_file(car_name: str):
    try:
        return {"file_path": car_name}
    except BaseException as error:
        print('there is an exception: {}'.format(error))
