import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import auth, disease, herb, location, esystem

app = FastAPI()

origins = ['http://localhost:3000', 'http://192.168.178.23:3000']  # add your front-end ip:port here

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(herb.router)
app.include_router(disease.router)
app.include_router(location.router)
app.include_router(esystem.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
