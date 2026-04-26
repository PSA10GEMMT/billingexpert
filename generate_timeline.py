import csv

COLORS = ['#2c3e6b', '#7a6548', '#6b8f71', '#c17c60', '#7b6b8d', '#5a8a8f', '#b07aa1', '#6c7ea0']
CURRENT_YEAR = 2026
PX_PER_YEAR = 40

def main():
    items = []
    with open('timeline_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)

    milestones = []
    details = []

    for item in items:
        t = item['type'].strip()
        if t == 'milestone':
            start = int(item['start_year'].strip())
            end_str = item['end_year'].strip()
            if end_str == '' or end_str.lower() == 'present':
                end = CURRENT_YEAR
            else:
                end = int(end_str)
            item['_start'] = start
            item['_end'] = end
            item['_details'] = []
            milestones.append(item)
        elif t == 'detail':
            year = int(item['start_year'].strip())
            item['_year'] = year
            details.append(item)

    milestones.sort(key=lambda x: (-x['_end'], -x['_start']))

    for i, m in enumerate(milestones):
        m['_color'] = COLORS[i % len(COLORS)]

    for d in details:
        for m in milestones:
            if m['_start'] <= d['_year'] <= m['_end']:
                m['_details'].append(d)
                d['_color'] = m['_color']
                break

    for m in milestones:
        m['_details'].sort(key=lambda x: -x['_year'])

    sections_html = build_sections(milestones)
    html = get_template().replace('%%SECTIONS%%', sections_html)

    with open('timeline.html', 'w') as f:
        f.write(html)
    print('timeline.html generated successfully!')


def build_sections(milestones):
    sections = ''
    for i, m in enumerate(milestones):
        color = m['_color']
        duration = max(m['_end'] - m['_start'], 1)

        if m['_start'] == m['_end']:
            date_label = str(m['_start'])
            end_label = str(m['_end'])
        else:
            end_label = 'Present' if m['_end'] == CURRENT_YEAR else str(m['_end'])
            date_label = str(m['_start']) + ' - ' + end_label

        tags = [t.strip() for t in m['tags'].strip().split('|') if t.strip()]
        tags_html = ''
        for tag in tags:
            tags_html += '<span class="tag" style="background-color: ' + color + '12; color: ' + color + '; border: 1px solid ' + color + '30;">' + tag + '</span>'
        if tags_html:
            tags_html = '<div class="tags">' + tags_html + '</div>'

        dots_html = ''
        for j, d in enumerate(m['_details']):
            d_tags = [t.strip() for t in d['tags'].strip().split('|') if t.strip()]
            d_tags_html = ''
            for tag in d_tags:
                d_tags_html += '<span class="tag" style="background-color: ' + color + '12; color: ' + color + '; border: 1px solid ' + color + '30;">' + tag + '</span>'
            if d_tags_html:
                d_tags_html = '<div class="tags">' + d_tags_html + '</div>'

            if j > 0:
                gap = max((m['_details'][j-1]['_year'] - d['_year']) * PX_PER_YEAR, 15)
            else:
                gap = max((m['_end'] - d['_year']) * PX_PER_YEAR, 15)

            if j == len(m['_details']) - 1:
                bottom_gap = max((d['_year'] - m['_start']) * PX_PER_YEAR, 15)
            else:
                bottom_gap = 0

            dots_html += '<div class="detail-dot-row" style="margin-top: ' + str(gap) + 'px; margin-bottom: ' + str(bottom_gap) + 'px;">'
            dots_html += '<div class="dot" style="background-color: ' + color + ';"></div>'
            dots_html += '<div class="connector-line" style="background-color: ' + color + ';"></div>'
            dots_html += '<div class="detail-card">'
            dots_html += '<div class="detail-card-header">'
            dots_html += '<span class="detail-year" style="background-color: ' + color + ';">' + str(d['_year']) + '</span>'
            dots_html += '<h4>' + d['title'].strip() + '</h4>'
            dots_html += '</div>'
            dots_html += '<p class="detail-subtitle">' + d['subtitle'].strip() + '</p>'
            dots_html += '<div class="detail-expanded active">'
            dots_html += '<p>' + d['description'].strip() + '</p>'
            dots_html += '<p class="detail-full">' + d['details'].strip() + '</p>'
            dots_html += d_tags_html
            dots_html += '</div>'
            dots_html += '</div>'
            dots_html += '</div>'

        if not m['_details']:
            bottom_pad = max(duration * PX_PER_YEAR - 80, 20)
        else:
            bottom_pad = 0

        sections += '<div class="milestone-section">'
        sections += '<div class="ms-left">'
        sections += '<div class="milestone-header" style="border-right: 3px solid ' + color + ';">'
        sections += '<span class="milestone-date" style="background-color: ' + color + ';">' + date_label + '</span>'
        sections += '<h3 class="milestone-title">' + m['title'].strip() + '</h3>'
        sections += '<p class="milestone-subtitle">' + m['subtitle'].strip() + '</p>'
        sections += '<p class="milestone-desc">' + m['description'].strip() + '</p>'
        sections += '<div class="milestone-expanded">'
        sections += '<p>' + m['details'].strip() + '</p>'
        sections += tags_html
        sections += '</div>'
        sections += '</div>'
        sections += '</div>'
        sections += '<div class="ms-center">'
        sections += '<div class="bar-year top" style="color: ' + color + ';">' + end_label + '</div>'
        sections += '<div class="milestone-bar" style="background: linear-gradient(180deg, ' + color + ', ' + color + '88);"></div>'
        sections += '<div class="bar-year bottom" style="color: ' + color + ';">' + str(m['_start']) + '</div>'
        sections += '</div>'
        sections += '<div class="ms-right">'
        sections += '<div class="details-container" style="padding-bottom: ' + str(bottom_pad) + 'px;">'
        sections += dots_html
        sections += '</div>'
        sections += '</div>'
        sections += '</div>'

    return sections


def get_template():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jace Sullivan - My Journey</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
        .timeline-page {
            padding: 120px 0 80px;
            background-color: #faf9f7;
            min-height: 100vh;
        }
        .timeline-page h1 {
            text-align: center;
            margin-bottom: 8px;
            font-size: 2.5rem;
            font-family: 'Playfair Display', Georgia, serif;
            color: #1a1a2e;
        }
        .timeline-intro {
            text-align: center;
            color: #7a6548;
            font-family: 'Playfair Display', Georgia, serif;
            font-style: italic;
            font-size: 1.1rem;
            margin-bottom: 15px;
        }
        .timeline-divider {
            width: 50px;
            height: 2px;
            background: linear-gradient(90deg, #2c3e6b, #7a6548);
            margin: 0 auto 50px;
        }
        .click-hint {
            text-align: center;
            color: #6a6a6a;
            font-size: 0.88rem;
            margin-bottom: 40px;
            letter-spacing: 0.5px;
        }
        .click-hint i {
            color: #7a6548;
        }
        .timeline-container {
            position: relative;
            max-width: 1100px;
            margin: 0 auto;
        }
        .milestone-section {
            display: flex;
            align-items: stretch;
            margin-bottom: 40px;
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.7s ease, transform 0.7s ease;
        }
        .milestone-section.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .ms-left {
            flex: 1;
            display: flex;
            align-items: flex-start;
            padding-right: 25px;
        }
        .ms-center {
            position: relative;
            width: 60px;
            min-width: 60px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .ms-right {
            flex: 1;
            padding-left: 25px;
        }
        .milestone-bar {
            flex: 1;
            width: 8px;
            border-radius: 4px;
            transition: box-shadow 0.4s ease;
        }
        .milestone-section:hover .milestone-bar {
            box-shadow: 0 0 20px rgba(0,0,0,0.08);
        }
        .bar-year {
            font-size: 0.72rem;
            font-weight: 600;
            white-space: nowrap;
            padding: 6px 0;
            letter-spacing: 0.5px;
            font-family: 'Inter', sans-serif;
        }
        .milestone-header {
            background: white;
            border-radius: 8px;
            padding: 24px 28px;
            border: 1px solid rgba(0,0,0,0.06);
            transition: all 0.4s ease;
            width: 100%;
            position: relative;
        }
        .milestone-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 8px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.08);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }
        .milestone-header:hover::before {
            opacity: 1;
        }
        .milestone-header:hover {
            transform: translateX(-4px);
        }
        .milestone-date {
            display: inline-block;
            padding: 4px 16px;
            color: white;
            border-radius: 3px;
            font-size: 0.82rem;
            font-weight: 500;
            margin-bottom: 12px;
            letter-spacing: 0.5px;
            font-family: 'Inter', sans-serif;
        }
        .milestone-title {
            font-size: 1.25rem;
            margin-bottom: 6px;
            color: #1a1a2e;
            font-family: 'Playfair Display', Georgia, serif;
        }
        .milestone-subtitle {
            color: #7a6548;
            font-style: italic;
            margin-bottom: 10px;
            font-size: 0.92rem;
            font-family: 'Playfair Display', Georgia, serif;
        }
        .milestone-desc {
            color: #4a4a4a;
            line-height: 1.7;
            font-size: 0.95rem;
        }
        .milestone-expanded {
            display: block;
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid rgba(0,0,0,0.06);
        }
        .milestone-expanded p {
            color: #3d3d3d;
            line-height: 1.7;
            font-size: 0.95rem;
        }
        .details-container {
            position: relative;
        }
        .detail-dot-row {
            display: flex;
            align-items: center;
            flex-direction: row;
        }
        .dot {
            width: 18px;
            height: 18px;
            min-width: 18px;
            min-height: 18px;
            border-radius: 50%;
            border: 3px solid #faf9f7;
            box-shadow: 0 0 0 1px rgba(0,0,0,0.08);
            z-index: 2;
            margin-left: -29px;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }
        .detail-dot-row:hover .dot {
            transform: scale(1.3);
            box-shadow: 0 0 0 2px rgba(0,0,0,0.12), 0 4px 12px rgba(0,0,0,0.15);
        }
        .connector-line {
            width: 20px;
            min-width: 20px;
            height: 2px;
            border-radius: 1px;
            opacity: 0.5;
        }
        .detail-card {
            flex: 1;
            background: white;
            border-radius: 8px;
            padding: 18px 22px;
            border: 1px solid rgba(0,0,0,0.06);
            cursor: pointer;
            transition: all 0.4s ease;
            position: relative;
        }
        .detail-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }
        .detail-card:hover::before {
            opacity: 1;
        }
        .detail-card:hover {
            transform: translateX(4px);
        }
        .detail-card-header {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }
        .detail-year {
            display: inline-block;
            padding: 2px 12px;
            color: white;
            border-radius: 3px;
            font-size: 0.78rem;
            font-weight: 500;
            letter-spacing: 0.5px;
            font-family: 'Inter', sans-serif;
        }
        .detail-card h4 {
            font-size: 1rem;
            color: #1a1a2e;
            margin: 0;
            font-family: 'Playfair Display', Georgia, serif;
            font-weight: 500;
        }
        .detail-subtitle {
            color: #7a6548;
            font-size: 0.85rem;
            font-style: italic;
            margin: 6px 0 0 0;
            font-family: 'Playfair Display', Georgia, serif;
        }
        .detail-expanded {
            display: block;
            margin-top: 14px;
            padding-top: 14px;
            border-top: 1px solid rgba(0,0,0,0.06);
        }
        .detail-expanded.active {
            display: block;
            animation: fadeIn 0.4s ease;
        }
        .detail-expanded p {
            color: #4a4a4a;
            line-height: 1.7;
            margin-bottom: 8px;
            font-size: 0.92rem;
        }
        .detail-full {
            font-size: 0.92rem;
        }
        .tags {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 12px;
        }
        .tag {
            padding: 3px 12px;
            border-radius: 3px;
            font-size: 0.75rem;
            font-weight: 500;
            letter-spacing: 0.3px;
            font-family: 'Inter', sans-serif;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @media screen and (max-width: 768px) {
            .timeline-page {
                padding: 100px 0 60px;
            }
            .timeline-page h1 {
                font-size: 1.8rem;
            }
            .milestone-section {
                flex-direction: column;
                margin-bottom: 30px;
            }
            .ms-left {
                padding-right: 0;
                margin-bottom: 0;
            }
            .ms-center {
                flex-direction: row;
                width: 100%;
                min-width: 100%;
                height: 50px;
                min-height: 50px;
                padding: 0 10px;
            }
            .milestone-bar {
                width: auto;
                height: 8px;
                flex: 1;
            }
            .bar-year {
                padding: 0 8px;
            }
            .ms-right {
                padding-left: 0;
                margin-top: 0;
            }
            .dot {
                margin-left: 0;
            }
            .detail-dot-row {
                margin-left: 10px;
            }
            .milestone-title {
                font-size: 1.1rem;
            }
        }
    </style>
    <script>
        (function() {
                window.location.href = 'login.html';
            }
        })();
    </script>
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="nav-container">
                <div class="nav-logo">
                    <a href="index.html">Jace Sullivan</a>
                </div>
                <ul class="nav-menu">
                    <li class="nav-item">
                        <a href="index.html" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="timeline.html" class="nav-link">Timeline</a>
                    </li>
                </ul>
                <div class="nav-toggle" id="mobile-menu">
                    <span class="bar"></span>
                    <span class="bar"></span>
                    <span class="bar"></span>
                </div>
            </div>
        </nav>
    </header>

    <main>
        <section class="timeline-page">
            <div class="container">
                <h1>My Professional Journey</h1>
                <p class="timeline-intro">A decade of building, teaching, and solving</p>
                <div class="timeline-divider"></div>
                
                <div class="timeline-container">
%%SECTIONS%%
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 Jace Sullivan. All rights reserved.</p>
        </div>
    </footer>

    <script>
        var navToggle = document.getElementById('mobile-menu');
        var navMenu = document.querySelector('.nav-menu');
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
        document.querySelectorAll('.nav-link').forEach(function(link) {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
            });
        });
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.milestone-section').forEach(function(section) {
            observer.observe(section);
        });
        document.querySelectorAll('.detail-card').forEach(function(card) {
            card.addEventListener('click', function() {
                var expanded = this.querySelector('.detail-expanded');
                if (expanded) {
                    expanded.classList.toggle('active');
                }
            });
        });
        window.addEventListener('scroll', function() {
            var navbar = document.querySelector('.navbar');
            if (window.scrollY > 100) {
                navbar.style.padding = '10px 0';
            } else {
                navbar.style.padding = '0';
            }
        });
    </script>
</body>
</html>"""


if __name__ == '__main__':
    main()
