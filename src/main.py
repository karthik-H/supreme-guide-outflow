import time
import logging
from src.controller.user_controller import UserController
from src.config.config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def main():
    logging.info("Starting periodic user data retrieval...")
    try:
        while True:
            UserController.save_users_to_csv()
            time.sleep(Config.INTERVAL_SECONDS)
    except KeyboardInterrupt:
        logging.info("Process terminated by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
