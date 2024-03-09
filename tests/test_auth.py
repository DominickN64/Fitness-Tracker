def test_app(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (starting point for the application)
    THEN check that the response is valid (app loads properly)
    """

    response = test_client.get('/login')
    assert response.status_code == 200


def test_sucessful_sign_up(test_client):
    """
    GIVEN data for the input fields of a brand new user
    WHEN user signs up by sending a post request to the url
    THEN the page redirects meaning the user sucessfully signed up
    """

    user_data = {
        "email": "newuser@example.com",
        "firstName": "User",
        "password1": "testPassword",
        "password2": "testPassword"
    }

    response = test_client.post("/sign-up", data=user_data)
    assert response.status_code == 302 #redirecting to another page 
    

def test_successful_login(test_client):
    """
    GIVEN data for an existing user from within the database
    WHEN user logs in by sending a post request to the url
    THEN the page redirects meaning the user sucessfully logged in
    """
    
    user_data = {"email": "newuser@example.com", "password": "testPassword"}
    
    
    response = test_client.post('/login', data=user_data)
    assert response.status_code == 302 #redirecting to another page


def test_sucessful_logout(test_client):
    """
    GIVEN a user is logged in
    WHEN the user logs out
    THEN the logout message is flashed meaning the logout was successful
    """

    response = test_client.get('/logout', follow_redirects=True)
    assert b"Successfully logged out" in response.data




