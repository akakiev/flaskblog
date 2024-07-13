# FlaskBlog Project

FlaskBlog is a web application built with Flask, SQLite, HTML, Jinja2, and Bootstrap. It allows users to create, read, update, and delete blog posts.

## Features
- Create new blog posts
- Display all blog posts
- View individual blog posts
- Edit existing blog posts
- Delete blog posts

## Project Structure
```plaintext
flaskblog/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── home.html
│   │   ├── post.html
│   │   ├── edit_post.html
│   │   ├── create_post.html
│   ├── static/
│       ├── css/
│           ├── styles.css
├── instance/
│   ├── flaskblog.sqlite
├── config.py
├── run.py
└── requirements.txt
```

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/flaskblog.git
    cd flaskblog
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database:**
    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

### Running the Application

1. **Start the Flask development server:**
    ```bash
    python run.py
    ```

2. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000
    ```

## Project Files

### `app/__init__.py`
This file initializes the Flask application and sets up the SQLAlchemy database.

### `app/routes.py`
This file defines the routes (URL endpoints) for the application, handling the logic for creating, reading, updating, and deleting blog posts.

### `app/models.py`
This file contains the SQLAlchemy database model for the blog posts.

### `app/templates/`
This directory contains the HTML templates for rendering the web pages.

- `layout.html`: Base template that includes the navigation bar and integrates Bootstrap.
- `home.html`: Template for displaying the list of blog posts.
- `post.html`: Template for displaying a single blog post.
- `edit_post.html`: Template for editing an existing blog post.
- `create_post.html`: Template for creating a new blog post.

### `config.py`
Configuration file for setting up the Flask application, including the database URI and secret key.

### `run.py`
Entry point for the Flask application. It runs the development server.

### `requirements.txt`
Lists the Python packages required for the project.

## Contributing
If you want to contribute to this project, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Bootstrap](https://getbootstrap.com/)
