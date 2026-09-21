"""Login step for the project.

Like input_variables.py, the prompts fall back to defaults so the program stays
runnable when there is no interactive terminal.

Added on the feature-login branch: credential validation plus an
is_authenticated() helper that the rest of the project can rely on.
"""

MIN_PASSWORD_LENGTH = 4


def read_text(prompt, default):
    try:
        value = input(prompt)
    except EOFError:
        value = ""
    if not value:
        print("   -> no input available, using default:", default)
        return default
    return value


def is_authenticated(name=None, password=None):
    """Return True only when both credentials are present and look valid."""
    name = user_name if name is None else name
    password = pass_word if password is None else password
    if not name or not password:
        return False
    if len(password) < MIN_PASSWORD_LENGTH:
        print("   -> password is too short, authentication refused")
        return False
    return True


user_name = read_text("Enter username : ", "veerandra")
pass_word = read_text("Enter password : ", "demo-password")
