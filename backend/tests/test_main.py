from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_order_count():
    response = client.get("/order-count")
    assert response.status_code == 200
    assert "order_count" in response.json()

def test_read_current_position():
    response = client.get("/current-position/0")  # Assuming 0 is a valid index
    assert response.status_code == 200
    assert "position" in response.json()

def test_read_pick_info():
    response = client.get("/pick-info/0")  # Assuming 0 is a valid index
    assert response.status_code == 200
    assert "last_pick" in response.json()
    assert "current_pick" in response.json()
    assert "next_pick" in response.json()

# Add more tests as needed
