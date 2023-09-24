from fastapi import FastAPI

from routes import auth, disease, herb

app = FastAPI()

app.include_router(auth.router)
app.include_router(herb.router)
app.include_router(disease.router)
