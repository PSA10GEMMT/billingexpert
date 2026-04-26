with open('timeline.html', 'r') as f:
    html = f.read()

html = html.replace('<p class="click-hint"><i class="fas fa-hand-pointer"></i> Click any detail to expand</p>', '')

with open('timeline.html', 'w') as f:
    f.write(html)
print('Click hint removed!')
