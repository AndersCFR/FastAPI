from fastapi import FastAPI, Body


app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author 1', 'category': 'Science'},
    {'title': 'Title Two', 'author': 'Author 2', 'category': 'Science'},
    {'title': 'Title 3', 'author': 'Author 3', 'category': 'History'},
    {'title': 'Title 4', 'author': 'Author 4', 'category': 'Math'},
    {'title': 'Title 5', 'author': 'Author 5', 'category': 'Math'},
]

@app.get("/books")
async def reload_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_all_books():
    return {'book_titls': 'mybook'}


# Path parameter
@app.get("/books/{book_title}/")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

#Query parameter
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return        
    
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        print(book.get('author'))
        if book.get('author').casefold() == book_author.casefold() and\
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Post, accessing to body request
@app.post("/books/create_book/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Put
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# Delete
@app.delete("/books/delete_book/{book_title}/")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# Books by author
@app.get("/books/by_author")
async def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)    
    return books_to_return

