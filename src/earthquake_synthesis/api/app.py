from fastapi import FastAPI
from pathlib import Path
import pandas as pd

app = FastAPI(title="Earthquake Synthesis API", version="0.1.0")

@app.get("/v1/manifest")
def get_manifest():
    manifest = Path(__file__).resolve().parents[3] / "data" / "manifest.csv"
    return {"manifest": manifest.read_text().splitlines()[:20]}

@app.get("/v1/sample/{filename}")
def get_sample(filename: str, limit: int = 5):
    data_path = Path(__file__).resolve().parents[3] / "data" / "raw" / filename
    if not data_path.exists():
        return {"error": f"{filename} not found"}
    if data_path.suffix == ".csv":
        df = pd.read_csv(data_path)
        return df.head(limit).to_dict(orient="records")
    return {"error": "only CSV preview supported"}
