from random import choices
from string import ascii_letters, digits

SYMBOLS = "~`!@#$%^&*()_-+={[}]|\:;<,>.?/\"'"


def generate_password(length):
    characters = ascii_letters + digits + SYMBOLS
    return "".join(choices(characters, k=int(length)))
