E-commerce API
A robust e-commerce REST API built with FastAPI, PostgreSQL, and Redis for caching and OTP management.
Features

User Authentication: Registration, login, and email verification with OTP
Product Management: CRUD operations for products
Category System: Organize products by categories
Comments: User reviews and comments on products
User Profiles: Profile management and product listings
Support System: User support messaging
Admin Panel: Administrative operations

Tech Stack

FastAPI: Modern Python web framework
PostgreSQL: Primary database
Redis: Caching and OTP storage
Docker: Containerization
Docker Compose: Multi-container orchestration
UV: Fast Python package installer
Uvicorn: ASGI server

Project Structure
.
├── admin/
│   ├── __init__.py
│   ├── auth.py
│   ├── product.py
│   └── user.py
├── database/
│   ├── __init__.py
│   ├── base.py
│   ├── category.py
│   ├── comment.py
│   ├── product.py
│   ├── support.py
│   └── user.py
├── root/
│   ├── __init__.py
│   └── config.py
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── category.py
│   ├── comment.py
│   ├── product.py
│   └── users.py
├── schemas/
│   ├── __init__.py
│   ├── product.py
│   └── user.py
├── services/
│   ├── __init__.py
│   └── otp_services.py
├── templates/
│   ├── login.html
│   └── verification_email.html
├── utils/
│   ├── __init__.py
│   ├── jwt_token.py
│   ├── supperuser.py
│   └── utils.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── env_exaple
└── main.py
API Endpoints
Authentication

POST /api/v1/auth/register - Register new user
POST /api/v1/auth/login - User login
POST /api/v1/auth/verification-email - Verify email with OTP

Products

POST /api/v1/products - Create product
GET /api/v1/products - Get all products
GET /api/v1/products/{product_id} - Get product by ID
DELETE /api/v1/products/{product_id} - Delete product

Categories

GET /api/v1/categories - Get all categories
POST /api/v1/categories - Create category
GET /api/v1/categories/{category_id}/products - Get products by category
DELETE /api/v1/categories/{category_id} - Delete category

Users

GET /api/v1/users/me - Get current user profile
PATCH /api/v1/users/me - Update current user profile
GET /api/v1/users/{user_id} - Get user by ID
GET /api/v1/users/me/products - Get current user's products
GET /api/v1/users/{user_id}/products - Get user's products
POST /api/v1/users/support-message - Send support message

Comments

GET /api/v1/products/{product_id}/comments - Get product comments
POST /api/v1/products/{product_id}/comments - Create comment
DELETE /api/v1/comments/{comments_id} - Delete comment

Setup

Clone the repository
Copy env_exaple to .env and configure your environment variables
Run with Docker Compose:

bashdocker-compose up -d
The API will be available at http://localhost:8000
Documentation
Interactive API documentation is available at:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc