import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    
    PARABANK_API_BASE_URL = os.getenv("PARABANK_API_BASE_URL")
    
    PARABANK_USERNAME = os.getenv("PARABANK_USERNAME")
    
    PARABANK_PASSWORD = os.getenv("PARABANK_PASSWORD")
    
    