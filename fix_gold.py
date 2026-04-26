# Darken the gold accent color across all files
old_gold = '#a0896e'
new_gold = '#7a6548'

for filename in ['styles.css', 'index.html', 'timeline.html', 'generate_timeline.py']:
    with open(filename, 'r') as f:
        content = f.read()
    content = content.replace(old_gold, new_gold)
    with open(filename, 'w') as f:
        f.write(content)
    print(f'{filename} updated!')

print('Gold accent darkened from #a0896e to #7a6548')
