import uuid as uuid_lib
import random
import string


def std_id():
    # lower case 12 character random string
    return str(random_string(12).lower())

def short_id():
    # used for case sensitive ids
    return random_string(6)

def redis_job_id():
    # random case sensitive string becaus redis keys are case sensitive
    return random_string(8)

def uuid():
    # generates uuid without dashes
    return str(uuid_lib.uuid4()).replace("-", "")

def random_string(length: int = 12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
