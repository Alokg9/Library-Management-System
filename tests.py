import unittest
from app import app

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.headers = {"Authorization": "Bearer securetoken123"}

    def test_create_book(self):
        response = self.app.post('/books', json={"title": "1984", "author": "George Orwell"}, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_list_books(self):
        response = self.app.get('/books', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_unauthorized(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
