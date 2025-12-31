from fastapi import FastAPI
from app.api.routes import router
from app.services.predictor import ClaimPredictor

app = FastAPI(title="Insurance Claim Prediction API")


@app.on_event("startup")
def startup_event():
    predictor = ClaimPredictor()
    predictor.load()
    app.state.predictor = predictor


app.include_router(router)
