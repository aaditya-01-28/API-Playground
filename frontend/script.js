// The base URL of your running backend
const API_BASE_URL = 'https://api-playground-ll3h.onrender.com'; 

const profileSection = document.getElementById('profile');
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
    profileSection.innerHTML = `
        <h2>${profile.name}</h2>
        <p><strong>Email:</strong> ${profile.email}</p>
        <p><strong>Education:</strong> ${profile.education}</p>
        <div class="links">
            <a href="${profile.links.github}" target="_blank">GitHub</a> | 
            <a href="${profile.links.linkedin}" target="_blank">LinkedIn</a> | 
            <a href="${profile.links.portfolio}" target="_blank">Portfolio</a>
        </div>
    `;
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