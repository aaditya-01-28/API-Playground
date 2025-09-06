import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv # Import load_dotenv
from models import db, Profile, Skill, Project, Work

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)
# Configure the database to use the URL from the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
CORS(app) # This enables Cross-Origin Resource Sharing

# --- API Endpoints ---

@app.route('/health', methods=['GET'])
def health_check():
    """Liveness probe."""
    return jsonify({"status": "healthy"}), 200

@app.route('/profile', methods=['GET'])
def handle_profile():
    """Read the main profile."""
    profile = Profile.query.first()
    if not profile:
        return jsonify({"message": "Profile not found"}), 404
        
    return jsonify({
        "name": profile.name,
        "email": profile.email,
        "education": profile.education,
        "links": {
            "github": profile.github_link,
            "linkedin": profile.linkedin_link,
            "portfolio": profile.portfolio_link
        },
        # --- ADD THE NEW DATA TO THE RESPONSE ---
        "summary": profile.summary,
        "technical_skills": profile.technical_skills,
        "internship": profile.internship,
        "achievements": profile.achievements
    })

@app.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects, optionally filtered by skill."""
    skill_name = request.args.get('skill')
    query = Project.query
    
    if skill_name:
        query = query.join(Project.skills).filter(Skill.name.ilike(f"%{skill_name}%"))
        
    projects = query.all()
    
    result = [{
        "title": p.title,
        "description": p.description,
        "link": p.link,
        "skills": [s.name for s in p.skills]
    } for p in projects]
    
    return jsonify(result)

@app.route('/skills/top', methods=['GET'])
def get_top_skills():
    """A simple endpoint to return all skills (can be extended)."""
    skills = Skill.query.all()
    return jsonify([s.name for s in skills])

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create tables if they don't exist
    app.run(debug=True)