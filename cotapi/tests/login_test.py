import sys

if "/Users/euanblackledge/Desktop/code/cotapi/cotapi" not in sys.path:
    sys.path += ["/Users/euanblackledge/Desktop/code/cotapi/cotapi"]

import login

def test_verify_works_with_valid_password():
    verified = login.verify_password('password', '$2b$12$XTROw3rZ8/pHzFjIalDbeOSA1neYmSI5ga9FBjMxCVeUZJQJjxw..')
    assert verified == True

def test_verify_catches_invalid_password():
    verified = login.verify_password('not_password', '$2b$12$U0eLT6orXi.JdvJudDVJuuM1qvDyEmjINPq1b4YPa2pVKPxUcFY..')
    assert verified == False

sys.path.remove("/Users/euanblackledge/Desktop/code/cotapi/cotapi")
