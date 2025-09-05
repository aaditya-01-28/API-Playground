# Developer API Playground: Aaditya Prabhakar

A full-stack application that serves my professional profile—including skills, projects, and work experience—through a RESTful API with a clean, interactive frontend.

---

## 🌐 Live Demo

**Frontend URL:** [Your Frontend Deployment Link]  
**API Base URL:** [Your Backend Deployment Link]

📸 **Project Preview**  
*(Add a screenshot or GIF of your running application here)*

---

## ✨ Features

- **RESTful API:** Exposes endpoints for all professional data, including profile, projects, skills, and work history.  
- **Dynamic Project Filtering:** Frontend supports real-time filtering of projects by technical skill.  
- **Decoupled Architecture:** Vanilla JavaScript frontend consuming a Python (Flask) backend API.  
- **Production-Ready Database:** PostgreSQL for robust and scalable data storage.  
- **Health Check Endpoint:** `/health` endpoint to monitor API liveness.

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Backend  | Python, Flask, Flask-SQLAlchemy |
| Database | PostgreSQL |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Deployment | Render (Backend & Database), Netlify/Vercel (Frontend) |

---

## 🚀 Getting Started Locally

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Git  
- Python 3.8+ and pip  
- Local PostgreSQL installation

---

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/api-playground.git

# Navigate to the project directory
cd api-playground
```
2. Backend Setup
```bash
Copy code
# Navigate to backend
cd backend

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL database and user
# (Open psql and run commands to create user and database)

# Create .env file with your database URL
echo 'DATABASE_URL="postgresql://user:password@localhost:5432/dbname"' > .env

# Seed the database
python seed.py

# Start Flask server
python app.py
Your backend API should now be running at http://127.0.0.1:5000.
```
3. Frontend Setup
Open frontend/script.js and set:

```bash
const API_BASE_URL = "http://127.0.0.1:5000";
Open frontend/index.html directly in your web browser.
```
# 📋 API Documentation
Method	Endpoint	Description
```bash
GET	/health	Checks the health of the API. Returns a 200 status.
GET	/profile	Retrieves main profile and contact information.
GET	/projects	Returns a list of all projects.
GET	/projects?skill={name}	Returns projects filtered by a specific skill (e.g., ?skill=Python).
```
# ☁️ Deployment
Flask backend + PostgreSQL hosted on Render. Internal connection string via environment variable.

Static frontend hosted on Netlify/Vercel. Frontend configured to make API calls to live Render backend.

# 📈 Future Improvements
Authentication: JWT-based auth for POST/PUT/DELETE endpoints.

Pagination: Implement for /projects endpoint.

Testing: Unit tests for API endpoints.

CI/CD: Automate testing and deployment using GitHub Actions.

# 📄 License
This project is licensed under the MIT License. See LICENSE for details.