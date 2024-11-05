import uuid as uuid_lib
import random
import string

def std_id() -> str:
    """Generates a lowercase 12-character random string."""
    return str(random_string(12).lower())

def short_id() -> str:
    """Generates a case-sensitive 6-character random string."""
    return random_string(6)

def redis_job_id() -> str:
    """Generates a case-sensitive 8-character random string for Redis keys."""
    return random_string(8)

def uuid() -> str:
    """Generates a UUID without dashes."""
    return str(uuid_lib.uuid4()).replace("-", "")

def random_string(length: int = 12) -> str:
    """Generates a random string of the given length containing letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
