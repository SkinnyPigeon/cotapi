import sys
import pytest
if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

from user import UserPersistance, UserInDB


def test_create_user_creates_user():
    user_to_create = UserPersistance('steve', 'password')
    created = user_to_create.create_user()
    assert created is True


def test_can_delete_user():
    user_to_delete = UserPersistance('steve')
    deleted = user_to_delete.delete_user()
    assert deleted.deleted_count == 1


def test_can_load_user():
    user_to_load = UserPersistance('euan')
    loaded_user = user_to_load.load_user()
    expected_user = {'username': 'euan',
                     'disabled': False,
                     'address': '51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23',
                     'key': '$2b$12$U0eLT6orXi.JdvJudDVJuuM1qvDyEmjINPq1b4YPa2pVKPxUcFY..'}
    expected_user = UserInDB(**expected_user)
    assert type(loaded_user) == type(expected_user)
    assert loaded_user.address == expected_user.address


sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
