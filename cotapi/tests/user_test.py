import sys
import pytest
if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

from user import UserPersistance

def test_create_user_creates_user():
    user_to_create = UserPersistance('steve', 'password')
    created = user_to_create.create_user()
    assert created == True

def test_can_delete_user():
    user_to_delete = UserPersistance('steve')
    deleted = user_to_delete.delete_user()
    assert deleted.deleted_count == 1

sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
