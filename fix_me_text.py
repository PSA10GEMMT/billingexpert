with open('index.html', 'r') as f:
    html = f.read()

old_text = "With a decade of experience across the full quote-to-cash lifecycle, I bring deep fluency in how billing, revenue, and payment systems interconnect. From initial quoting and order management through invoicing, collections, and revenue recognition — understanding the complete monetization ecosystem is what allows me to architect solutions that truly fit."

new_text = "Over the past decade, I've worked across the full quote-to-cash lifecycle and developed a deep understanding of how billing, revenue, and payment systems connect. From quoting and order management through invoicing, collections, and revenue recognition — this end-to-end fluency in the monetization ecosystem is what allows me to architect solutions that truly fit."

html = html.replace(old_text, new_text)

with open('index.html', 'w') as f:
    f.write(html)
print('Monetization text updated!')
