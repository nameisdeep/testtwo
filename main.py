import pickle
from fastapi import FastAPI

app = FastAPI()

with open('gasleakage.pkl', 'rb') as f:
    model = pickle.load(f)


@app.get("/")
async def read_root():
    return JSONResponse(content={"Hello": "World"})





if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)