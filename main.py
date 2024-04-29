
import pickle
from fastapi import FastAPI,HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class SensorData(BaseModel):
    temperature: float
    humidity: float
    lpg: float


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/check")
def make_api_call(sensor_data: SensorData):

    url = "http://3.6.36.123:8000/test"
    try:
        response = requests.post(url, json=sensor_data.dict())
        response.raise_for_status()  # Raises HTTPError for bad requests (4XX or 5XX)
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
