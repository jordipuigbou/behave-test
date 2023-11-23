from endpoints.health import Health

def test_health():
    health = Health()
    response = health.get()
    assert response == ({'status': 'ok'}, 200)
