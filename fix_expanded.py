with open('timeline.html', 'r') as f:
    html = f.read()

html = html.replace('class="detail-expanded"', 'class="detail-expanded active"')

html = html.replace(
    '''.detail-expanded {
            display: none;''',
    '''.detail-expanded {
            display: block;''')

with open('timeline.html', 'w') as f:
    f.write(html)
print('All entries expanded!')

# Also fix the generator so future rebuilds keep them expanded
with open('generate_timeline.py', 'r') as f:
    gen = f.read()

gen = gen.replace('class="detail-expanded"', 'class="detail-expanded active"')
gen = gen.replace('display: none;', 'display: block;')

with open('generate_timeline.py', 'w') as f:
    f.write(gen)
print('Generator updated too!')
