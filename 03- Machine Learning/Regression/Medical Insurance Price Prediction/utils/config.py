from dotenv import load_dotenv
import os
import joblib

load_dotenv(override=True)


APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv("VERSION")
SECRET_KEY_TOKEN =os.getenv('SECRET_KEY_TOKEN')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_PATH = os.path.join(BASE_DIR, "models")

model_path = os.path.join(MODELS_PATH, "model_best_forest.pkl")

forest_model = joblib.load(model_path)
