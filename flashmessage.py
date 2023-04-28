from flask import session


def create(name: str, value: str):
    if 'message' not in session:
        session['message'] = {}

    session['message'][name] = value


def get(name: str) -> str:
    if isinstance(session.get('message'), dict):
        value = session['message'].get(name)
        session['message'].pop(name, None)

        return value

    return ''
