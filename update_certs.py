import re

with open('index.html', 'r') as f:
    html = f.read()

# Find the certifications section and add links
# We'll look for cert-related text and wrap/append links

cert_links = {
    'BillingPlatform': [
        {
            'name': 'Partner Accounting Pro Module 5: Contract Modifications',
            'url': 'https://verify.skilljar.com/c/qaq9cvr8q7r4',
            'date': 'July 2024'
        },
        {
            'name': 'Partner Pro Module 5: End-to-End Billing with Complex Formula Products',
            'url': 'https://verify.skilljar.com/c/y59hxuzfsuqq',
            'date': 'Jan 2024'
        }
    ],
    'Salesforce': [
        {
            'name': 'Salesforce Trailblazer — Billing Specialist Superbadge, 70+ Badges',
            'url': 'https://www.salesforce.com/trailblazer/jsullivanatg123',
            'date': ''
        }
    ],
    'Teaching': [
        {
            'name': 'Secondary Math Teaching License',
            'url': '',
            'date': 'Montana OPI — May 2012'
        }
    ],
    'Engineering': [
        {
            'name': 'Engineering Intern',
            'url': '',
            'date': 'Montana Department of Labor and Industry'
        }
    ]
}

# Build a new certifications HTML block
certs_html = ''
for category, certs in cert_links.items():
    for cert in certs:
        if cert['url']:
            link = f'<a href="{cert["url"]}" target="_blank" style="color: #4a6cf7; text-decoration: none; transition: color 0.3s;">{cert["name"]}</a>'
        else:
            link = cert['name']
        date_span = f' <span style="color: #999; font-size: 0.85rem;">— {cert["date"]}</span>' if cert['date'] else ''
        certs_html += f'''
                            <div style="display: flex; align-items: center; gap: 10px; padding: 12px 0; border-bottom: 1px solid #eee;">
                                <i class="fas fa-certificate" style="color: #4a6cf7; font-size: 1.1rem; min-width: 20px;"></i>
                                <div>
                                    <div style="font-weight: 500;">{link}</div>
                                    <div style="font-size: 0.85rem; color: #888;">{category}{date_span}</div>
                                </div>
                            </div>'''

# Try to find and replace the certifications section
# Look for common patterns - adjust if needed
patterns = [
    (r'(<!-- Certifications -->.*?)(<!-- /Certifications -->)', 'marker'),
    (r'(<div[^>]*class="[^"]*cert[^"]*"[^>]*>)(.*?)(</div>\s*</div>)', 'class'),
]

replaced = False

# Try to find a section with "Certification" or "cert" in it
cert_section_pattern = r'(<(?:div|section)[^>]*>)\s*(?:<[^>]*>)*\s*(?:Certification|Certificate|Certified).*?(?=<(?:div|section)[^>]*class|</(?:main|section|body)>)'

# Simple approach: insert a new certifications section or replace existing
# First check if there's already a certifications area
if 'ertification' in html or 'ertified' in html:
    # Find the section that mentions certifications
    # Look for a heading or title containing cert
    cert_heading = re.search(r'<h[23][^>]*>[^<]*[Cc]ert[^<]*</h[23]>', html)
    if cert_heading:
        # Find the parent container and replace its content
        pos = cert_heading.start()
        # Find the next closing section/div pair
        heading_match = cert_heading.group()
        new_section = f'''{heading_match}
                        <div class="certs-list">
{certs_html}
                        </div>'''
        # Replace the heading and insert certs after it
        # Find what comes after the heading until the next major section
        after_heading = html[cert_heading.end():]
        # Find the next h2/h3 or section close
        next_section = re.search(r'<h[23]|</section>', after_heading)
        if next_section:
            end_pos = cert_heading.end() + next_section.start()
            html = html[:cert_heading.start()] + new_section + html[end_pos:]
            replaced = True

if not replaced:
    # Insert before the footer or before closing main
    # Add a full certifications section
    cert_full = f'''
        <section class="certifications" style="padding: 60px 0; background-color: #f9fafb;">
            <div class="container">
                <h2 style="text-align: center; margin-bottom: 30px;">Certifications & Licenses</h2>
                <div style="max-width: 700px; margin: 0 auto; background: white; border-radius: 10px; padding: 20px 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.06);">
{certs_html}
                </div>
            </div>
        </section>
'''
    # Insert before footer
    footer_match = re.search(r'<footer', html)
    if footer_match:
        html = html[:footer_match.start()] + cert_full + html[footer_match.start():]
        replaced = True

if replaced:
    with open('index.html', 'w') as f:
        f.write(html)
    print('index.html updated with certification links!')
else:
    print('Could not find insertion point. Adding before </main>.')
    html = html.replace('</main>', cert_full + '</main>')
    with open('index.html', 'w') as f:
        f.write(html)
    print('index.html updated with certification links!')
