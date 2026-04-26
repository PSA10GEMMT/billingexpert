with open('styles.css', 'r') as f:
    css = f.read()

# Replace about-content to be column layout
css = css.replace(
'''.about-content {
    display: flex;
    gap: 50px;
    align-items: center;
}''',
'''.about-content {
    display: flex;
    flex-direction: column;
    gap: 30px;
}''')

# Replace about-highlights to be two-column row
css = css.replace(
'''.about-highlights {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
}''',
'''.about-highlights {
    display: flex;
    flex-direction: row;
    gap: 30px;
    align-items: flex-start;
    width: 100%;
}''')

# Remove flex:2 from about-text
css = css.replace(
'''.about-text {
    flex: 2;
}''',
'''.about-text {
    width: 100%;
}''')

# Add the two-column classes
new_css = '''

.about-col-left {
    flex: 1;
    min-width: 0;
}

.about-col-right {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

@media screen and (max-width: 768px) {
    .about-highlights {
        flex-direction: column !important;
    }
}
'''

css += new_css

with open('styles.css', 'w') as f:
    f.write(css)

print('styles.css updated!')

# Now update index.html structure
with open('index.html', 'r') as f:
    html = f.read()

# Remove the old about-two-col override style block if it exists
import re
html = re.sub(r'\s*<style>\s*\.about-two-col[\s\S]*?</style>\s*', '\n', html)

# Restructure the about section
# Find the about-highlights div and restructure it
# Replace the two-col div with about-highlights using proper classes
html = html.replace('class="about-two-col"', 'class="about-highlights"')
html = html.replace('class="col-left"', 'class="about-col-left"')
html = html.replace('class="col-right"', 'class="about-col-right"')

with open('index.html', 'w') as f:
    f.write(html)

print('index.html updated!')
