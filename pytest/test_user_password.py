import pytest
import json

class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read())
    
    def test_user_password(self, users):
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a weak password" %(user['name'])
            assert passwd != 'password', msg
            assert passwd != 'password123', msg