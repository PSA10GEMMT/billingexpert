for filename in ['index.html', 'timeline.html', 'references.html']:
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        # Skip standalone <script> followed by </head> (empty broken script block)
        if '<script>' in lines[i].strip() and lines[i].strip() == '<script>':
            # Check if next non-empty line is </head>
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and '</head>' in lines[j]:
                i = j  # skip to the </head> line, which we keep
                continue
        new_lines.append(lines[i])
        i += 1
    
    with open(filename, 'w') as f:
        f.writelines(new_lines)
    print(f'{filename} fixed!')
