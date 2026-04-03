from passlib.context import CryptContext

pwdcontext = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    return pwdcontext.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwdcontext.verify(plain_password, hashed_password)

