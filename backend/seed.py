# backend/seed.py
from app import app, db
from models import Profile, Skill, Project, Work

def seed_data():
    # Clear all existing data from the database
    db.drop_all()
    db.create_all()

    # --- Profile Information ---
    profile = Profile(
        name="AADITYA PRABHAKAR",
        email="aadityaprabhakar01@gmail.com",
        education="Bachelor of Engineering, Major in Computer Science - OP JINDAL UNIVERSITY",
        github_link="https://github.com/aaditya-01-28",     # <-- Update this
        linkedin_link="https://linkedin.com/in/aaditya-prabhakar-ab4ab527a", # <-- Update this
        portfolio_link="https://yourportfolio.com"            # <-- Update this
    )
    db.session.add(profile)

    # --- Technical Skills ---
    # Create a dictionary to hold skill objects for easy reference
    skills = {}
    skill_names = [
        # Programming
        "Python", "JavaScript", "SQL", "HTML", "CSS",
        # Frameworks & Libraries
        "Flask", "React", "Socket.IO", "Pandas", "NumPy", "TensorFlow", 
        "Scikit-learn", "Matplotlib", "OpenCV", "Node.js", "React Native",
        # Databases & Cloud
        "PostgreSQL", "MySQL", "Firebase", "Google Cloud", "Redis",
        # Tools & Platforms
        "Git", "Docker", "Tableau", "MS Excel", "Raspberry Pi", "n8n", "Canva",
        # AI/ML & IoT
        "Machine Learning", "Deep Learning", "CNN", "NLP", "Computer Vision",
        "IoT", "MQTT", "WebSocket", "GPS Modules"
    ]
    for name in skill_names:
        skill = Skill(name=name)
        skills[name] = skill
        db.session.add(skill)

    # --- Internship Experience ---
    internship_desc = (
        "• Built an Al-based system using OpenCV to detect water spills from CCTV feeds in real time.\n"
        "• Trained a custom image classifier to identify wet surfaces in industrial zones.\n"
        "• Automated alert notifications via WhatsApp and cloud logging to Google Drive.\n"
        "• Reduced manual monitoring by 80% and enabled alerts with under 2s latency."
    )
    jindal_internship = Work(
        company="Jindal Steel",
        role="AI/ML Intern (Implied)", # Role not specified, you can change this
        period="June 2025 - August 2025",
        description=internship_desc
    )
    db.session.add(jindal_internship)

    # --- Projects ---
    # Project 1: Smart Water Detection System
    p1 = Project(
        title="Smart Water Detection System",
        description="AI-driven CCTV surveillance system to detect water spills and wet surfaces in industrial environments, ensuring workplace safety. Integrated real-time alerting via WhatsApp and automated incident logging to Google Drive.",
        link="https://github.com/yourusername/project1", # <-- Update this
        skills=[skills["Python"], skills["OpenCV"], skills["CNN"], skills["Flask"]]
    )

    # Project 2: E-Bike Digital Dashboard
    p2 = Project(
        title="E-Bike Digital Dashboard",
        description="Designed an IoT-powered digital dashboard for an e-bike to display real-time telemetry including GPS location, temperature, battery percentage, headlights, and indicators.",
        link="https://github.com/yourusername/project2", # <-- Update this
        skills=[skills["Raspberry Pi"], skills["Python"], skills["IoT"], skills["GPS Modules"]]
    )
    
    # Project 3: Mesh It Up - Mesh Network Dashboard
    p3 = Project(
        title="Mesh It Up - Mesh Network Dashboard",
        description="Built a web-based dashboard to visualize and manage mesh network devices in real time. Supported live device data, file sharing, and private messaging across connected devices.",
        link="https://github.com/yourusername/project3", # <-- Update this
        skills=[skills["Flask"], skills["Socket.IO"], skills["Python"], skills["Raspberry Pi"], skills["HTML"], skills["CSS"], skills["JavaScript"]]
    )

    # Project 4: Smart Parking Management System
    p4 = Project(
        title="Smart Parking Management System (Ongoing)",
        description="QR and geo-tagging-based automated parking system that assigns slots dynamically, manages vehicle entry logging, and tracks slot availability in real time.",
        link="https://github.com/yourusername/project4", # <-- Update this
        skills=[skills["Python"], skills["Flask"], skills["SQL"], skills["Raspberry Pi"], skills["GPS Modules"]]
    )

    # Project 5: Real-Time Bus Tracking System
    p5 = Project(
        title="Real-Time Bus Tracking System",
        description="Developed a backend and mobile system for live bus tracking with passenger-facing apps. Used GPS + MQTT for real-time updates, WebSocket for live maps, and PostgreSQL + Redis for efficient data handling.",
        link="https://github.com/yourusername/project5", # <-- Update this
        skills=[skills["Node.js"], skills["PostgreSQL"], skills["Redis"], skills["MQTT"], skills["WebSocket"], skills["React"], skills["React Native"], skills["Docker"]]
    )

    db.session.add_all([p1, p2, p3, p4, p5])
    
    # Commit all changes to the database
    db.session.commit()
    print("Database seeded successfully with resume data!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()