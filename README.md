# Library Management System API

 This is a Flask-based API designed for managing books and members in a library.
 The system supports CRUD operations, search functionality, pagination, and token-based authentication for secure access.

# Features:
 - Books Management: Add, view, update, and delete books.
 - Members Management: Manage library members with CRUD operations.
 - Search Functionality: Search books by title or author.
 - Pagination: Efficiently handle large datasets with paginated endpoints.
 - Authentication: Secure the API with token-based authentication.

# Requirements:
 Ensure you have the following installed before running the application:
 - Python 3.8 or higher
 - pip (Python package manager)

# Installation and Setup:

1. Clone the Repository:
git clone https://github.com/your-repo/library-management-api.git
cd library-management-api

2. Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows

3. Run the Application:
flask run
The API will be available at http://127.0.0.1:5000.

# Books:
 - GET /books: Retrieve a list of books with optional pagination.
 - POST /books: Add a new book.
 - GET /books/<id>: Retrieve details of a specific book.
 - PUT /books/<id>: Update a book's information.
 - DELETE /books/<id>: Delete a book.

# Members:
 - GET /members: Retrieve a list of members with optional pagination.
 - POST /members: Add a new member.
 - GET /members/<id>: Retrieve details of a specific member.
 - PUT /members/<id>: Update a member's information.
 - DELETE /members/<id>: Delete a member.

# License:
 This project is licensed under the MIT License. See the LICENSE file for details.

# Contact:
 For any queries or suggestions, please contact:
 - Email: alok.gupta.bnp@gmail.com
 - GitHub: https://github.com/ALokg9

Here are some output:
Create a Book:
![Screenshot 2025-01-04 201830](https://github.com/user-attachments/assets/c59d046c-4c23-4c9c-b681-95a8c5a4b963)

List Books:
![Screenshot 2025-01-04 201922](https://github.com/user-attachments/assets/2ed1a89d-c3a3-4264-9704-877267b7a9e4)

Search Books:
![Screenshot 2025-01-04 202002](https://github.com/user-attachments/assets/a273b1a1-c262-44b3-ade1-f9eabf886970)

Get a Single Book:
![Screenshot 2025-01-04 202034](https://github.com/user-attachments/assets/48f5e6c7-79f4-4bad-964f-afe88b690532)

Update a Book:
![Screenshot 2025-01-04 202109](https://github.com/user-attachments/assets/2a797a57-d6b2-434c-85da-b68b2a01b95e)

Delete a Book:
![Screenshot 2025-01-04 202143](https://github.com/user-attachments/assets/5aa40a8a-c1d1-4321-84bd-8ad0dc4f89f0)

Create a Member:
![Screenshot 2025-01-04 202227](https://github.com/user-attachments/assets/b2d08b5e-eb76-4511-a658-5b8706dedd94)

List Members:
![Screenshot 2025-01-04 202248](https://github.com/user-attachments/assets/62d0b03b-930c-4b19-b82c-9f31b1afaeb5)

Get a Single Member:
![Screenshot 2025-01-04 202313](https://github.com/user-attachments/assets/6423fdfb-79b6-4335-91d6-5b04dd8f5078)

Update a Member
![Screenshot 2025-01-04 202352](https://github.com/user-attachments/assets/92811d35-48d1-4620-aa4c-c570e3c60547)

Delete a Member
![Screenshot 2025-01-04 202425](https://github.com/user-attachments/assets/2f2ccbd2-54c9-4830-917b-74cf198ee99f)
