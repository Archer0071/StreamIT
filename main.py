from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount('/',StaticFiles(directory='ui',html=True),name='ui')
@app.get("/")
async def root():
    return {"message":"WelCome to fastApi"}

if __name__ == '__main__':
    uvicorn.run(app)