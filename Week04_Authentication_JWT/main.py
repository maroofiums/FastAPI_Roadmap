# from fastapi import FastAPI
# from app.database import create_db_and_tabeles

# app = FastAPI()

# @app.on_event("startup")
# def startup_event():
#     create_db_and_tabeles()

from app.core.security import hash_password, verify_password

hashed = hash_password("mysecretpassword")
print(f"Hashed password: {hashed}")
is_valid = verify_password("mysecretpassword", hashed)
print(f"Password valid: {is_valid}")
is_valid_wrong = verify_password("wrongpassword", hashed)
print(f"Wrong password valid: {is_valid_wrong}")
