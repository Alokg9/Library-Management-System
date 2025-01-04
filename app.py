from flask import Flask, request, jsonify
from database import books_db, members_db, book_id_counter, member_id_counter
from auth import is_authenticated

app = Flask(__name__)

# Pagination helper function
def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = -(-len(items) // per_page)  # Ceiling division
    return {
        "items": items[start:end],
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "total_items": len(items),
    }

# CRUD for Books
@app.route('/books', methods=['POST'])
def create_book():
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data.get('title') or not data.get('author'):
        return jsonify({"error": "Title and author are required"}), 400

    global book_id_counter
    new_book = {"id": book_id_counter, "title": data['title'], "author": data['author']}
    books_db.append(new_book)
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route('/books', methods=['GET'])
def list_books():
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    search = request.args.get('search', '').lower()
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    filtered_books = [book for book in books_db if search in book['title'].lower() or search in book['author'].lower()]
    return jsonify(paginate(filtered_books, page, per_page)), 200

@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_book(book_id):
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    book = next((b for b in books_db if b['id'] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'GET':
        return jsonify(book), 200

    if request.method == 'PUT':
        data = request.json
        book.update({"title": data.get("title", book["title"]), "author": data.get("author", book["author"])})
        return jsonify(book), 200

    if request.method == 'DELETE':
        books_db.remove(book)
        return jsonify({"message": "Book deleted"}), 200

# CRUD for Members
@app.route('/members', methods=['POST', 'GET'])
def manage_members():
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    if request.method == 'POST':
        global member_id_counter
        data = request.json
        if not data.get('name'):
            return jsonify({"error": "Name is required"}), 400
        new_member = {"id": member_id_counter, "name": data['name']}
        members_db.append(new_member)
        member_id_counter += 1
        return jsonify(new_member), 201

    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        return jsonify(paginate(members_db, page, per_page)), 200

@app.route('/members/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_member(member_id):
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    member = next((m for m in members_db if m['id'] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    if request.method == 'GET':
        return jsonify(member), 200

    if request.method == 'PUT':
        data = request.json
        member.update({"name": data.get("name", member["name"])})
        return jsonify(member), 200

    if request.method == 'DELETE':
        members_db.remove(member)
        return jsonify({"message": "Member deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
