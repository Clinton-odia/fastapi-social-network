# FastAPI Social Network API

A production-ready social networking backend built with **FastAPI**, featuring user authentication, posts, comments, likes/upvotes, and secure password hashing with **bcrypt/passlib**.  

This project was designed as a portfolio-ready application to demonstrate backend engineering, API design, and database modeling with modern Python frameworks. It follows clean architecture principles and includes essential functionality expected in a real-world social platform.

---

## 🚀 Features

- **User Authentication**
  - User registration and login with JWT-based authentication
  - Secure password hashing using `bcrypt` via `passlib`

- **Posts**
  - Create, read, update, and delete posts
  - View all posts or posts by a specific user

- **Comments**
  - Add comments to posts
  - Read, update, and delete comments

- **Likes / Upvotes**
  - Like/unlike posts
  - Upvote/downvote comments

- **Database Layer**
  - SQLAlchemy ORM for relational database mapping
  - Alembic migrations for schema evolution

- **Error Handling & Validation**
  - Custom error responses using FastAPI exception handlers
  - Pydantic models for request/response validation

---

## 📂 Project Structure

```bash
fastapi-social-network/
│── app/
│   ├── main.py             # Application entry point
│   ├── database.py         # Database connection & session management
│   ├── models.py           # SQLAlchemy ORM models
│   ├── schemas.py          # Pydantic request/response schemas
│   ├── routers/            # Modular route handlers
│   │   ├── auth.py         # Authentication endpoints
│   │   ├── users.py        # User CRUD
│   │   ├── posts.py        # Post CRUD
│   │   ├── comments.py     # Comment CRUD
│   │   ├── likes.py        # Post/comment likes
│   ├── utils.py            # Helper functions (password hashing, token generation)
│   └── config.py           # Environment and settings
│
│── alembic/                # Database migrations
│── requirements.txt        # Python dependencies
│── README.md               # Documentation
