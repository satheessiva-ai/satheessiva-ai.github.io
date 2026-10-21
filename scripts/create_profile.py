from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

DIST = Path(__file__).resolve().parents[1]

# A concise profile intended to accompany the site, not a role-specific application.
font_base = Path('/usr/share/fonts/truetype/dejavu')
for alias, name in [('ProfileSans', 'DejaVuSans.ttf'), ('ProfileBold', 'DejaVuSans-Bold.ttf'), ('ProfileSerif', 'DejaVuSerif.ttf')]:
    pdfmetrics.registerFont(TTFont(alias, str(font_base / name)))
out = DIST / 'sathees-siva-leadership-profile.pdf'
c = canvas.Canvas(str(out), pagesize=(612, 792))
c.setTitle('Sathees Siva | Leadership Profile')
c.setAuthor('Sathees Siva')
c.setSubject('Operations, technology and transformation leadership')
paper, ink, muted, lime = [HexColor(v) for v in ['#f6f5ef', '#203e36', '#5e665e', '#d6dfb8']]
c.setFillColor(paper)
c.rect(0, 0, 612, 792, fill=1, stroke=0)
c.setFillColor(ink)
c.rect(0, 626, 612, 166, fill=1, stroke=0)
c.setFillColor(lime)
c.setFont('ProfileSans', 8)
c.drawString(44, 759, 'PEOPLE. PROCESS. PROGRESS.')
c.setFillColor(paper)
c.setFont('ProfileSerif', 32)
c.drawString(42, 712, 'Sathees Siva')
c.setFont('ProfileSans', 11)
c.drawString(44, 684, 'Operations, Technology & Transformation Leader')
c.setFont('ProfileSans', 8.1)
contact_prefix = 'Toronto, Canada  |  satheess@outlook.com  |  '
linkedin_label = 'linkedin.com/in/sathees-siva-80648aaa'
c.drawString(44, 654, contact_prefix + linkedin_label)
email_x = 44 + pdfmetrics.stringWidth('Toronto, Canada  |  ', 'ProfileSans', 8.1)
email_width = pdfmetrics.stringWidth('satheess@outlook.com', 'ProfileSans', 8.1)
linkedin_x = 44 + pdfmetrics.stringWidth(contact_prefix, 'ProfileSans', 8.1)
linkedin_width = pdfmetrics.stringWidth(linkedin_label, 'ProfileSans', 8.1)
assert linkedin_x + linkedin_width <= 568
c.linkURL('mailto:satheess@outlook.com', (email_x, 650, email_x + email_width, 664), relative=0)
c.linkURL('https://www.linkedin.com/in/sathees-siva-80648aaa/', (linkedin_x, 650, linkedin_x + linkedin_width, 664), relative=0)

styles = {
    'body': ParagraphStyle('body', fontName='ProfileSans', fontSize=9, leading=13.4, textColor=ink),
    'small': ParagraphStyle('small', fontName='ProfileSans', fontSize=8.2, leading=12.2, textColor=muted),
    'bold': ParagraphStyle('bold', fontName='ProfileBold', fontSize=9.2, leading=14, textColor=ink),
}
def paragraph(text, x, y, width, style='body'):
    p = Paragraph(text, styles[style])
    _, h = p.wrap(width, 750)
    p.drawOn(c, x, y - h)
    return y - h
def label(text, y):
    c.setFillColor(ink)
    c.setFont('ProfileBold', 8)
    c.drawString(44, y, text)
    c.setStrokeColor(HexColor('#d7dbcf'))
    c.line(44, y - 9, 568, y - 9)
    return y - 24

y = paragraph('I build multidisciplinary teams, strengthen delivery, and turn business needs into practical technical solutions. My experience spans technical support, Salesforce, promotion operations, AI and workflow automation.', 44, 604, 524)
y = label('SELECTED IMPACT AT POINTS / PLUSGRADE', y - 24)
for heading, body in [
    ('Team growth: 5 to 14 people', 'Established a Team Lead model and developed three employees into management roles.'),
    ('Reliable delivery: 60%+ fewer production incidents', 'Strengthened validation, monitoring and risk reviews. Quality reviews caught 100+ potential partner-facing issues annually before release.'),
    ('Practical AI: 80%+ less production time per request', 'Led AI-powered creative and content tools automating 1,000+ asset requests each year.'),
    ('Workflow automation: 360+ hours saved annually', 'Implemented integrations, including daily foreign-exchange rate updates, to remove recurring manual work.'),
]:
    y = paragraph(heading, 44, y, 524, 'bold')
    y = paragraph(body, 44, y - 2, 524, 'small') - 12

y = label('EXPERIENCE', y - 8)
y = paragraph('Director, Promotions | Points / Plusgrade | 2024 to present', 44, y, 524, 'bold')
y = paragraph('Lead web developers, product specialists and data specialists supporting 2,000+ promotions annually and over $500M in partner revenue across airlines, hotels and financial institutions.', 44, y - 4, 524, 'body')
y = paragraph('Promoted five times over a decade, progressing from Technical Support Analyst &amp; Salesforce Administrator through Product Specialist, Team Lead, Manager and Senior Manager to Director.', 44, y - 8, 524, 'small')
y = label('CAPABILITIES & EDUCATION', y - 25)
y = paragraph('People leadership and coaching; partner operations; quality and incident reduction; cross-functional delivery; AI and workflow automation; executive reporting.', 44, y, 524, 'body')
y = paragraph('Salesforce, Jira, SQL, Workato, ChatGPT, Claude, HTML, CSS and APIs.', 44, y - 7, 524, 'small')
y = paragraph('BSc, Business Administration (Business E-Commerce), DeVry University.<br/>Business E-Commerce Diploma, DeVry College of Technology.', 44, y - 8, 524, 'small')
assert y > 58, f'Profile overflow: final y={y}'
c.setStrokeColor(HexColor('#d7dbcf'))
c.line(44, 43, 568, 43)
c.setFillColor(muted)
c.setFont('ProfileSans', 7)
c.drawString(44, 29, 'Revenue figures describe partner business supported by promotion operations.')
c.drawRightString(568, 29, 'Leadership profile | October 2026')
c.showPage()
c.save()
print(f'Updated one-page leadership profile (content ends at {y:.1f}pt).')
