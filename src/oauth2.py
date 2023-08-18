from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta

from src import schemas, database, models
from src.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Using environment variables for secrets



def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, key = SECRET_KEY, algorithm=ALGORITHM)
    # jwt.encode()
    return encoded_jwt




def verify_access_token(token: str, credentials_exception):
    if token is None:
        raise credentials_exception

    try:

        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        user_id  = payload.get("user_id")
        

        if user_id is None:
            # print("no id")
            raise credentials_exception
    
        token_data = schemas.TokenData(id = str(user_id))

    except JWTError:
        raise credentials_exception

    return token_data


# """ We can use this to pass this as a dependency to any of our path operations, this will take the token from the request automatically
#  extract the id for us (verify) it will automatically fetch the user from the database and add it as a param for our path operations function """
# automatically sends users verified email to session state: db: Session = Depends(database.get_db)
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})
    
    if token is None:
        raise credentials_exception
    
    token_data = verify_access_token(token, credentials_exception)
    # print(token_data)
    user_id = int(token_data.id) if token_data.id is not None else None
    user = db.query(models.User).filter(models.User.id == user_id).first()

    # user = db.query(models.User).filter(models.User.id == int(token_data.id)).first()

    if user is None:
        raise credentials_exception
    
    # return verify_access_token(token, credentials_exception)

    return user