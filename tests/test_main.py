import pytest
from fastapi.testclient import TestClient

import app.main as app_main
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_counter():
    app_main.n_counter = 0


def test_favicon_endpoint():
    response = client.get("/favicon.ico")
    assert response.status_code == 204
    # Ensure favicon request did not increment counter
    assert app_main.n_counter == 0


def test_color_random_endpoint():
    response = client.get("/color/random")
    assert response.status_code == 200
    data = response.json()
    assert data["n"] == 1
    assert "sleep" in data
    assert "host" in data
    assert "date" in data
    assert "timestamp" in data
    assert "color" in data
    assert len(data["color"]) == 1
    assert data["X-Real-IP"] == ""
    assert data["X-Forwarded-Email"] == ""


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["n"] == 1
    assert "color" in data


def test_headers_extraction():
    headers = {
        "X-Real-IP": "172.31.18.68",
        "X-Forwarded-For": "172.31.18.68, 10.1.167.46",
        "X-Forwarded-Email": "user@example.com",
        "Authorization": "Bearer secrettoken123",
        "X-Auth-Request-User": "example_user",
        "X-Auth-Request-Email": "user@example.com",
        "X-Auth-Request-Access-Token": "accesstoken123",
        "X-Auth-Request-Groups": "admin,devs",
    }
    response = client.get("/color/random", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["X-Real-IP"] == "172.31.18.68"
    assert data["X-Forwarded-For"] == "172.31.18.68, 10.1.167.46"
    assert data["X-Forwarded-Email"] == "user@example.com"
    assert data["Authorization"] == "Bearer secrettoken123"
    assert data["X-Auth-Request-User"] == "example_user"
    assert data["X-Auth-Request-Email"] == "user@example.com"
    assert data["X-Auth-Request-Access-Token"] == "accesstoken123"
    assert data["X-Auth-Request-Groups"] == "admin,devs"
    assert data["X-Forwarded-User"] == ""


def test_color_by_name():
    response = client.get("/color/khaki")
    assert response.status_code == 200
    data = response.json()
    assert "khaki" in data["color"]
    assert data["color"]["khaki"]["hex"] == "#F0E68C"
    assert data["color"]["khaki"]["rgb"] == "(240,230,140)"
    assert data["color"]["khaki"]["name"] == "khaki"


def test_color_by_hex():
    response = client.get("/color/F0E68C")
    assert response.status_code == 200
    data = response.json()
    assert "khaki" in data["color"]

    response_with_hash = client.get("/color/%23F0E68C")
    assert response_with_hash.status_code == 200
    data_hash = response_with_hash.json()
    assert "khaki" in data_hash["color"]


def test_color_not_found():
    response = client.get("/color/unknowncolor123")
    assert response.status_code == 404


def test_colors_list_endpoint():
    response = client.get("/colors")
    assert response.status_code == 200
    data = response.json()
    assert "color" in data
    assert len(data["color"]) >= 130
    assert "khaki" in data["color"]


def test_counter_increment():
    r1 = client.get("/color/random")
    assert r1.json()["n"] == 1

    r_favicon = client.get("/favicon.ico")
    assert r_favicon.status_code == 204

    r2 = client.get("/color/khaki")
    assert r2.json()["n"] == 2


def test_color_random_text_endpoint():
    response = client.get("/color/random/text")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Color:" in response.text
    assert "Font Color:" in response.text
    assert "RGB:" in response.text
    assert "HEX:" in response.text
    assert "n: 1" in response.text


def test_color_text_by_name():
    response = client.get("/color/khaki/text")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "#F0E68C" in response.text
    assert "(240,230,140)" in response.text
    assert "khaki" in response.text
    assert "Font Color: black" in response.text


def test_color_text_by_hex():
    response = client.get("/color/F0E68C/text")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "khaki" in response.text

    response_with_hash = client.get("/color/%23F0E68C/text")
    assert response_with_hash.status_code == 200
    assert "khaki" in response_with_hash.text


def test_color_text_not_found():
    response = client.get("/color/unknowncolor123/text")
    assert response.status_code == 404


def test_dark_color_font_selection():
    response = client.get("/color/black/text")
    assert response.status_code == 200
    assert "Font Color: white" in response.text
