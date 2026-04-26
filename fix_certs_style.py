with open('index.html', 'r') as f:
    html = f.read()

# Make all cert icons the same color - navy to match theme
html = html.replace('style="color: #4a6cf7; font-size: 1.1rem; min-width: 20px;"', 'style="color: #2c3e6b; font-size: 1.1rem; min-width: 20px;"')
html = html.replace('style="color: #22c55e; font-size: 1.1rem; min-width: 20px;"', 'style="color: #2c3e6b; font-size: 1.1rem; min-width: 20px;"')
html = html.replace('style="color: #f59e0b; font-size: 1.1rem; min-width: 20px;"', 'style="color: #2c3e6b; font-size: 1.1rem; min-width: 20px;"')

# Make hyperlinks more subtle - dark bronze instead of bright blue
html = html.replace('style="color: #4a6cf7; text-decoration: none;"', 'style="color: #2c3e6b; text-decoration: none; border-bottom: 1px solid #2c3e6b40;"')

# Also fix the trophy icon at the top of the certs card
html = html.replace('style="font-size: 2rem; color: #4a6cf7;"', 'style="font-size: 2rem; color: #2c3e6b;"')

with open('index.html', 'w') as f:
    f.write(html)
print('Cert icons and links updated!')
