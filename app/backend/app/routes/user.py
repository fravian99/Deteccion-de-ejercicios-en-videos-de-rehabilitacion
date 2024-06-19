
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app import auth, utils
from app.database import get_db
from app.schemas import AuthBase
from app.models import User
from app.controllers import user_controller, auth_controller


router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post("/new-user")
async def new_user(user: AuthBase, db: Session = Depends(get_db)):
    try:
        auth_controller.create_user(db, user)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail="Internal Error")
    return True

@router.post("/login/")
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user: User = user_controller.get_user_by_username(db=db, username=user_credentials.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    credentials = auth_controller.get_credentials_by_id(db = db, user_id=user.id)
    if not credentials or not utils.verify_password(user_credentials.password, credentials.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = auth.create_token(data={'user_id':user.id,'username':user.username,"rol":user.rol})
    return {"message": "Logged in successfully","token":token}
