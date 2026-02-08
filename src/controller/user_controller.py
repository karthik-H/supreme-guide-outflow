import os
import csv
import logging
from datetime import datetime
from src.config.config import Config
from src.service.user_service import UserService

class UserController:
    @staticmethod
    def save_users_to_csv():
        users = UserService.get_all_users_flat()
        if not users:
            logging.warning("No user data to write.")
            return
        os.makedirs(Config.CSV_OUTPUT_DIR, exist_ok=True)
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        filename = f"user_data_{timestamp}.csv"
        filepath = os.path.join(Config.CSV_OUTPUT_DIR, filename)
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=users[0].keys())
                writer.writeheader()
                writer.writerows(users)
            logging.info(f"Saved {len(users)} users to {filepath}")
        except Exception as e:
            logging.error(f"Error writing CSV file: {e}")
