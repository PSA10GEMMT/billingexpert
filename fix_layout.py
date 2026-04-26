with open('index.html', 'r') as f:
    html = f.read()

# Add override styles right before </head>
override_css = '''
    <style>
        .about-two-col {
            display: flex !important;
            flex-direction: row !important;
            gap: 30px !important;
            margin-top: 30px !important;
            align-items: flex-start !important;
        }
        .about-two-col .col-left {
            flex: 1 !important;
            min-width: 0 !important;
        }
        .about-two-col .col-right {
            flex: 1 !important;
            min-width: 0 !important;
            display: flex !important;
            flex-direction: column !important;
            gap: 20px !important;
        }
        @media screen and (max-width: 768px) {
            .about-two-col {
                flex-direction: column !important;
            }
        }
    </style>
'''

html = html.replace('</head>', override_css + '</head>')

# Replace the about-highlights div with new two-column structure
old_div = 'style="display: flex; gap: 30px; margin-top: 30px; align-items: flex-start; flex-wrap: wrap;"'
new_div = 'class="about-two-col"'
html = html.replace(old_div, new_div)

# Replace the left column wrapper
old_left = 'style="flex: 1; min-width: 300px; background: white; border-radius: 10px; padding: 24px; box-shadow: 0 2px 10px rgba(0,0,0,0.06);"'
new_left = 'class="col-left" style="background: white; border-radius: 10px; padding: 24px; box-shadow: 0 2px 10px rgba(0,0,0,0.06);"'
html = html.replace(old_left, new_left)

# Replace the right column wrapper
old_right = 'style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 20px;"'
new_right = 'class="col-right"'
html = html.replace(old_right, new_right)

with open('index.html', 'w') as f:
    f.write(html)

print('Layout fix applied!')
