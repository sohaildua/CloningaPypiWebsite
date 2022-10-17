import pypi_org.data.db_session as db_session

from typing import Optional
from pypi_org.data.users import User
from passlib.handlers.sha2_crypt import sha512_crypt as cyrpto


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()


def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()


def get_user_by_id(id: int) -> Optional[User]:
    session = db_session.create_session()
    user =session.query(User).filter(User.id == id).first()
    return user


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None
    user = User()
    user.email = email
    user.name = name
    user.hashed_password = hash_text(password)
    session = db_session.create_session()
    session.expire_on_commit = False

    session.add(user)
    session.commit()


    return user


def hash_text(text: str) -> str:
    hashed_text = cyrpto.encrypt(text, rounds=171204)
    return hashed_text


def verify_text(plain_text: str, hashed_text: str) -> str:
    return cyrpto.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_text(password, user.hashed_password):
        return None
    return user
