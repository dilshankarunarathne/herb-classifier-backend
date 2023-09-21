from fastapi import FastAPI

from routes import auth, disease

app = FastAPI()

app.add_route(auth)
app.add_route(disease)

