from fastapi import Depends, HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone

from app.config import settings

from fastapi.security.oauth2 import OAuth2PasswordBearer
oauth2_schema = OAuth2PasswordBearer(tokenUrl='user/login')


def create_token(data: dict, expires_delta: timedelta | None = None):
    """
    Crea un token nuevo.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credential_expection):
    """
    Verifica el token
    """
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=settings.ALGORITHM)
        user_id: int = payload.get('sub')
        if user_id is None:
            raise credential_expection
    except jwt.ExpiredSignatureError:
        raise credential_expection
    except InvalidTokenError:
        raise credential_expection
    return payload

def get_current_user(token: str = Depends(oauth2_schema)):
    """
    Devuelve el id del usuario si el token es valido
    """
    credential_expection = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credential",
                                         headers={"WWW-Authenticate":"Bearer"})

    payload = verify_token(token,credential_expection)
    user_id: int = payload.get('sub')
    return user_id

def get_editor_user(token: str = Depends(oauth2_schema)):
    credential_expection = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credential",
                                         headers={"WWW-Authenticate":"Bearer"})
    """
    Devuelve el id del usuario editor si el token pertenece a uno con ese rol
    """

    payload = verify_token(token,credential_expection)
    role: int = payload.get('role')
    user_id: int = payload.get('sub')
    if role in settings.CAN_EDIT_ROLES:
        return user_id
    else:
        raise credential_expection