auth_script = '''
    <script>
        (function() {
            if (sessionStorage.getItem('be_auth') !== 'authenticated') {
                window.location.href = 'login.html';
            }
        })();
    </script>
'''

for filename in ['index.html', 'timeline.html', 'references.html']:
    with open(filename, 'r') as f:
        html = f.read()
    
    if 'be_auth' not in html:
        html = html.replace('</head>', auth_script + '</head>')
        with open(filename, 'w') as f:
            f.write(html)
        print(f'{filename} protected!')
    else:
        print(f'{filename} already protected')
