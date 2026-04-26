for filename in ['index.html', 'timeline.html']:
    with open(filename, 'r') as f:
        html = f.read()
    
    if 'references.html' not in html:
        old_nav = '''<li class="nav-item">
                        <a href="timeline.html" class="nav-link">Timeline</a>
                    </li>
                </ul>'''
        new_nav = '''<li class="nav-item">
                        <a href="timeline.html" class="nav-link">Timeline</a>
                    </li>
                    <li class="nav-item">
                        <a href="references.html" class="nav-link">References</a>
                    </li>
                </ul>'''
        html = html.replace(old_nav, new_nav)
        
        with open(filename, 'w') as f:
            f.write(html)
        print(f'{filename} nav updated!')
    else:
        print(f'{filename} already has references link')
