""" tests """
from fastapi.testclient import TestClient
from app.main import app
from app.settings import settings


def test_app():
    """ tests endpoint """
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"Hello": "World"}
