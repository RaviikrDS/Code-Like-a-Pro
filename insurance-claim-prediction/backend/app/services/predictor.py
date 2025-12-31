import pandas as pd
from app.services.model_loader import ModelLoader
from app.core.logging import logger

class ClaimPredictor:
    def __init__(self):
        self.model = None
        self.scaler = None

    def load(self):
        self.model, self.scaler = ModelLoader.load()
        logger.info("Model loaded successfully")

    def predict(self, data: dict) -> float:
        df = pd.DataFrame([data])
        scaled = self.scaler.transform(df)
        prediction = self.model.predict(scaled)[0]
        return float(prediction)
