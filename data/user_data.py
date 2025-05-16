import random
import string


def generate_user_data():
    username = 'user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return {
        "username": username,
        "password": password,
    }
