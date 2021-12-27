from moviecataloger.src.models import UserAccount
import pytest

@pytest.fixture(scope='module')
def new_user():
    user = UserAccount('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user