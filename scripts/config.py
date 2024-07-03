from pathlib import Path

class Config:
  RANDOM_SEED = 90
  ASSETS_PATH = Path("../")
  REPO = "~/Documents/10 academy/Week 10/Brent-oil-prices-data-analysis"
  DATASET_FILE_PATH = "data/BrentOilHistoricalData.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "models"