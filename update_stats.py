import os

css_path = r'c:\Users\cokre\OneDrive\Desktop\DigambaraIndustriesWebsite\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .stats-section background and text color
# Replace background: url('images/hero-bg.jpg') center/cover fixed no-repeat;
# Replace padding: 100px 0;
# Replace color: white;
# We want beige and white shade. Let's use a gradient from white to beige.
stats_old = """.stats-section {
    position: relative;
    background: url('images/hero-bg.jpg') center/cover fixed no-repeat;
    padding: 100px 0;
    color: white;
}"""
stats_new = """.stats-section {
    position: relative;
    background: linear-gradient(135deg, #ffffff 0%, #fdf8f5 100%);
    padding: 100px 0;
    color: #222222;
}"""
if stats_old in css:
    css = css.replace(stats_old, stats_new)

# 2. Update .stats-overlay
# currently: background: rgba(0, 0, 0, 0.7); -> we don't need a dark overlay anymore if it's beige.
# Let's just make it transparent or a very light white overlay
overlay_old = """.stats-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
}"""
overlay_new = """.stats-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.4);
}"""
if overlay_old in css:
    css = css.replace(overlay_old, overlay_new)

# 3. Handle `.stat-box h2` and `.stat-box p` text
# `.stat-box h2` is currently orange (#ff8c00), which is fine, but the user asked for "dark colored text". Let's make it Navy Blue (#0a192f) or Black. Let's use Navy Blue for numbers so they pop, and black for text. Wait, user specifically said text in black and white only earlier. So let's make it Black.
css = css.replace('.stat-box h2 {\n    font-family: \'Lora\', serif;\n    font-weight: 600;\n    font-size: 2.5rem;\n    font-weight: 700;\n    color: #ff8c00;\n}', '.stat-box h2 {\n    font-family: \'Lora\', serif;\n    font-size: 2.5rem;\n    font-weight: 700;\n    color: #000000;\n}')

# `.stat-box p` is #fff3e3. Change to black or dark grey.
css = css.replace('.stat-box p {\n    margin-top: 8px;\n    font-size: 14px;\n    color: #fff3e3;\n}', '.stat-box p {\n    margin-top: 8px;\n    font-size: 16px;\n    font-weight: 600;\n    color: #222222;\n}')

# 4. Remove .stats-section from the dark background fancy font rule
# It currently has:
# .products-hero *,
# .stats-section *,
# .cert-header *,
fancy_old = """.products-hero *,
.stats-section *,
.cert-header *,"""
fancy_new = """.products-hero *,
.cert-header *,"""
if fancy_old in css:
    css = css.replace(fancy_old, fancy_new)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Stats section updated")
