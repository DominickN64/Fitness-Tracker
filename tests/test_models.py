from app.models import User


def test_new_user():
    """
    GIVEN a User object is declared with a specific ID
    WHEN that User is logged in
    THEN check that the users properties are correct
    """
    user = User(101)
    assert user.id == '101'
    assert user.is_authenticated
    assert user.is_active
    assert user.is_anonymous == False
     
