import sys
import pytest

if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

import login
import user

pytestmark = pytest.mark.asyncio


@pytest.mark.skip("Relies on having the same password hash")
def test_verify_works_with_valid_password():
    verified = login.verify_password('password', '$2b$12$XTROw3rZ8/pHzFjIalDbeOSA1neYmSI5ga9FBjMxCVeUZJQJjxw..')
    assert verified is True


def test_verify_catches_invalid_password():
    verified = login.verify_password('not_password', '$2b$12$U0eLT6orXi.JdvJudDVJuuM1qvDyEmjINPq1b4YPa2pVKPxUcFY..')
    assert verified is False


@pytest.mark.skip("Relies on having the same password hash")
def test_authenticate_user_returns_user():
    authenticated_user = login.authenticate_user('euan', 'password')
    expected_user = {'username': 'euan',
                     'disabled': False,
                     'address':
                     '51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23',
                     'key': '$2b$12$XTROw3rZ8/pHzFjIalDbeOSA1neYmSI5ga9FBjMxCVeUZJQJjxw..'
                     }
    assert authenticated_user == user.UserInDB(**expected_user)


def test_token_created():
    token = login.create_access_token({'sub': 'euan'})
    assert token[:2] == 'ey'
    assert len(token) == 123


@pytest.mark.skip("Relies on having the same password hash")
async def test_get_current_user_returns_user_with_valid_token():
    token = login.create_access_token({'sub': 'euan'})
    current_user = await login.get_current_user(token)
    expected_user = {'username':
                     'euan', 'disabled': False,
                     'address': '51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23',
                     'key': '$2b$12$XTROw3rZ8/pHzFjIalDbeOSA1neYmSI5ga9FBjMxCVeUZJQJjxw..'}
    assert current_user == user.UserInDB(**expected_user)


@pytest.mark.skip("Relies on having the same password hash")
async def test_get_current_active_user_returns_valid_user():
    token = login.create_access_token({'sub': 'euan'})
    current_user = await login.get_current_user(token)
    active_user = await login.get_current_active_user(current_user)
    expected_user = {'username':
                     'euan',
                     'disabled': False,
                     'address': '51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23',
                     'key': '$2b$12$XTROw3rZ8/pHzFjIalDbeOSA1neYmSI5ga9FBjMxCVeUZJQJjxw..'}
    assert active_user == user.UserInDB(**expected_user)


sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
