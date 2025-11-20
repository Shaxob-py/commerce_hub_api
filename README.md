<div align="center">

# 🚀 FastAPI AI Travel Agent

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=32&duration=3000&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=FastAPI+AI+Travel+Agent;Intelligent+Trip+Planning;Redis+%2B+PostgreSQL+Powered;Next-Gen+Travel+Assistant" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-00D4FF?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=1a1a1a" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=1a1a1a" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white&labelColor=1a1a1a" alt="Redis"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=1a1a1a" alt="Docker"/>
  <img src="https://img.shields.io/badge/Python-3.11+-FFD43B?style=for-the-badge&logo=python&logoColor=1a1a1a&labelColor=1a1a1a" alt="Python"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="800">
</p>



---

</div>

## 🎯 Project Overview

<table>
<tr>
<td width="60%">

### 🌟 **What Makes This Special?**


**Key Benefits:**
- 🚀 **Lightning Fast**: Sub-100ms response times
- 🔒 **Enterprise Ready**: Secure authentication and data protection
- 📈 **Scalable**: Built for growth with Redis caching
</td>
<td width="40%">

```python
@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.create_all()
    admin.mount_to(app)
    print('project ishga tushdi')
    yield
    # await db.drop_all()
    print('project toxtadi')


app = FastAPI(docs_url='/', root_path='/api', title="Commerce Hub API", lifespan=lifespan, )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    msg = exc.args[0][0]['msg']
    return JSONResponse(
        {'message': msg},
        status.HTTP_400_BAD_REQUEST,
    )


app = FastAPI(
    docs_url='/',

    title="Commerce Hub API",
    description="api/vi",
    lifespan=lifespan,
)
```

</td>
</tr>
</table>

## ✨ Core Features

<div align="center">

### 🎨 **Feature Showcase**

</div>

<table>
<tr>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/FastAPI-Backend-00D4FF?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=1a1a1a"/>
<br/><strong>High-Performance API</strong>
<br/>Async endpoints with automatic documentation
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=1a1a1a"/>
<br/><strong>Robust Data Storage</strong>
<br/>Reliable relational database with migrations
</td>
<td align="center" width="25%">
<img src="https://img.shields.io/badge/Redis-Caching-FF4438?style=for-the-badge&logo=redis&logoColor=white&labelColor=1a1a1a"/>
<br/><strong>Lightning Cache</strong>
<br/>In-memory caching for optimal performance



<details>
<summary>🔥 <strong>Advanced Features</strong></summary>

### 🎯 **Authentication & Security**
- 🔐 **JWT Token Authentication**: Secure session management
- 📱 **OTP Verification**: SMS-based two-factor authentication
- 🛡️ **Password Hashing**: Bcrypt encryption for user data
- 🔒 **Rate Limiting**: Redis-based request throttling


### 🗄️ **Data Management**
- 👥 **User Profiles**: User
- ✈️ **Product**: Product
- 🌍 **Category Coverage**: Category
- 📚 **Support Message**: Support

### 🚀 **Performance & Deployment**
- ⚡ **Async Operations**: Non-blocking request handling
- 🐳 **Docker Containerization**: Easy deployment and scaling
- 📈 **Monitoring Ready**: Built-in health checks
- 🔄 **Database Migrations**: Alembic-powered schema management

</details>

## 🚀 Quick Start

### 📋 Prerequisites

<div align="center">

![Python 3.11+](https://img.shields.io/badge/Python-3.11+-FFD43B?style=flat-square&logo=python&logoColor=1a1a1a&labelColor=FFD43B)
![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?style=flat-square&logo=docker&logoColor=white&labelColor=2496ED)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat-square&logo=postgresql&logoColor=white&labelColor=4169E1)
![Redis](https://img.shields.io/badge/Redis-7+-FF4438?style=flat-square&logo=redis&logoColor=white&labelColor=FF4438)

</div>

### 🎮 **Option 1: Docker Compose (Recommended)**

```bash
# 🔥 One-command setup
git colone https://github.com/Shaxob-py/commerce_hub_api.git
cd fastapi-ai-agent
docker-compose up -d

# 🎉 That's it! API is running at http://localhost:8000
```

### 🛠️ **Option 2: Local Development**

<table>
<tr>
<td width="50%">

**1️⃣ Clone & Setup:**
```bash
git clone https://github.com/your-username/fastapi-ai-agent.git
cd fastapi-ai-agent

# Install UV (modern Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**2️⃣ Environment Setup:**
```bash
# Create virtual environment and install deps
uv sync

# Copy environment template
cp .env.example .env
```

</td>
<td width="50%">

**3️⃣ Database Setup:**
```bash
# Start PostgreSQL & Redis
docker-compose up postgres redis -d

# Run migrations
uv run alembic upgrade head
```

**4️⃣ Launch Application:**
```bash
# Development server with hot reload
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 🎊 Access: http://localhost:8000/docs
```

</td>
</tr>
</table>

## 🎯 API Endpoints

<div align="center">

### 🛣️ **REST API Routes**

</div>

<details>
<summary><b> User </b></summary>

```http

GET
/api/v1/users/{user_id}
GET
/api/v1/users/me
PATCH
/api/v1/users/me
GET
/api/v1/users/me/products
POST
/api/v1/users/support-message
GET
/api/v1/users/{user_id}/products
```

</details>



<details>
<summary><b>🌍 Product</b></summary>

```http
POST
/api/v1/products
GET
/api/v1/products
GET
/api/v1/products/{product_id}
DELETE
/api/v1/products/{product_id}
```

</details>

<details>
<summary><b>🔐 Auth </b></summary>

```http
POST
/api/v1/auth/register
POST
/api/v1/auth/login
POST
/api/v1/auth/verification-email
```

</details>






## 📁 Project Architecture

<div align="center">

### 🏗️ **Clean Architecture Design**

</div>

```

admin
__init__.py
auth.py
product.py
user.py
database
__init__.py
base.py
category.py
comment.py
product.py
support.py
user.py
root
__init__.py
config.py
routers
__init__.py
auth.py
category.py
comment.py
product.py
users.py
schemas
__init__.py
product.py
user.py
services
__init__.py
otp_services.py
templates
login.html
verification_email.html
utils
__init__.py
jwt_token.py
supperuser.py
utils.py
.gitignore
Dockerfile
README.md
docker-compose.yml
env_exaple
main.py
pyproject.toml
test_main.http
uv.lock
```

## ⚙️ Configuration

<div align="center">

### 🎛️ **Environment Variables**

</div>

```bash
# 🗄️ Database Configuration
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=*
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1121

EMAIL_HOST="*"
EMAIL_PORT=465
EMAIL_USER="*"
EMAIL_PASSWORD="*"

REDIS_URL=redis://localhost:6379/1

JWT_SECRET_KEY=*
JWT_ALGORITHM=*
JWT_ACCESS_TOKEN_EXPIRE_TIME=60
JWT_REFRESH_TOKEN_EXPIRE_TIME=3600

```

## 🐳 Docker Deployment

<div align="center">

### 🏗️ **Production-Ready Setup**

</div>

```yaml
# docker-compose.yml
version: '3.9'

services:
  🚀 api:
    build: 
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://travel_user:secure_password@postgres:5432/travel_db
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - travel_network

  🗄️ postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: travel_db
      POSTGRES_USER: travel_user
      POSTGRES_PASSWORD: secure_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U travel_user -d travel_db"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - travel_network

  ⚡ redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - travel_network

volumes:
  postgres_data:
  redis_data:

networks:
  travel_network:
    driver: bridge
```



## 🎨 API Documentation

<div align="center">

### 📚 **Interactive Documentation**

[![Swagger UI](https://img.shields.io/badge/Swagger_UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=1a1a1a&labelColor=85EA2D)](http://localhost:8000/docs)
[![ReDoc](https://img.shields.io/badge/ReDoc-8A2BE2?style=for-the-badge&logo=readthedocs&logoColor=white&labelColor=8A2BE2)](http://localhost:8000/redoc)
[![OpenAPI](https://img.shields.io/badge/OpenAPI_3.0-6BA539?style=for-the-badge&logo=openapiinitiative&logoColor=white&labelColor=6BA539)](http://localhost:8000/openapi.json)

</div>

## 🛠️ Development Workflow

### 🤝 **Contributing Guidelines**

<div align="center">

<table>
<tr>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/1-Fork-FF6B6B?style=for-the-badge&logo=github&logoColor=white"/>
<br/>🍴 <strong>Fork</strong>
<br/>Create your copy
</td>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/2-Clone-4ECDC4?style=for-the-badge&logo=git&logoColor=white"/>
<br/>📥 <strong>Clone</strong>
<br/>Get local copy
</td>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/3-Branch-45B7D1?style=for-the-badge&logo=git&logoColor=white"/>
<br/>🌿 <strong>Branch</strong>
<br/>Create feature branch
</td>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/4-Code-96CEB4?style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
<br/>💻 <strong>Code</strong>
<br/>Implement features
</td>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/5-Test-FECA57?style=for-the-badge&logo=pytest&logoColor=white"/>
<br/>🧪 <strong>Test</strong>
<br/>Ensure quality
</td>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/6-Commit-FF9FF3?style=for-the-badge&logo=git&logoColor=white"/>
<br/>📝 <strong>Commit</strong>
<br/>Save changes
</td>
<td align="center" width="14%">
<img src="https://img.shields.io/badge/7-PR-54A0FF?style=for-the-badge&logo=github&logoColor=white"/>
<br/>🔄 <strong>PR</strong>
<br/>Submit changes
</td>
</tr>
</table>

</div>

```bash
# 🌿 Create feature branch
git checkout -b feature/amazing-new-feature

# 💻 Make your changes
# ... code, code, code ...

# 🧪 Test your changes
make test

# 📝 Commit with conventional commits
git commit -m "✨ feat(api): add trip recommendation endpoint"

# 🚀 Push and create PR
git push origin feature/amazing-new-feature
```
## 🔧 Technology Stack

<div align="center">

### 🚀 **Modern Backend Technologies**

<table>
<tr>
<th align="center">🎯 Category</th>
<th align="center">🛠️ Technology</th>
<th align="center">📝 Purpose</th>
<th align="center">🏆 Version</th>
</tr>
<tr>
<td align="center">🌐 <strong>Web Framework</strong></td>
<td align="center"><img src="https://img.shields.io/badge/FastAPI-00D4FF?style=flat&logo=fastapi&logoColor=white"/> FastAPI</td>
<td align="center">High-performance async API</td>
<td align="center"><code>Latest</code></td>
</tr>
<tr>
<td align="center">🗄️ <strong>Database</strong></td>
<td align="center"><img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white"/> PostgreSQL</td>
<td align="center">Primary data storage</td>
<td align="center"><code>15+</code></td>
</tr>
<tr>
<td align="center">⚡ <strong>Cache</strong></td>
<td align="center"><img src="https://img.shields.io/badge/Redis-FF4438?style=flat&logo=redis&logoColor=white"/> Redis</td>
<td align="center">Caching & session management</td>
<td align="center"><code>7+</code></td>
</tr>
<tr>
<td align="center">📦 <strong>Package Manager</strong></td>
<td align="center"><img src="https://img.shields.io/badge/UV-FF6B6B?style=flat&logo=python&logoColor=white"/> UV</td>
<td align="center">Fast Python package manager</td>
<td align="center"><code>Latest</code></td>
</tr>
<tr>
<td align="center">🔄 <strong>Migrations</strong></td>
<td align="center"><img src="https://img.shields.io/badge/Alembic-green?style=flat&logo=python&logoColor=white"/> Alembic</td>
<td align="center">Database schema management</td>
<td align="center"><code>Latest</code></td>
</tr>
<tr>
<td align="center">📐 <strong>Validation</strong></td>
<td align="center"><img src="https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=python&logoColor=white"/> Pydantic</td>
<td align="center">Data validation & serialization</td>
<td align="center"><code>V2</code></td>
</tr>
<tr>
<td align="center">🐳 <strong>Containerization</strong></td>
<td align="center"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white"/> Docker</td>
<td align="center">Application containerization</td>
<td align="center"><code>Latest</code></td>
</tr>
<tr>
</table>

</div>


## 🆘 Support & Resources

<div align="center">

### 🤝 **Get Help**

[![GitHub Issues](https://img.shields.io/badge/GitHub_Issues-FF6B6B?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username/fastapi-ai-agent/issues)
[![API Documentation](https://img.shields.io/badge/API_Docs-4ECDC4?style=for-the-badge&logo=swagger&logoColor=white)](http://localhost:8000/docs)
[![Discussions](https://img.shields.io/badge/Discussions-45B7D1?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username/fastapi-ai-agent/discussions)

</div>
