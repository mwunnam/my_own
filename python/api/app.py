#!/usr/bin/env python3
from flask import Flask, jsonify, request



app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Best Days', 'author': 'Michael Wunnam'},
    {'id': 2, 'title': 'Who Cares', 'author': 'David Cross'}
]


# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'book': books})


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({'book': book})
    else:
        return jsonify({'erro': 'book was not found'})


@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    book = [books for book in books if book['id'] != book_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
