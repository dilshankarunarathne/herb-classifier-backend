from fastapi import FastAPI

from routes import auth, disease

app = FastAPI()

app.include_router(auth)
app.add_route(disease)

