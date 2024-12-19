import requests

API_URL = "http://127.0.0.1:8000"
API_TOKEN = "749f233e4ff64dda08c3132a8766656c"

def test_get_nodes():
    response = requests.get(f"{API_URL}/nodes/")
    assert response.status_code == 200

def test_get_node_with_relationships():
    node_id = 1  # Replace with valid ID
    response = requests.get(f"{API_URL}/nodes/{node_id}")
    assert response.status_code == 200

def test_add_node():
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    data = {"label": "TestNode", "properties": {"name": "Test"}}
    response = requests.post(f"{API_URL}/nodes/", json=data, headers=headers)
    assert response.status_code == 200

def test_delete_node():
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    node_id = 1  # Replace with valid ID
    response = requests.delete(f"{API_URL}/nodes/{node_id}", headers=headers)
    assert response.status_code == 200
