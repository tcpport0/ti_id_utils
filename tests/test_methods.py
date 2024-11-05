from ti_id_utils import std_id, short_id, redis_job_id, uuid

def test_std_id():
    # Test length and case
    result = std_id()
    assert len(result) == 12
    assert result.islower()
    assert result.isalnum()

def test_short_id():
    # Test length and format
    result = short_id()
    assert len(result) == 6
    assert result.isalnum()

def test_redis_job_id():
    # Test length and format
    result = redis_job_id()
    assert len(result) == 8
    assert result.isalnum()

def test_uuid():
    # Test length and format without dashes
    result = uuid()
    assert len(result) == 32  # UUID without dashes is 32 chars
    assert result.isalnum()
    assert "-" not in result
