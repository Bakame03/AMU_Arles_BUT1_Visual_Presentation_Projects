from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# --- 1. Setup the PDF Document ---
pdf_filename = "BUT_Informatique_Arles_Flyer.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4,
                        rightMargin=1.5*cm, leftMargin=1.5*cm,
                        topMargin=1.5*cm, bottomMargin=1.5*cm)

# AMU Official Colors
AMU_BLUE = colors.HexColor("#003d7c")
AMU_YELLOW = colors.HexColor("#ffcc00")

# Styles
styles = getSampleStyleSheet()

# Custom Styles
style_title = ParagraphStyle(
    'CustomTitle',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=28,
    textColor=colors.white,
    alignment=TA_CENTER,
    spaceAfter=10,
    leading=32
)

style_subtitle = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=16,
    textColor=AMU_YELLOW,
    alignment=TA_CENTER,
    spaceAfter=30
)

style_h2 = ParagraphStyle(
    'CustomH2',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=16,
    textColor=AMU_BLUE,
    spaceBefore=15,
    spaceAfter=10,
    borderWidth=0
)

style_body = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    textColor=colors.black,
    leading=16,
    alignment=TA_LEFT
)

style_dates_header = ParagraphStyle(
    'DatesHeader',
    parent=styles['Heading3'],
    fontName='Helvetica-Bold',
    fontSize=14,
    textColor=colors.white,
    alignment=TA_CENTER,
    spaceAfter=6
)

style_dates_body = ParagraphStyle(
    'DatesBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    textColor=colors.white,
    alignment=TA_CENTER,
    leading=14
)

# --- 2. Function to Draw Backgrounds (Header/Footer) ---
def draw_header_footer(canvas, doc):
    # Header Blue Box
    canvas.saveState()
    canvas.setFillColor(AMU_BLUE)
    canvas.rect(0, A4[1] - 4.5*cm, A4[0], 5*cm, fill=1, stroke=0)
    
    # Footer Blue Box
    canvas.setFillColor(AMU_BLUE)
    canvas.rect(0, 0, A4[0], 2.5*cm, fill=1, stroke=0)
    
    # Decorative Yellow Line under Header
    canvas.setFillColor(AMU_YELLOW)
    canvas.rect(0, A4[1] - 4.6*cm, A4[0], 0.15*cm, fill=1, stroke=0)
    
    # Footer Text Overlay
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawCentredString(A4[0]/2, 1.8*cm, "CONTACTEZ-NOUS : iut.univ-amu.fr")
    
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(A4[0]/2, 1.3*cm, "Rue Raoul Follereau, 13200 Arles | Tél : 04 13 55 21 00 | Email : iut-arles-scol@univ-amu.fr")
    
    canvas.setFont("Helvetica-Oblique", 8)
    canvas.drawRightString(A4[0] - 1*cm, 0.5*cm, "IUT Aix-Marseille | Ville d'Arles")
    
    canvas.restoreState()

# --- 3. Build Content Elements ---
elements = []

# Header Text (Spacers push it down into the blue box)
elements.append(Spacer(1, 0.2*cm))
elements.append(Paragraph("DEVIENS L'INFORMATICIEN<br/>DE DEMAIN", style_title))
elements.append(Paragraph("BUT INFORMATIQUE - IUT D'AIX-MARSEILLE - SITE D'ARLES", style_subtitle))
elements.append(Spacer(1, 1.5*cm))

# -- Two Column Section (Why Arles vs Program) --
why_arles_text = """
<b>Effectifs réduits & Ambiance :</b><br/>
Promo de ~60 étudiants. Un suivi personnalisé loin de l'anonymat des grands campus.<br/><br/>
<b>Spécialité Unique :</b><br/>
Coloration <b>Imagerie Numérique (2D/3D)</b> et Développement Fullstack dès la 2ème année.<br/><br/>
<b>Cadre de vie :</b><br/>
Campus moderne aux portes de la Camargue, à 5 min du centre-ville historique.
"""

program_text = """
<b>Diplôme National (Bac+3) :</b><br/>
Grade de Licence (180 ECTS). Insertion pro immédiate ou poursuite d'études (Master/Ingénieur).<br/><br/>
<b>Pédagogie par Projets :</b><br/>
Mises en situation professionnelle (SAÉ) concrètes tout au long de l'année.<br/><br/>
<b>Professionnalisation :</b><br/>
22 à 26 semaines de stage.<br/>
Alternance possible en <b>3ème année</b>.
"""

data = [
    [Paragraph("🎯 POURQUOI ARLES ?", style_h2), Paragraph("💻 LE PROGRAMME", style_h2)],
    [Paragraph(why_arles_text, style_body), Paragraph(program_text, style_body)]
]

table_style = TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ('LINEAFTER', (0,0), (0,-1), 1, colors.lightgrey), # Vertical divider line
    ('BOTTOMPADDING', (0,0), (-1,-1), 20),
])

t = Table(data, colWidths=[9*cm, 9*cm])
t.setStyle(table_style)
elements.append(t)

elements.append(Spacer(1, 1*cm))

# -- Key Dates Section (Blue Box with Yellow Border) --
date_content = [
    [Paragraph("📅 À VOS AGENDAS ! (Admission 2025/2026)", style_dates_header)],
    [Paragraph("<b>📍 SALON ARLES CAMPUS</b><br/>Mardi 2 Décembre 2025 – CCI d'Arles (Palais des Congrès)", style_dates_body)],
    [Spacer(1, 0.2*cm)],
    [Paragraph("<b>🔓 JOURNÉE PORTES OUVERTES (JPO)</b><br/>Mercredi 28 Janvier 2026 – De 14h à 20h<br/><i>Venez visiter les locaux et rencontrer les étudiants !</i>", style_dates_body)]
]

dates_table = Table(date_content, colWidths=[16*cm])
dates_style = TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), AMU_BLUE),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 15),
    ('BOTTOMPADDING', (0,0), (-1,-1), 15),
    ('BOX', (0,0), (-1,-1), 2, AMU_YELLOW), # Yellow border
])
dates_table.setStyle(dates_style)
elements.append(dates_table)

elements.append(Spacer(1, 1.5*cm))

# -- Admission Info --
admission_text = """
<b>🚀 ADMISSION VIA PARCOURSUP</b><br/>
Public : Bac Général (Maths/NSI/Sciences) & Bac Techno (STI2D).<br/>
~56 Places disponibles.
"""
elements.append(Paragraph(admission_text, style_body))

# --- 4. Generate PDF ---
doc.build(elements, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
print(f"Success! PDF generated at: {pdf_filename}")