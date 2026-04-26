with open('index.html', 'r') as f:
    html = f.read()

old_desc = 'A thoughtful and creative problem solver based in Missoula, Montana, with a decade of experience implementing billing systems for enterprise companies. Well versed in the entire monetization ecosystem and a leading expert in complex usage rating. Bringing a unique perspective shaped by a diverse background in solution architecture, engineering, project management, and education.'

new_desc = "I'm a thoughtful and creative problem solver based in Missoula, Montana, with a decade of experience implementing billing systems for enterprise companies. I'm well versed in the entire monetization ecosystem and have become a leading expert in complex usage rating. My diverse background in solution architecture, engineering, project management, and education gives me a unique perspective that I bring to every project."

html = html.replace(old_desc, new_desc)

with open('index.html', 'w') as f:
    f.write(html)
print('Hero description updated!')
