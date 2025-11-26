# User Validator - Authentication Service
import re
from typing import Optional

class UserValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        # ISSUE: Incomplete regex pattern
        pattern = r'^[a-zA-Z0-9]+@'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Validate password strength"""
        # ISSUE: No minimum length check
        if len(password) < 6:
            return False
        return True
    
    @staticmethod
    def sanitize_username(username: str) -> str:
        """Sanitize username - ISSUE: Incomplete sanitization"""
        # ISSUE: Missing validation
        return username.strip()
