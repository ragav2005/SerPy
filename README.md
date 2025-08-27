# SerPy

A simple ASGI web application built with Python.

## Description

SerPy is a basic ASGI (Asynchronous Server Gateway Interface) application that responds to HTTP requests with a welcome message.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ragav2005/SerPy.git
   cd SerPy
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using Uvicorn:

```bash
uvicorn Test:app --reload
```

The server will start on `http://127.0.0.1:8000`. Visit the URL in your browser to see the welcome message.

## Project Structure

- `SerPy.py`: The main ASGI application class.
- `Test.py`: Entry point for running the app.
- `requirements.txt`: List of Python dependencies.
