import os

css_path = r'c:\Users\cokre\OneDrive\Desktop\DigambaraIndustriesWebsite\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Midnight Blue to Dusty Blue Gradient
# Standard Hex values for these:
# Midnight Blue: #191970
# Dusty Blue: #6CA0DC or similar desaturated light/mid blue. Let's use #4A7A8C or #5E7D9A or #3B5998. The user's other teal/navy colors are #0a192f etc. Let's use exactly MIDNIGHT BLUE (#191970) and DUSTY BLUE (#62829e).
navy_dusty_gradient = "linear-gradient(135deg, #191970 0%, #62829e 100%)"

# 1. Update .about-header
about_old = """.about-header {
    background: #000000;
    padding: 70px 20px;
    border-radius: 14px;
    margin-bottom: 60px;
    color: white;
}"""
about_new = f""".about-header {{
    background: {navy_dusty_gradient};
    padding: 70px 20px;
    border-radius: 14px;
    margin-bottom: 60px;
    color: white;
}}"""
if about_old in css:
    css = css.replace(about_old, about_new)

# 2. Update .contact-header
# Contact header uses an image background currently: background: url('../images/blue.png') center/cover fixed no-repeat;
# It has an overlay overlay: rgba(0,0,0,0.7)
# Let's replace the image background with the gradient
contact_old = """.contact-header {
    position: relative;
    background: url('../images/blue.png') center/cover fixed no-repeat;
    padding: 120px 20px;
    color: white;
    overflow: hidden;
}"""
contact_new = f""".contact-header {{
    position: relative;
    background: {navy_dusty_gradient};
    padding: 120px 20px;
    color: white;
    overflow: hidden;
}}"""
if contact_old in css:
    css = css.replace(contact_old, contact_new)

# Remove overlay transparency so gradient is visible
overlay_old = """.contact-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
}"""
overlay_new = """.contact-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: transparent;
}"""
if overlay_old in css:
    css = css.replace(overlay_old, overlay_new)


# 3. Update .products-hero
products_old = """.products-hero {
    position: relative;
    background: url('../images/hero-bg.jpg') center/cover no-repeat;
    padding: 120px 20px;
    color: white;
}"""
products_new = f""".products-hero {{
    position: relative;
    background: {navy_dusty_gradient};
    padding: 120px 20px;
    color: white;
}}"""
if products_old in css:
    css = css.replace(products_old, products_new)

p_overlay_old = """.products-hero .overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.7);
}"""
p_overlay_new = """.products-hero .overlay {
    position: absolute;
    inset: 0;
    background: transparent;
}"""
if p_overlay_old in css:
    css = css.replace(p_overlay_old, p_overlay_new)


# 4. Update .cert-header
cert_old = """.cert-header {
    background: url('../images/hero-bg.jpg') center/cover no-repeat;
    position: relative;
    padding: 100px 20px;
    color: white;
    margin-bottom: 50px;
}"""
cert_new = f""".cert-header {{
    background: {navy_dusty_gradient};
    position: relative;
    padding: 100px 20px;
    color: white;
    margin-bottom: 50px;
}}"""
if cert_old in css:
    css = css.replace(cert_old, cert_new)

c_overlay_old = """.cert-header .overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.7);
}"""
c_overlay_new = """.cert-header .overlay {
    position: absolute;
    inset: 0;
    background: transparent;
}"""
if c_overlay_old in css:
    css = css.replace(c_overlay_old, c_overlay_new)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Headers updated to midnight blue and dusty blue gradient.")
