# JWT Token Handler - Authentication Service
import jwt
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class JWTHandler:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
    
    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Decode JWT token - VULNERABLE: No format validation"""
        try:
            # ISSUE: Missing token format validation
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except:  # ISSUE: Bare except clause
            return None
    
    def verify_user_token(self, token: str, expected_user_id: Any) -> bool:
        """Verify token belongs to user - ISSUE: No type checking"""
        payload = self.decode_token(token)
        if not payload:
            return False
        # ISSUE: No type checking for expected_user_id
        return payload.get('user_id') == expected_user_id
    
    def get_user_from_token(self, token: str) -> Optional[str]:
        """Extract user from token - ISSUE: Bare except"""
        try:
            payload = self.decode_token(token)
            if payload:
                return payload.get('user_id')
        except:  # ISSUE: Bare except catches SystemExit
            pass
        return None
    
    def create_token(self, user_id: str, expires_in_hours: int = 24) -> str:
        """Create JWT token"""
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=expires_in_hours),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")
