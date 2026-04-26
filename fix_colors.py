# Fix styles.css
with open('styles.css', 'r') as f:
    css = f.read()

# Darken body text colors
css = css.replace('color: #777;', 'color: #4a4a4a;')
css = css.replace('color: #666;', 'color: #3d3d3d;')
css = css.replace('color: #555;', 'color: #3d3d3d;')
css = css.replace('color: #888;', 'color: #5a5a5a;')
css = css.replace('color: #999;', 'color: #6a6a6a;')
css = css.replace('color: #aaa;', 'color: #6a6a6a;')

with open('styles.css', 'w') as f:
    f.write(css)
print('styles.css text colors darkened!')

# Fix timeline.html
with open('timeline.html', 'r') as f:
    html = f.read()

html = html.replace('color: #777;', 'color: #4a4a4a;')
html = html.replace('color: #666;', 'color: #3d3d3d;')
html = html.replace('color: #555;', 'color: #3d3d3d;')
html = html.replace('color: #888;', 'color: #5a5a5a;')
html = html.replace('color: #999;', 'color: #6a6a6a;')
html = html.replace('color: #aaa;', 'color: #6a6a6a;')

with open('timeline.html', 'w') as f:
    f.write(html)
print('timeline.html text colors darkened!')

# Fix inline styles in index.html
with open('index.html', 'r') as f:
    idx = f.read()

idx = idx.replace('color: #777;', 'color: #4a4a4a;')
idx = idx.replace('color: #666;', 'color: #3d3d3d;')
idx = idx.replace('color: #555;', 'color: #3d3d3d;')
idx = idx.replace('color: #888;', 'color: #5a5a5a;')
idx = idx.replace('color: #999;', 'color: #6a6a6a;')
idx = idx.replace('color: #aaa;', 'color: #6a6a6a;')

with open('index.html', 'w') as f:
    f.write(idx)
print('index.html text colors darkened!')
