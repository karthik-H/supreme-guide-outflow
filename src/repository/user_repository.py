import requests
from src.config.config import Config
from typing import List, Dict, Any
import logging

class UserRepository:
    @staticmethod
    def fetch_all_users() -> List[Dict[str, Any]]:
        try:
            response = requests.get(Config.API_URL, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Error fetching users: {e}")
            return []
