with open('index.html', 'r') as f:
    html = f.read()

old_edu = '''<ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">M.A. Curriculum & Instruction — University of Montana</li>
                                    <li>B.S. Industrial Engineering — Montana State University</li>
                                </ul>'''

new_edu = '''<ul style="text-align: left; list-style: disc; padding-left: 20px; margin-top: 10px;">
                                    <li style="margin-bottom: 6px;">M.A. Curriculum & Instruction — University of Montana</li>
                                    <li style="margin-bottom: 6px;">B.S. Industrial Engineering — Montana State University</li>
                                    <li>Engineering Studies — South Dakota School of Mines & Technology</li>
                                </ul>'''

html = html.replace(old_edu, new_edu)

with open('index.html', 'w') as f:
    f.write(html)
print('Education updated!')
