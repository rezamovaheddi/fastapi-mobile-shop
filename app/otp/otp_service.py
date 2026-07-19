import random
from datetime import datetime, timedelta


class OTPService:
    @staticmethod
    def generate_code() -> str:
        return str(random(random.randint(100000, 999999)))

    @staticmethod
    def expire_code(min: int = 5):
        return datetime.utcnow() + timedelta(minutes=min)

    @staticmethod
    def is_expired(expire_time: datetime) -> bool:
        return datetime.utcnow() > expire_time
