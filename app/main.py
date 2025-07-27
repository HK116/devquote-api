from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from app.quotes import quotes

app = FastAPI(title="DevQuote API", version="1.0.0")

class Quote(BaseModel):
    id: int
    author: str
    quote: str

@app.get("/quote", response_model=Quote)
def get_random_quote():
    import random
    return random.choice(quotes)

@app.get("/all_quotes", response_model=List[Quote])
def get_all_quotes():
    return quotes

@app.get("/quote/{quote_id}", response_model=Quote)
def get_quote_by_id(quote_id: int):
    for q in quotes:
        if q["id"] == quote_id:
            return q
    raise HTTPException(status_code=404, detail="Quote Not Found.")