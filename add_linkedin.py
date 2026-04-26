with open('index.html', 'r') as f:
    html = f.read()

# Add LinkedIn to contact section
old_contact = '''<div class="contact-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>Missoula, Montana</span>
                        </div>'''

new_contact = '''<div class="contact-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>Missoula, Montana</span>
                        </div>
                        <div class="contact-item">
                            <a href="https://www.linkedin.com/in/jacesullivanmt/" target="_blank" style="color: inherit; text-decoration: none; display: flex; align-items: center; gap: 10px;">
                                <i class="fab fa-linkedin" style="font-size: 1.5rem; color: #0077b5;"></i>
                                <span>LinkedIn Profile</span>
                            </a>
                        </div>'''

html = html.replace(old_contact, new_contact)

# Also add a LinkedIn icon to the hero buttons area
old_buttons = '''<a href="#contact" class="btn btn-secondary">Get In Touch</a>
                </div>'''

new_buttons = '''<a href="#contact" class="btn btn-secondary">Get In Touch</a>
                    <a href="https://www.linkedin.com/in/jacesullivanmt/" target="_blank" class="btn btn-secondary" style="display: inline-flex; align-items: center; gap: 8px;"><i class="fab fa-linkedin"></i> LinkedIn</a>
                </div>'''

html = html.replace(old_buttons, new_buttons)

with open('index.html', 'w') as f:
    f.write(html)

print('LinkedIn added!')
