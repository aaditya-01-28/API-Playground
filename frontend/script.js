const API_BASE_URL = 'https://api-playground-ll3h.onrender.com'; 

const projectsList = document.getElementById('projects-list');
const searchInput = document.getElementById('skill-search');

// Fetch and display the profile info
async function fetchProfile() {
    try {
        const response = await fetch(`${API_BASE_URL}/profile`);
        const profile = await response.json();
        displayProfile(profile);
    } catch (error) {
        console.error('Error fetching profile:', error);
    }
}

// Fetch and display projects, with an optional skill filter
async function fetchProjects(skill = '') {
    try {
        let url = `${API_BASE_URL}/projects`;
        if (skill) {
            url += `?skill=${encodeURIComponent(skill)}`;
        }
        const response = await fetch(url);
        const projects = await response.json();
        displayProjects(projects);
    } catch (error) {
        console.error('Error fetching projects:', error);
    }
}

// --- Functions to render data into HTML ---

function displayProfile(profile) {
    // --- Existing profile section ---
    document.getElementById('profile').innerHTML = `
        <h2>${profile.name}</h2>
        <p><strong>Email:</strong> ${profile.email} | <strong>Education:</strong> ${profile.education}</p>
        <div class="links">
            <a href="${profile.links.github}" target="_blank">GitHub</a> | 
            <a href="${profile.links.linkedin}" target="_blank">LinkedIn</a> | 
            <a href="${profile.links.portfolio}" target="_blank">Portfolio</a>
        </div>
    `;

    // --- NEW SECTIONS ---
    // Summary
    document.getElementById('summary').innerHTML = `
        <h2>Summary</h2>
        <p>${profile.summary}</p>
    `;

    // Internship
    if (profile.internship) {
        document.getElementById('internship').innerHTML = `
            <h2>Internship</h2>
            <div class="project-card">
                <h3>${profile.internship.organization}</h3>
                <p><strong>${profile.internship.duration}</strong></p>
                <p>${profile.internship.details}</p>
            </div>
        `;
    }
    
    // Technical Skills
    if (profile.technical_skills) {
        let skillsHtml = '<h2>Technical Skills</h2>';
        for (const category in profile.technical_skills) {
            skillsHtml += `<p><strong>${category}:</strong> ${profile.technical_skills[category]}</p>`;
        }
        document.getElementById('tech-skills').innerHTML = skillsHtml;
    }

    // Achievements
    if (profile.achievements) {
        let achievementsHtml = '<h2>Achievements</h2><ul>';
        profile.achievements.forEach(ach => {
            achievementsHtml += `<li>${ach}</li>`;
        });
        achievementsHtml += '</ul>';
        document.getElementById('achievements').innerHTML = achievementsHtml;
    }
}

function displayProjects(projects) {
    if (projects.length === 0) {
        projectsList.innerHTML = '<p>No projects found.</p>';
        return;
    }
    projectsList.innerHTML = projects.map(p => `
        <div class="project-card">
            <h3>${p.title}</h3>
            <p>${p.description}</p>
            <div class="skills">
                ${p.skills.map(s => `<span>${s}</span>`).join('')}
            </div>
            <a href="${p.link}" target="_blank">View Project</a>
        </div>
    `).join('');
}

// --- Event Listeners ---
searchInput.addEventListener('input', (e) => {
    fetchProjects(e.target.value);
});

// --- Initial Load ---
document.addEventListener('DOMContentLoaded', () => {
    fetchProfile();
    fetchProjects(); 
});