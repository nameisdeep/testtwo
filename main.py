from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello,World deep gohil"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)