import pytest
import requests


def test_website_online():
    sites = ["/", "/cow"]
    for i in sites:
        url = f"http://159.89.8.96{i}"

        response = requests.get(url)

        assert response.status_code == 200, f"De website {url} is offline. Statuscode: {response.status_code}"
