with open('index.html', 'r') as f:
    html = f.read()

me_section = '''
        <!-- Monetization Ecosystem Section -->
        <section class="monetization" id="monetization" style="padding: 100px 0; background: white;">
            <div class="container">
                <h2>The Monetization Ecosystem</h2>
                <p style="color: #4a4a4a; font-size: 1.05rem; line-height: 1.8; max-width: 750px; margin-top: 25px; margin-bottom: 50px;">With a decade of experience across the full quote-to-cash lifecycle, I bring deep fluency in how billing, revenue, and payment systems interconnect. From initial quoting and order management through invoicing, collections, and revenue recognition — understanding the complete monetization ecosystem is what allows me to architect solutions that truly fit.</p>
                <div style="display: flex; flex-direction: column; align-items: center; gap: 40px; max-width: 900px; margin: 0 auto;">
                    <div style="width: 100%; background: #faf9f7; border-radius: 8px; padding: 20px; border: 1px solid rgba(0,0,0,0.06); transition: all 0.4s ease;" onmouseover="this.style.boxShadow='0 12px 35px rgba(0,0,0,0.06)'; this.style.transform='translateY(-4px)';" onmouseout="this.style.boxShadow='none'; this.style.transform='translateY(0)';">
                        <img src="ME1.png" alt="Monetization Ecosystem Overview" style="width: 100%; height: auto; border-radius: 4px; display: block;">
                    </div>
                    <div style="width: 100%; background: #faf9f7; border-radius: 8px; padding: 20px; border: 1px solid rgba(0,0,0,0.06); transition: all 0.4s ease;" onmouseover="this.style.boxShadow='0 12px 35px rgba(0,0,0,0.06)'; this.style.transform='translateY(-4px)';" onmouseout="this.style.boxShadow='none'; this.style.transform='translateY(0)';">
                        <img src="ME2.png" alt="Quote to Cash Process" style="width: 100%; height: auto; border-radius: 4px; display: block;">
                    </div>
                </div>
                <p style="color: #6a6a6a; font-size: 0.92rem; font-style: italic; text-align: center; margin-top: 30px; font-family: 'Playfair Display', Georgia, serif;">More detailed commentary coming soon.</p>
            </div>
        </section>
'''

# Insert between About and Skills
html = html.replace(
    '<!-- Skills Section -->',
    me_section + '\n        <!-- Skills Section -->'
)

# If that didn't match, try finding the skills section by its tag
if '<!-- Monetization Ecosystem Section -->' not in html:
    html = html.replace(
        '<section class="skills"',
        me_section + '\n        <section class="skills"'
    )

with open('index.html', 'w') as f:
    f.write(html)
print('Monetization Ecosystem section added!')
