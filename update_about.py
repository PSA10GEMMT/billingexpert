with open('index.html', 'r') as f:
    html = f.read()

old_about_p1 = "I'm a problem-solving professional with a diverse background that bridges engineering, education, and enterprise technology. Currently working as a Solution Architect and Project Manager at ATG/Cognizant, I specialize in billing system configuration, integration, and migration for complex upstream and downstream systems."

old_about_p2 = "My journey from coaching basketball and teaching math to engineering and solution architecture has given me a rare combination of technical expertise and interpersonal skills. I've been a member of a team my whole life — as a player, coach, teacher, and now as a technology leader. The most consistent feedback I receive is how easy I am to work with."

new_about_p1 = "My path to solution architecture wasn't a straight line — and that's what makes it valuable. I started in engineering and education, coaching basketball and teaching math, before transitioning into enterprise technology. At ATG/Cognizant, I began as a Quality Assurance Specialist testing across CRM, CPQ, Billing, and FMS platforms, which gave me end-to-end visibility into the monetization ecosystem and the foundation to grow into Solution Architecture."

new_about_p2 = "Today I lead full billing implementations for enterprise clients across industries including financial services, telecommunications, transportation, retail, and fiber internet. I specialize in billing system configuration, integration design, and complex usage rating — translating business requirements into technical solutions that scale. I've been a member of a team my whole life — as a player, coach, teacher, and now as a technology leader. The most consistent feedback I receive is how easy I am to work with."

html = html.replace(old_about_p1, new_about_p1)
html = html.replace(old_about_p2, new_about_p2)

with open('index.html', 'w') as f:
    f.write(html)
print('About section updated!')
