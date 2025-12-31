from fastapi import APIRouter, Request
from app.schemas.claim import ClaimRequest

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Insurance Claim Prediction API"}

@router.post("/predict")
def predict_claim(request: ClaimRequest, req: Request):
    predictor = req.app.state.predictor
    amount = predictor.predict(request.dict())
    return {"estimated_claim_amount": amount}


@router.get("/health")
def health():
    return {"status": "ok"}
