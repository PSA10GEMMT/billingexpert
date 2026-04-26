import re

for filename in ['index.html', 'timeline.html', 'references.html']:
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    skip = False
    for line in lines:
        if 'be_auth' in line:
            skip = True
            # Also remove the script tags around it
            # Remove the previous line if it's the opening script tag
            if new_lines and '<script>' in new_lines[-1]:
                new_lines.pop()
            # Also remove the (function() { line if present
            if new_lines and '(function()' in new_lines[-1]:
                new_lines.pop()
            continue
        if skip:
            if '</script>' in line or '})();' in line or 'window.location' in line or '}' == line.strip():
                continue
            else:
                skip = False
        new_lines.append(line)
    
    with open(filename, 'w') as f:
        f.writelines(new_lines)
    print(f'{filename} cleaned!')
