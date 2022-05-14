from sample_packageee import sample_hello


def test_version():
    assert sample_hello() == "Hello"
