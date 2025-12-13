from fpdf import FPDF
import math

# --- CONFIGURATION ---
# ⚠️ IMPORTANT: Replace with your actual team member names for the filename!
TEAM_MEMBERS = "Membre 1, Membre 2, Membre 3, Membre 4, Membre 5"  # REPLACE THESE
FILENAME = "poster_Membre1_Membre2_Membre3.pdf"  # Important for the grade! Format: poster_nom1_nom2_nom3.pdf

# Colors (RGB) - Modern Professional Palette
COLOR_BG = (250, 252, 255)         # Ultra light background
COLOR_DARK = (20, 25, 40)          # Deep charcoal (Tech vibe)
COLOR_HEADER = (15, 20, 35)        # Dark charcoal header
COLOR_ACCENT1 = (59, 130, 246)     # Vibrant Blue
COLOR_ACCENT2 = (139, 92, 246)     # Rich Purple
COLOR_ACCENT3 = (249, 115, 22)     # Energetic Orange
COLOR_ACCENT4 = (34, 197, 94)      # Success Green
COLOR_ACCENT5 = (239, 68, 68)      # Alert Red
COLOR_TEXT_LIGHT = (255, 255, 255) # White text
COLOR_TEXT_DARK = (30, 30, 30)     # Dark text
COLOR_SUBTLE = (240, 245, 250)     # Subtle background

class PosterPDF(FPDF):
    def header(self):
        pass

    def draw_section_box(self, x, y, w, h, title, content, color_accent=COLOR_ACCENT1, icon="", font_size=8.5):
        """Draw a modern section box with gradient effect and rounded corners simulation."""
        # Enhanced shadow effect (multiple layers)
        for offset in [2.5, 1.5, 0.8]:
            alpha = max(0, 50 - offset * 15)
            self.set_fill_color(200 - alpha, 200 - alpha, 200 - alpha)
            self.set_draw_color(200 - alpha, 200 - alpha, 200 - alpha)
            self.rect(x + offset, y + offset, w, h, 'DF')
        
        # White background with subtle border
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(220, 220, 230)
        self.set_line_width(1.2)
        self.rect(x, y, w, h, 'DF')
        
        # Colored accent bar at top (thicker with gradient effect)
        self.set_fill_color(*color_accent)
        self.rect(x, y, w, 12, 'F')
        
        # Subtle highlight on accent bar
        self.set_fill_color(min(255, color_accent[0] + 30), 
                           min(255, color_accent[1] + 30), 
                           min(255, color_accent[2] + 30))
        self.rect(x, y, w, 3, 'F')
        
        # Icon + Title Text on accent bar
        self.set_xy(x + 5, y + 2.5)
        self.set_text_color(*COLOR_TEXT_LIGHT)
        self.set_font('Helvetica', 'B', 10.5)
        title_text = f"{icon} {title}" if icon else title
        self.cell(w - 10, 7, title_text, 0, 0, 'L')
        
        # Content Text with better spacing
        self.set_xy(x + 5, y + 15)
        self.set_text_color(*COLOR_TEXT_DARK)
        self.set_font('Helvetica', '', font_size)
        self.multi_cell(w - 10, 4, content, align='L')
    
    def draw_team_member_box(self, x, y, w, h, member_num, task_name, color):
        """Draw a box representing a team member and their assigned task (COMPACT)."""
        # Background
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(*color)
        self.set_line_width(1)
        self.rect(x, y, w, h, 'DF')
        
        # Colored left border
        self.set_fill_color(*color)
        self.rect(x, y, 3, h, 'F')
        
        # Member number circle (smaller)
        self.set_fill_color(*color)
        self.circle(x + 1.5, y + 3, 2.5, 'F')
        self.set_xy(x - 0.5, y + 1.5)
        self.set_text_color(*COLOR_TEXT_LIGHT)
        self.set_font('Helvetica', 'B', 6.5)
        self.cell(4, 3, str(member_num), 0, 0, 'C')
        
        # Task name (compact)
        self.set_xy(x + 5, y + 1.5)
        self.set_text_color(*COLOR_TEXT_DARK)
        self.set_font('Helvetica', 'B', 7)
        self.multi_cell(w - 7, 3, task_name, align='L')
    
    def draw_icon_box(self, x, y, size, color):
        """Draw a simple icon placeholder (circle)"""
        self.set_fill_color(*color)
        self.set_draw_color(*color)
        self.circle(x, y, size, 'F')
    
    def draw_pentagon_diagram(self, cx, cy, radius, labels, colors):
        """Draw an enhanced pentagon with 5 sections, gradients, and modern styling."""
        # Outer glow effect (subtle)
        self.set_fill_color(245, 248, 255)
        self.set_draw_color(230, 235, 245)
        self.set_line_width(0.5)
        
        # Calculate pentagon points
        points = []
        for i in range(5):
            angle = (i * 72 - 90) * math.pi / 180  # Start from top
            x = cx + (radius + 2) * math.cos(angle)
            y = cy + (radius + 2) * math.sin(angle)
            points.append((x, y))
        self.polygon(points, 'DF')
        
        # Main pentagon with gradient effect
        points = []
        for i in range(5):
            angle = (i * 72 - 90) * math.pi / 180
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            points.append((x, y))
        
        # Draw filled pentagon with light background
        self.set_fill_color(250, 252, 255)
        self.set_draw_color(200, 210, 230)
        self.set_line_width(1.5)
        self.polygon(points, 'DF')
        
        # Draw 5 colored segments with thicker lines
        for i in range(5):
            angle_start = (i * 72 - 90) * math.pi / 180
            
            # Draw segment line from center to edge
            x_end = cx + radius * math.cos(angle_start)
            y_end = cy + radius * math.sin(angle_start)
            self.set_draw_color(*colors[i])
            self.set_line_width(3)
            self.line(cx, cy, x_end, y_end)
            
            # Draw small circle at vertex
            self.set_fill_color(*colors[i])
            self.circle(x_end, y_end, 2.5, 'F')
        
        # Center circle
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(180, 190, 210)
        self.set_line_width(1.5)
        self.circle(cx, cy, 8, 'DF')
        
        # Center text
        self.set_xy(cx - 5, cy - 2.5)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(*COLOR_DARK)
        self.cell(10, 5, "CORE", 0, 0, 'C')
        
        # Place labels around pentagon with better styling (COMPACT)
        for i, label in enumerate(labels):
            angle = (i * 72 - 90) * math.pi / 180
            label_dist = radius + 15
            x_label = cx + label_dist * math.cos(angle)
            y_label = cy + label_dist * math.sin(angle)
            
            # Background box for label (smaller)
            self.set_fill_color(*colors[i])
            self.set_draw_color(*colors[i])
            self.set_line_width(0.5)
            label_w = 24
            label_h = 5
            self.rect(x_label - label_w/2, y_label - label_h/2, label_w, label_h, 'DF')
            
            # Label text (smaller)
            self.set_xy(x_label - label_w/2, y_label - 2)
            self.set_font('Helvetica', 'B', 6.5)
            self.set_text_color(*COLOR_TEXT_LIGHT)
            self.cell(label_w, 4, label, 0, 0, 'C')

def create_poster():
    # Setup A3 Landscape (420mm x 297mm) - ALL ON ONE PAGE
    pdf = PosterPDF(orientation='L', unit='mm', format='A3')
    pdf.add_page()
    
    # Background with subtle gradient effect
    pdf.set_fill_color(*COLOR_BG)
    pdf.rect(0, 0, 420, 297, 'F')
    
    # Subtle pattern overlay
    pdf.set_fill_color(248, 250, 252)
    for i in range(0, 420, 20):
        if i % 40 == 0:
            pdf.rect(i, 0, 20, 297, 'F')

    # ============ HEADER BANNER ============
    # Main header background with gradient effect (COMPACT)
    pdf.set_fill_color(*COLOR_HEADER)
    pdf.rect(0, 0, 420, 22, 'F')
    
    # Accent gradient line
    pdf.set_fill_color(*COLOR_ACCENT1)
    pdf.rect(0, 22, 420, 2, 'F')
    
    # Main Title (compact)
    pdf.set_xy(8, 3)
    pdf.set_text_color(*COLOR_TEXT_LIGHT)
    pdf.set_font('Helvetica', 'B', 18)
    pdf.cell(280, 7, "ANTHROPIC : ANALYSE STRATEGIQUE D'UNE ORGANISATION", 0, 1)
    
    # Subtitle
    pdf.set_xy(8, 11)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_text_color(220, 225, 240)
    pdf.cell(280, 4, "Methodologie de recherche et etat d'avancement du projet (SAE)", 0, 1)
    
    # Team Names (Right aligned)
    pdf.set_xy(300, 6)
    pdf.set_font('Helvetica', '', 7)
    pdf.set_text_color(200, 210, 230)
    team_text = f"Equipe: {TEAM_MEMBERS}"
    pdf.cell(110, 4, team_text, 0, 1, 'R')

    # ============ COLUMN LAYOUT ============
    y_top = 26
    
    # -------- COLUMN 1: CONTEXT & METHODOLOGY (Left 25%) --------
    x1 = 5
    w1 = 98
    
    # BOX A: The Subject (COMPACT)
    text_subject = (
        "ORGANISATION CIBLE\n\n"
        "Anthropic - Entreprise d'IA\n"
        "San Francisco, USA\n\n"
        "Pourquoi ce choix ?\n"
        "Cas d'etude ideal:\n"
        "- Croissance rapide IA\n"
        "- Enjeux ethiques\n"
        "- Impact environnemental\n"
        "- Structure moderne"
    )
    pdf.draw_section_box(x1, y_top, w1, 45, "LE SUJET", text_subject, COLOR_ACCENT1, "[*]", 7)
    
    # BOX B: Team Organization & Methodology (COMPACT)
    text_method = (
        "ORGANISATION EQUIPE\n\n"
        "5 etudiants = 5 experts\n"
        "Travail parallele\n\n"
        "OUTILS:\n"
        "- Trello (Kanban)\n"
        "- Discord (Communication)\n\n"
        "APPROCHE:\n"
        "1. Repartition 5 axes\n"
        "2. Recherche individuelle\n"
        "3. Partage resultats\n"
        "4. Synthese collective"
    )
    pdf.draw_section_box(x1, y_top + 49, w1, 50, "METHODE", text_method, COLOR_ACCENT2, "[*]", 7)
    
    # BOX C: Current Status (COMPACT)
    text_status = (
        "ETAT D'AVANCEMENT\n\n"
        "[OK] Phase 1: Setup\n"
        "   Trello + Discord\n\n"
        "[>>] Phase 2: EN COURS\n"
        "   Recherche individuelle\n\n"
        "[..] Phase 3: A venir\n"
        "   Partage resultats\n\n"
        "[..] Phase 4: Finalisation\n"
        "   Presentation"
    )
    pdf.draw_section_box(x1, y_top + 103, w1, 50, "ROADMAP", text_status, COLOR_ACCENT3, "[*]", 7)

    # -------- COLUMN 2: THE CORE ANALYSIS (Center 50%) --------
    x2 = 107
    w2 = 200
    
    # Title with enhanced background (COMPACT)
    pdf.set_fill_color(245, 248, 252)
    pdf.rect(x2, y_top, w2, 9, 'F')
    pdf.set_draw_color(220, 230, 240)
    pdf.set_line_width(1)
    pdf.rect(x2, y_top, w2, 9, 'D')
    
    pdf.set_xy(x2 + 3, y_top + 2)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(*COLOR_DARK)
    pdf.cell(w2 - 6, 5, "LES 5 AXES D'ANALYSE - REPARTITION PAR EQUIPE", 0, 1, 'C')
    
    # Team member assignments visualization (COMPACT)
    y_team_start = y_top + 12
    team_tasks = [
        ("1. HISTOIRE", "Histoire organisation\n(Passe et present)", COLOR_ACCENT1),
        ("2. MACRO-ENVIRONNEMENT", "Analyse PESTEL\n(Environnement externe)", COLOR_ACCENT2),
        ("3. ANALYSE INTERNE", "Analyse SWOT\n(Forces/Faiblesses)", COLOR_ACCENT3),
        ("4. ANALYSE EXTERNE", "Analyse PORTER\n(Concurrence)", COLOR_ACCENT4),
        ("5. FINALITES & STRUCTURE", "Metiers, structure\net strategies", COLOR_ACCENT5)
    ]
    
    for i, (task_label, task_desc, color) in enumerate(team_tasks):
        y_pos = y_team_start + i * 28
        pdf.draw_team_member_box(x2 + 3, y_pos, w2 - 6, 26, i+1, f"{task_label}\n{task_desc}", color)
    
    # Pentagon diagram (smaller, compact)
    center_x = x2 + w2 / 2
    center_y = y_top + 155
    radius = 18
    
    # 5 Analysis points with vibrant colors
    labels = ["HISTOIRE", "PESTEL", "SWOT", "PORTER", "STRATEGIE"]
    colors = [COLOR_ACCENT1, COLOR_ACCENT2, COLOR_ACCENT3, COLOR_ACCENT4, COLOR_ACCENT5]
    
    pdf.draw_pentagon_diagram(center_x, center_y, radius, labels, colors)
    
    # Compact content boxes around pentagon
    boxes_content = [
        ("1. HISTOIRE", "- Origine\n- Evolution\n- Position"),
        ("2. PESTEL", "- Politique\n- Economique\n- Social\n- Techno\n- Environ.\n- Legal"),
        ("3. SWOT", "- Forces\n- Faiblesses\n- Opportunites\n- Menaces"),
        ("4. PORTER", "- Concurrence\n- Nouveaux entrants\n- Substituts\n- Fournisseurs\n- Clients"),
        ("5. STRUCTURE", "- Finalites\n- Metiers\n- Organisation\n- Strategies")
    ]
    
    # Compact positions around pentagon
    positions = [
        (center_x - 35, center_y - 35, 32, 25),  # Top
        (center_x + 28, center_y - 14, 32, 25),  # Top-Right
        (center_x + 20, center_y + 22, 32, 25),  # Bottom-Right
        (center_x - 52, center_y + 22, 32, 25),  # Bottom-Left
        (center_x - 60, center_y - 14, 32, 25)   # Top-Left
    ]
    
    for i, (title, content) in enumerate(boxes_content):
        x, y, w, h = positions[i]
        # Background box
        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(colors[i][0], colors[i][1], colors[i][2])
        pdf.set_line_width(1)
        pdf.rect(x, y, w, h, 'DF')
        
        # Colored top bar
        pdf.set_fill_color(*colors[i])
        pdf.rect(x, y, w, 5, 'F')
        
        # Title
        pdf.set_xy(x + 1, y + 0.5)
        pdf.set_font('Helvetica', 'B', 6.5)
        pdf.set_text_color(*COLOR_TEXT_LIGHT)
        pdf.multi_cell(w - 2, 3, title, align='C')
        
        # Content
        pdf.set_xy(x + 2, y + 6)
        pdf.set_font('Helvetica', '', 6)
        pdf.set_text_color(25, 25, 25)
        pdf.multi_cell(w - 4, 2.8, content, align='L')

    # -------- COLUMN 3: WORKFLOW & OBJECTIVES (Right 25%) --------
    x3 = 311
    w3 = 103
    
    # BOX A: Workflow Process (COMPACT)
    text_workflow = (
        "PROCESSUS DE TRAVAIL\n\n"
        "ETAPE 1: Repartition\n"
        "1 membre = 1 axe\n\n"
        "ETAPE 2: Recherche\n"
        "Travail parallele\n\n"
        "ETAPE 3: Partage\n"
        "Via Trello/Discord\n\n"
        "ETAPE 4: Synthese\n"
        "Presentation collective"
    )
    pdf.draw_section_box(x3, y_top, w3, 50, "WORKFLOW", text_workflow, COLOR_ACCENT2, "[*]", 7)
    
    # BOX B: Tools & Collaboration (COMPACT)
    text_tools = (
        "OUTILS COLLABORATIFS\n\n"
        "TRELLO:\n"
        "- Kanban\n"
        "- Suivi taches\n"
        "- Partage docs\n\n"
        "DISCORD:\n"
        "- Communication\n"
        "- Partage notes\n"
        "- Coordination"
    )
    pdf.draw_section_box(x3, y_top + 54, w3, 50, "OUTILS", text_tools, COLOR_ACCENT1, "[*]", 7)
    
    # BOX C: Objectives & Expected Results (COMPACT)
    text_objectives = (
        "OBJECTIFS PROJET\n\n"
        "COMPRENDRE:\n"
        "- Fonctionnement\n"
        "- Environnement\n"
        "- Strategies\n\n"
        "PRODUIRE:\n"
        "- Analyse complete\n"
        "- Synthese\n"
        "- Presentation\n"
        "- Poster"
    )
    pdf.draw_section_box(x3, y_top + 108, w3, 45, "OBJECTIFS", text_objectives, COLOR_ACCENT4, "[*]", 7)

    # ============ FOOTER ============
    # Footer background (COMPACT)
    pdf.set_fill_color(245, 247, 250)
    pdf.rect(0, 285, 420, 12, 'F')
    pdf.set_draw_color(220, 225, 235)
    pdf.set_line_width(0.5)
    pdf.line(0, 285, 420, 285)
    
    # Footer text - left side
    pdf.set_xy(5, 288)
    pdf.set_font('Helvetica', 'I', 6.5)
    pdf.set_text_color(120, 130, 150)
    pdf.cell(200, 3.5, 
             "SAE - BUT1 Informatique | AMU Arles | 2024-2025", 
             0, 0, 'L')
    
    # Footer text - center
    pdf.set_xy(210, 288)
    pdf.cell(200, 3.5, 
             "Methodologie de recherche documentaire et analyse strategique", 
             0, 0, 'C')
    
    # Footer text - right side (filename reminder)
    pdf.set_xy(300, 291)
    pdf.set_font('Helvetica', '', 6)
    pdf.set_text_color(150, 160, 180)
    pdf.cell(115, 3.5, 
             f"Fichier: {FILENAME}", 
             0, 0, 'R')

    # Output
    pdf.output(FILENAME)
    print(f"\n{'='*70}")
    print(f"✅ SUCCESS! Poster generated: {FILENAME}")
    print(f"{'='*70}")
    print(f"📄 Layout: 3-Column (25%-50%-25%) | Size: A3 Landscape | Pages: 1")
    print(f"🎨 Features: Enhanced colors, shadows, team visualization, modern design")
    print(f"📊 Content: Team organization, methodology, 5 analysis axes, workflow")
    print(f"\n⚠️  IMPORTANT: Make sure to update TEAM_MEMBERS and FILENAME with actual names!")
    print(f"   Format: poster_nom1_nom2_nom3.pdf (required for grading)")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    create_poster()