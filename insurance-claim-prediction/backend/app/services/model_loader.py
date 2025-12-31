import json
import joblib
from app.core.config import METADATA_FILE, ARTIFACTS_DIR

class ModelLoader:
    @staticmethod
    def load():
        with open(METADATA_FILE) as f:
            metadata = json.load(f)

        version = metadata["active_version"]
        model = joblib.load(ARTIFACTS_DIR / version / "model.pkl")
        scaler = joblib.load(ARTIFACTS_DIR / version / "scaler.pkl")

        return model, scaler
