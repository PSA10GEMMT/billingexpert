with open('index.html', 'r') as f:
    html = f.read()

# Experience box
old_exp = '''<h3>Experience</h3>
                                <p>10+ years across engineering, education, and technology</p>'''
new_exp = '''<h3>Experience</h3>
                                <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">10+ years implementing billing systems and leading quote-to-cash implementations</li>
                                    <li>5 years of coaching, teaching, and managing</li>
                                </ul>'''
html = html.replace(old_exp, new_exp)

# Education box
old_edu = '''<h3>Education</h3>
                                <p>M.A. Curriculum & Instruction | B.S. Industrial Engineering</p>'''
new_edu = '''<h3>Education</h3>
                                <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">M.A. Curriculum & Instruction — University of Montana</li>
                                    <li>B.S. Industrial Engineering — Montana State University</li>
                                </ul>'''
html = html.replace(old_edu, new_edu)

# Strengths box
old_str = '''<h3>Strengths</h3>
                                <p>Motivated, energetic, and lighthearted. Lifelong team player — from coaching basketball to leading cross-functional technology teams.</p>'''
new_str = '''<h3>Strengths</h3>
                                <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">Motivated, energetic, and lighthearted</li>
                                    <li style="margin-bottom: 6px;">Lifelong team player and leader</li>
                                    <li>From coaching basketball to leading cross-functional technology teams</li>
                                </ul>'''
html = html.replace(old_str, new_str)

with open('index.html', 'w') as f:
    f.write(html)
print('Boxes updated with left-aligned bullets!')
