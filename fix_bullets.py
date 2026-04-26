with open('index.html', 'r') as f:
    html = f.read()

# Fix Experience box - ul is self-closing, li items outside
old_exp = '''<h3>Experience</h3>
                                 <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;"></ul>
                                <li style="margin-bottom: 6px;">10+ years of implementing billing systems and leading quote to cash implementations</li>
                                <li>5 years of Coaching - Teaching - Managing </li>'''

new_exp = '''<h3>Experience</h3>
                                <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">10+ years of implementing billing systems and leading quote-to-cash implementations</li>
                                    <li>5 years of coaching, teaching, and managing</li>
                                </ul>'''

html = html.replace(old_exp, new_exp)

# Fix Strengths box - same issue
old_str = '''<h3>Strengths</h3>
                                 <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;"></ul>
                                <li style="margin-bottom: 6px;">Motivated, energetic, and lighthearted.</li>
                                <li>Lifelong team player - from coaching basketball to leading cross-functional technology teams.</li>'''

new_str = '''<h3>Strengths</h3>
                                <ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">Motivated, energetic, and lighthearted</li>
                                    <li>Lifelong team player — from coaching basketball to leading cross-functional technology teams</li>
                                </ul>'''

html = html.replace(old_str, new_str)

with open('index.html', 'w') as f:
    f.write(html)
print('Bullets fixed!')
