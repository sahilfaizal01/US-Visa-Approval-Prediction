import os
from datetime import date 
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = os.getenv("MONGODB_URL")

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"
