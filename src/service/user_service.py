from src.repository.user_repository import UserRepository
from src.domain.user import User
from typing import List, Dict, Any
import logging

class UserService:
    @staticmethod
    def get_all_users_flat() -> List[Dict[str, Any]]:
        raw_users = UserRepository.fetch_all_users()
        users = [User(data) for data in raw_users]
        flat_users = [user.to_flat_dict() for user in users]
        logging.info(f"Fetched and flattened {len(flat_users)} users.")
        return flat_users
