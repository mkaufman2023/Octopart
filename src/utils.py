"""
# utils

Utility functions and classes.
"""
import json
import requests
from pyjsonviewer import view_data


def view(data: list | dict) -> None:
    """
    Shows JSON data in a GUI window.

    ## Parameters
    - `data` ( *list* | *dict* ) - The data to view.
    """
    view_data(json_data=data)


def request(payload: dict | str | None = None, method: str = "POST") -> requests.Response:
    """
    Private wrapper around `requests.request()`.
    """
    response = requests.request(
        url = "https://octopart.com/api/v4/internal",
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="129", "Google Chrome";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        },
        json = payload,
        method = method,
    )
    response.raise_for_status()
    return response

