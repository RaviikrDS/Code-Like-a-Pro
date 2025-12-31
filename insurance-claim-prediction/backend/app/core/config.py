from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = BASE_DIR / "artifacts"
METADATA_FILE = ARTIFACTS_DIR / "metadata.json"
