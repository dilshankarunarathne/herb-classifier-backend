from datetime import timedelta

from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.user_model import UserInDB

from auth.authorize import authenticate_user, oauth2_scheme
from auth.hashing import get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, blacklist_token
from services.user_service import user_exists, get_next_avail_id, add_new_user

"""
    routers for authentication
"""