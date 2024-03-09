from bson import ObjectId
from app.database import collection

def test_add_note_success(test_client):
    """
    GIVEN a user is logged in 
    WHEN the user writes and submits a note with a post request
    THEN the note gets added to the database and displayed on screen
    """

    user_data = {"email": "newuser@example.com", "password": "testPassword"}
    
    test_client.post('/login', data=user_data)
    
    note_data = {
        "note": "This is a test note."
    }
    
    response = test_client.post('/', data=note_data, follow_redirects=True)
    
    
    assert b"Lift added" in response.data


