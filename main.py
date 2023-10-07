from fastapi import FastAPI

from routes import auth, disease, herb, location



app = FastAPI()

app.include_router(auth.router)
app.include_router(herb.router)
app.include_router(disease.router)
app.include_router(location.router)
