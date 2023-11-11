import os


def get_full_api_url(route):
    return f'{os.getenv("API_BASE_URL")}/{route}'
