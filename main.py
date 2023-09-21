from fastapi import FastAPI

from routes import auth, disease

app = FastAPI()

app.include_router(auth.router)
app.add_route(disease)

