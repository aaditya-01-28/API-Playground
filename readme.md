# Developer API Playground: Aaditya Prabhakar

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack application that serves my professional profile—including a personal summary, skills, internship experience, achievements, and projects—through a RESTful API with a clean, interactive frontend.

### **Live Demo**
* **Frontend URL:**  https://startling-dasik-e35a26.netlify.app/
* **API Base URL:**  https://api-playground-ll3h.onrender.com
* **Resume URL:**    https://drive.google.com/file/d/1cqSnVINUI3nEt82CNWVxwXCEVpMF6U3I/view?usp=sharing

---

## 📸 Project Preview



---

## ✨ Features

* **Comprehensive Profile API**: Exposes a `/profile` endpoint with detailed personal data including summary, skills, internship, and achievements.
* **Dynamic Project Filtering**: The frontend allows for real-time filtering of projects by technical skill.
* **Decoupled Architecture**: A standalone vanilla JavaScript frontend (hosted on Netlify) that consumes a Python Flask backend API (hosted on Render).
* **Production-Ready Database**: Uses a cloud-hosted PostgreSQL database (from Neon) for robust and scalable data storage.
* **Health Check**: A `/health` endpoint to monitor API liveness.

---

## 🛠️ Technology Stack

| Category      | Technology                                                                                                                              |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend** | Python, Flask, Flask-SQLAlchemy                                                                                                         |
| **Database** | PostgreSQL (Neon)                                                                                                                       |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript                                                                                                         |
| **Deployment**| Render (Backend), Netlify (Frontend)                                                                                                    |

---

## 🚀 Getting Started Locally

Follow these instructions to get the project up and running on your local machine.

### **Prerequisites**
* Git
* Python 3.8+ and Pip
* A local PostgreSQL or MySQL installation

### **1. Clone & Setup**
```bash
# Clone the repository
git clone [https://github.com/yourusername/api-playground.git](https://github.com/aaditya-01-28/api-playground.git)

# Navigate to the project directory
cd api-playground/backend
```
2. Backend Setup
```Bash

# Create and activate a virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your local database URL
# Example for PostgreSQL:
# DATABASE_URL="postgresql://user:password@localhost:5432/dbname"

# Run the database seeder to populate it with your data
python seed.py

# Start the Flask server
python app.py
Your backend API should now be running at http://127.0.0.1:5000.
```
3. Frontend Setup
Open the frontend/script.js file.

Ensure the API_BASE_URL constant is set to http://127.0.0.1:5000.

Open the frontend/index.html file directly in your web browser.

# 📋 API Documentation
The API provides the following endpoints:

Method	Endpoint	Description
GET	/health	Checks the health of the API. Returns a 200 status.
GET	/projects	Returns a list of all projects.
GET	/projects?skill={name}	Returns projects filtered by a specific skill.
GET	/profile	Retrieves the main profile and contact information.

Export to Sheets
/profile Response Body
```bash

{
    "name": "AADITYA PRABHAKAR",
    "email": "aadityaprabhakar01@gmail.com",
    "education": "...",
    "links": {
        "github": "...",
        "linkedin": "...",
        "portfolio": "..."
    },
    "summary": "An enthusiastic and result-driven Computer Science Engineer...",
    "technical_skills": {
        "Programming": "Python, JavaScript, SQL, HTML, CSS",
        "Frameworks & Libraries": "Flask, React, Socket.IO, Pandas, ...",
        "...": "..."
    },
    "internship": {
        "organization": "Jindal Steel",
        "duration": "June 2025 - August 2025",
        "details": "Built an Al-based system using OpenCV..."
    },
    "achievements": [
        "1st Place Winner - IoT & Hardware, INNOVATE 4.0 Hackathon...",
        "Coordinator - TECHNOROLLIX 2K25..."
    ]
}
```
# ☁️ Deployment
This project is deployed with a decoupled, multi-cloud architecture:

The static frontend is hosted on Netlify.

The Flask backend is hosted as a Web Service on Render.

The PostgreSQL database is hosted on Neon and connected to the Render backend via an environment variable.
