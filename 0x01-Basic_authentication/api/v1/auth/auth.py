#!/usr/bin/env python3
"""
    Manage API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class to manage API requests"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Test """
        return False

    def authorization_header(self, request=None) -> str:
        """ Test """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Test """
        return None
