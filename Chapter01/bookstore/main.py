from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }

@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "authod_id": author_id,
        "name": "Ernest Hemingway"
    }

@app.get("/books")
async def read_books(year: int = None):
    if year:
        return {
            "year": year,
            "books": ["Book 1", "Book 2"]
        }
    return {"books": ["All Books"]}
#Page 16