import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_URL = os.getenv('API_URL')
    CSV_OUTPUT_DIR = os.getenv('CSV_OUTPUT_DIR', 'csv_snapshots')
    INTERVAL_SECONDS = int(os.getenv('INTERVAL_SECONDS', '10'))
