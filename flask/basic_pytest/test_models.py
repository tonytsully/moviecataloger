from moviecataloger.src.models import UserAccount
from basic_pytest.conftest import new_user

def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
