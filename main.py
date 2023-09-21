from fastapi import FastAPI

from routes import auth

app = FastAPI()

app.add_route(auth)

