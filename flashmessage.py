from flask import session


def create(name: str, value: str):
    if 'message' not in session:
        session['message'] = value


def get(name: str) -> str:
    value = session.get('message', '')
    session.pop('message', '')

    return value
