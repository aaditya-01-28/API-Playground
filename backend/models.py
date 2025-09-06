from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON # Using JSON for lists

db = SQLAlchemy()

# Using association tables for many-to-many relationships (Skills <-> Projects, Skills <-> Work)
project_skills = db.Table('project_skills',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    education = db.Column(db.String(200))
    github_link = db.Column(db.String(200))
    linkedin_link = db.Column(db.String(200))
    portfolio_link = db.Column(db.String(200))
    # --- ADD THE NEW FIELDS BELOW ---
    summary = db.Column(db.Text)
    technical_skills = db.Column(JSON)
    internship = db.Column(JSON)
    achievements = db.Column(JSON)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200))
    # Relationship to skills
    skills = db.relationship('Skill', secondary=project_skills, lazy='subquery',
        backref=db.backref('projects', lazy=True))

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(100))
    description = db.Column(db.Text)