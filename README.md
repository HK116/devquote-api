# DevQuote API

A simple FastAPI project that returns random developer quotes.

## Features

- `GET /quote` — returns a random quote
- `GET /quotes` — returns all quotes
- `GET /quote/{id}` — returns a quote by ID

## How to Run

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

2. Install dependencies:
    ```bash
   pip install -r requirements.txt

3. Run the server:
    ```bash
   uvicorn app.main:app --reload

4. Access API docs at:
    ```bash
   http://127.0.0.1:8000/docs

## Testing
Run tests with:
    ```bash
    pytest

## Future improvements:

- Store quotes in a JSON file or database
- Add POST endpoint to add quotes
- Add pagination for `/quotes`
- Deploy using Docker or a cloud provider