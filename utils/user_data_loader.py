import os
from dotenv import load_dotenv

load_dotenv()

def get_user():
    """
    Returns valid user credentials from environment variables.
    """
    return {
        "username": os.environ.get("SAUCE_USERNAME"),
        "password": os.environ.get("SAUCE_PASSWORD")
    }