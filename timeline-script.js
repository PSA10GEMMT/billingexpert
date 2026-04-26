// Mobile Navigation Toggle (same as script.js)
const navToggle = document.getElementById('mobile-menu');
const navMenu = document.querySelector('.nav-menu');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
    });
});

// Timeline interaction
document.addEventListener('DOMContentLoaded', () => {
    // Show timeline items as they come into view
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.timeline-item').forEach(item => {
        observer.observe(item);
    });
    
    // Toggle details on click
    const timelineContents = document.querySelectorAll('.timeline-content');
    
    timelineContents.forEach(content => {
        content.addEventListener('click', () => {
            const details = content.querySelector('.timeline-details');
            details.classList.toggle('active');
        });
        
        // Add hover effect to show more details are available
        content.addEventListener('mouseenter', () => {
            if (!content.querySelector('.timeline-details').classList.contains('active')) {
                content.style.transform = 'translateY(-5px)';
            }
        });
        
        content.addEventListener('mouseleave', () => {
            if (!content.querySelector('.timeline-details').classList.contains('active')) {
                content.style.transform = 'translateY(0)';
            }
        });
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    
    if (window.scrollY > 100) {
        navbar.style.padding = '10px 0';
        navbar.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.padding = '0';
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }
});