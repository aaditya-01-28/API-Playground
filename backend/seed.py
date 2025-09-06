from app import app, db
from models import Profile, Skill, Project, Work

def seed_data():
    # Clear all existing data from the database
    db.drop_all()
    db.create_all()

    # --- UPDATED Profile Information ---
    profile = Profile(
        name="AADITYA PRABHAKAR",
        email="aadityaprabhakar01@gmail.com",
        education="Bachelor of Engineering, Major in Computer Science - OP JINDAL UNIVERSITY",
        github_link="https://github.com/aaditya-01-28",
        linkedin_link="https://linkedin.com/in/aaditya-prabhakar-ab4ab527a",
        
        # --- ADD THE NEW DATA BELOW ---
        summary="An enthusiastic and result-driven Computer Science Engineer with expertise in Python, AI/ML, IoT, and full-stack development along with strong problem-solving, project management, and rapid prototyping skills.",
        technical_skills={
            "Programming": "Python, JavaScript, SQL, HTML, CSS",
            "Frameworks & Libraries": "Flask, React, Socket.IO, Pandas, NumPy, TensorFlow, Scikit-learn, Matplotlib, OpenCV",
            "Databases & Cloud": "PostgreSQL, MySQL, Firebase, Google Cloud, Redis",
            "Tools & Platforms": "Git, Docker, Tableau, MS Excel, Raspberry Pi, n8n, Canva"
        },
        internship={
            "organization": "Jindal Steel",
            "duration": "June 2025 - August 2025",
            "details": "Built an Al-based system using OpenCV to detect water spills from CCTV feeds in real time. Trained a custom image classifier to identify wet surfaces and automated alert notifications."
        },
        achievements=[
            "1st Place Winner - IoT & Hardware, INNOVATE 4.0 Hackathon, GIET University (Apr 2025)",
            "Coordinator - TECHNOROLLIX 2K25, National Tech Fest at OP Jindal University (Mar 2025)"
        ]
    )
    db.session.add(profile)

    # --- Technical Skills (for projects) ---
    skills = {}
    skill_names = [
        "Python", "JavaScript", "SQL", "HTML", "CSS", "Flask", "React", "Socket.IO", "Pandas", "NumPy", "TensorFlow", 
        "Scikit-learn", "Matplotlib", "OpenCV", "Node.js", "React Native", "PostgreSQL", "MySQL", "Firebase", "Google Cloud", "Redis",
        "Git", "Docker", "Tableau", "MS Excel", "Raspberry Pi", "n8n", "Canva", "Machine Learning", "Deep Learning", "CNN", "NLP", "Computer Vision",
        "IoT", "MQTT", "WebSocket", "GPS Modules"
    ]
    for name in skill_names:
        skill = Skill(name=name)
        skills[name] = skill
        db.session.add(skill)

    # --- Projects ---
    p1 = Project(
        title="Smart Water Detection System",
        description="AI-driven CCTV surveillance system to detect water spills and wet surfaces in industrial environments, ensuring workplace safety. Integrated real-time alerting via WhatsApp and automated incident logging to Google Drive.",
        link="https://github.com/aaditya-01-28/Smart-Water-Detection-System",
        skills=[skills["Python"], skills["OpenCV"], skills["CNN"], skills["Flask"]]
    )
    p2 = Project(
        title="E-Bike Digital Dashboard",
        description="Designed an IoT-powered digital dashboard for an e-bike to display real-time telemetry including GPS location, temperature, battery percentage, headlights, and indicators.",
        link="https://github.com/aaditya-01-28/E-Bike-Digital-Dashboard",
        skills=[skills["Raspberry Pi"], skills["Python"], skills["IoT"], skills["GPS Modules"]]
    )
    p3 = Project(
        title="Mesh It Up - Mesh Network Dashboard",
        description="Built a web-based dashboard to visualize and manage mesh network devices in real time. Supported live device data, file sharing, and private messaging across connected devices.",
        link="https://github.com/aaditya-01-28/Mesh-It-Up",
        skills=[skills["Flask"], skills["Socket.IO"], skills["Python"], skills["Raspberry Pi"], skills["HTML"], skills["CSS"], skills["JavaScript"]]
    )
    p4 = Project(
        title="Smart Parking Management System (Ongoing)",
        description="QR and geo-tagging-based automated parking system that assigns slots dynamically, manages vehicle entry logging, and tracks slot availability in real time.",
        link="https://github.com/aaditya-01-28/Smart-Parking-Management-System",
        skills=[skills["Python"], skills["Flask"], skills["SQL"], skills["Raspberry Pi"], skills["GPS Modules"]]
    )
    p5 = Project(
        title="Real-Time Bus Tracking System",
        description="Developed a backend and mobile system for live bus tracking with passenger-facing apps. Used GPS + MQTT for real-time updates, WebSocket for live maps, and PostgreSQL + Redis for efficient data handling.",
        link="https://github.com/aaditya-01-28/Real-Time-Bus-Tracking-System",
        skills=[skills["Node.js"], skills["PostgreSQL"], skills["Redis"], skills["MQTT"], skills["WebSocket"], skills["React"], skills["React Native"], skills["Docker"]]
    )
    db.session.add_all([p1, p2, p3, p4, p5])
    
    db.session.commit()
    print("Database seeded successfully with detailed resume data!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()