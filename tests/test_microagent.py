def test_get_status():
    from microagents.example_microagent import get_status
    result = get_status()
    assert result["status"] == "ok"
