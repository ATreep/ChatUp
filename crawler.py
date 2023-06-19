import requests


def web_content(url: str) -> str:
    return requests.get(url).text


def api_response(url: str):
    return requests.get(url)
