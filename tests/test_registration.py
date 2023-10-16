import unittest
from app import app

class TestRegistrationApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_valid_registration(self):
        response = self.app.post('/register', data=dict(username='newuser', password='newpassword', name='John Doe', phone='123-456-7890'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful for newuser', response.data)

    def test_existing_user_registration(self):
        # First, register a user to make the username 'user1' already taken
        response = self.app.post('/register', data=dict(username='user1', password='password1', name='Jane Smith', phone='987-654-3210'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful for user1', response.data)
        
        # Now, attempt to register the same username again
        response = self.app.post('/register', data=dict(username='user1', password='newpassword', name='John Doe', phone='123-456-7890'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already taken', response.data)

if __name__ == '__main__':
    unittest.main()
