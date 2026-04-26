import re

for filename in ['index.html', 'timeline.html', 'references.html']:
    with open(filename, 'r') as f:
        html = f.read()
    
    # Remove the auth script block
    html = re.sub(r'\s*<script>\s*$$function$$$$\s*\{\s*if\s*$$sessionStorage\.getItem$$\'be_auth\'$$.*?\}$$$$$$;\s*</script>\s*', '\n', html, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(html)
    print(f'{filename} auth removed!')

print('All pages are now public!')
