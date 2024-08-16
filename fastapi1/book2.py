from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        
BOOKS = [
    Book(1, 'Computer science', 'coding row', 'A very nice book', 5),
    Book(2, 'Fast API', 'coding row', 'A very nice book', 3),
    Book(3, 'Master endpoints', 'coding row', 'A very nice book', 2),
    Book(4, 'DE', 'coding row', 'A very nice book', 6),
    Book(5, 'HCP 1', 'coding row', 'A very nice book', 7),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


