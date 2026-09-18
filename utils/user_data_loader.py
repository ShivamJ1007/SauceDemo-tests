import os
from dotenv import load_dotenv

load_dotenv()

def get_user():
    """
    Returns valid user credentials from environment variables.
    """
    return {
        "username": os.environ.get("USERNAME"),
        "password": os.environ.get("PASSWORD")
    }