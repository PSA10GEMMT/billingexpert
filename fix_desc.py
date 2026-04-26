with open('index.html', 'r') as f:
    html = f.read()

old_desc = 'Technical, analytical, lifelong learner based in Missoula, Montana. With over 10 years of professional experience spanning solution architecture, engineering, project management, and education, I bring a unique problem-solving perspective to every challenge.'

new_desc = 'A thoughtful and creative problem solver based in Missoula, Montana, with a decade of experience implementing billing systems for enterprise companies. Well versed in the entire monetization ecosystem and a leading expert in complex usage rating, I bring a unique perspective shaped by a diverse background in solution architecture, engineering, project management, and education.'

html = html.replace(old_desc, new_desc)

with open('index.html', 'w') as f:
    f.write(html)

print('Description updated!')
