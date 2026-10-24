import unittest
from unittest.mock import MagicMock
from user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.repo_mock = MagicMock()
        self.service = UserService(self.repo_mock)

    def test_create_user_success(self):
        self.repo_mock.find_by_email.return_value = None
        self.repo_mock.save.return_value = {"id": 1, "name": "João", "email": "joao@email.com"}
        
        user = self.service.create_user("João", "joao@email.com")
        self.assertEqual(user["id"], 1)
        self.repo_mock.save.assert_called_once()

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.service.create_user("João", "invalid-email")

if __name__ == "__main__":
    unittest.main()