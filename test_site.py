import pytest
import requests


def test_website_online():
    sites = ["/", "/cow"]
    for i in sites:
        url = f"http://142.93.110.2{i}"

        response = requests.get(url)

        assert response.status_code == 200, f"De website {url} is offline. Statuscode: {response.status_code}"
