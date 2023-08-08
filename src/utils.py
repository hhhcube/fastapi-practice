from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# take inputed password and hash it then compare to hashed password in database
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
