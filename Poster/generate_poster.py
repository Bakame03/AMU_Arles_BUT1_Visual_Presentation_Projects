import os
import webbrowser

# ==========================================
# POSTER CONTENT CONFIGURATION
# Edit the values below to update the poster text
# ==========================================

POSTER_DATA = {
    "title": "EMPREINTES ÉCOLOGIQUES D'UNE ORGANISATION",
    "subtitle": "SAÉ : Analyse de l'Organisation & Empreinte Numérique",
    "subject_company": "ANTHROPIC",
    "group_members": [
        "Membre 1",
        "Membre 2",
        "Membre 3",
        "Membre 4",
        "Membre 5"
    ],
    
    # Section 1: History
    "history_title": "1. Histoire",
    "history_content": """
    <p><strong>Fondation :</strong> Créée en 2021 par Dario et Daniela Amodei (anciens d'OpenAI).</p>
    <p><strong>Mission :</strong> Développer une IA sûre, fiable et interprétable. "Constitutionnal AI".</p>
    <p><strong>Jalons clés :</strong></p>
    <ul>
        <li>2021 : Levée de fonds série A ($124M).</li>
        <li>2023 : Lancement de Claude et Claude 2.</li>
        <li>Partenariats majeurs avec Google et Amazon.</li>
    </ul>
    """,

    # Section 2: Macro-Environment
    "macro_title": "2. Macro-Environnement (PESTEL)",
    "macro_content": """
    <ul>
        <li><strong>Politique :</strong> Régulations IA (EU AI Act, décrets US).</li>
        <li><strong>Économique :</strong> Marché de l'IA générative en explosion. Investissements massifs.</li>
        <li><strong>Social :</strong> Crainte de l'IA, impact sur l'emploi, demande d'éthique.</li>
        <li><strong>Technologique :</strong> Course à la puissance (LLM), innovation rapide.</li>
        <li><strong>Écologique :</strong> Consommation énergétique des Data Centers.</li>
        <li><strong>Légal :</strong> Propriété intellectuelle, droits d'auteur, sécurité des données.</li>
    </ul>
    """,

    # Section 3: Internal Analysis
    "internal_title": "3. Analyse Interne",
    "internal_content": """
    <p><strong>Forces :</strong> Recherche de pointe en sécurité (Alignment),Talents ex-OpenAI, Culture de la sécurité.</p>
    <p><strong>Faiblesses :</strong> Moins de visibilité grand public que ChatGPT, dépendance aux financements externes.</p>
    <p><strong>Ressources :</strong> Partenariats cloud (AWS/GCP), capital humain très qualifié.</p>
    """,

    # Section 4: External Analysis
    "external_title": "4. Analyse Externe",
    "external_content": """
    <p><strong>Opportunités :</strong> Marché B2B, intégration dans des outils tiers, demande pour une IA "éthique".</p>
    <p><strong>Menaces :</strong> Concurrence féroce (OpenAI, Google DeepMind, Meta), régulations strictes, coûts de compute.</p>
    <p><strong>Analyse concurrentielle :</strong> Positionnement "Safety First" vs "Move Fast".</p>
    """,

    # Section 5: Strategy & Structure
    "strategy_title": "5. Finalités & Stratégie",
    "strategy_content": """
    <p><strong>Structure :</strong> Public Benefit Corporation (PBC). Structure hybride visant le profit mais avec une mission sociale contraignante.</p>
    <p><strong>Stratégie :</strong> "Safety-focused scaling". Ne pas être les premiers à tout prix, mais être les plus sûrs.</p>
    <p><strong>Métiers :</strong> Chercheurs en ML, Ingénieurs sécurité, Policy experts.</p>
    """,

    # Ecological Focus (SAÉ Requirement)
    "eco_title": "Empreinte Numérique & Solution",
    "eco_content": """
    <p><strong>Le Problème :</strong> L'entraînement des LLM consomme des GWh d'électricité et des milliers de litres d'eau (refroidissement).</p>
    <p><strong>Démarche Anthropic :</strong></p>
    <ul>
        <li>Utilisation de serveurs cloud optimisés (AWS Trainium/Inferentia).</li>
        <li>Recherche sur l'efficacité des modèles ("Smaller models").</li>
        <li>Engagement de transparence (Constitutionnal AI).</li>
    </ul>
    <p><strong>Notre Analyse :</strong> Impact carbone vs Bénéfice social de l'IA.</p>
    """
}

# Pre-calculate group members HTML to avoid formatting issues in the template
POSTER_DATA["group_members_html"] = ' '.join([f'<span>{m}</span> • ' for m in POSTER_DATA["group_members"]])[:-3]

# ==========================================
# HTML TEMPLATE
# ==========================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poster - {subject_company}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0f1014;
            --card-bg: rgba(30, 32, 40, 0.7);
            --accent-color: #d4a373; /* Anthropic-ish warm tone */
            --accent-secondary: #a98467;
            --text-main: #f0f0f0;
            --text-muted: #b0b0b0;
            --border-highlight: rgba(212, 163, 115, 0.3);
            --gradient-1: linear-gradient(135deg, #2b2d42 0%, #1a1b23 100%);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Outfit', sans-serif;
            padding: 2rem;
            min-height: 100vh;
            /* Subtle background pattern */
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(212, 163, 115, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(100, 100, 200, 0.05) 0%, transparent 20%);
        }}

        /* A4/Poster Container wrapper for screen viewing */
        .poster-container {{
            max-width: 1400px; /* Large format */
            margin: 0 auto;
            background: var(--gradient-1);
            border: 1px solid #333;
            border-radius: 20px;
            padding: 3rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            grid-gap: 2rem;
            position: relative;
            overflow: hidden;
        }}

        /* Header spans full width */
        header {{
            grid-column: 1 / -1;
            text-align: center;
            margin-bottom: 2rem;
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 1.5rem;
        }}

        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            color: var(--accent-color);
            margin-bottom: 0.5rem;
            letter-spacing: -1px;
            text-transform: uppercase;
        }}

        .subtitle {{
            font-size: 1.5rem;
            color: var(--text-muted);
            font-weight: 300;
            margin-bottom: 1rem;
        }}

        .group-members {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            font-size: 1.1rem;
            color: var(--text-main);
            background: rgba(255,255,255,0.05);
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            display: inline-flex;
            border: 1px solid rgba(255,255,255,0.1);
        }}

        /* Layout Grid Areas */
        /* Left Column: History & Macro */
        .col-left {{
            grid-column: span 4;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        /* Center Column: Ecological Focus (Centerpiece) & Strategy */
        .col-center {{
            grid-column: span 4;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        /* Right Column: Internal & External */
        .col-right {{
            grid-column: span 4;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        /* Cards Styling */
        .card {{
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-highlight);
            border-radius: 16px;
            padding: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            border-color: var(--accent-color);
        }}

        .card h2 {{
            font-family: 'Playfair Display', serif;
            color: var(--accent-color);
            font-size: 1.8rem;
            margin-bottom: 1rem;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding-bottom: 0.5rem;
        }}

        .card-content {{
            font-size: 1rem;
            line-height: 1.6;
            color: #ddd;
        }}

        .card-content ul {{
            padding-left: 1.2rem;
            margin-bottom: 0.5rem;
        }}
        
        .card-content li {{
            margin-bottom: 0.5rem;
        }}

        .card-content strong {{
            color: #fff;
        }}

        /* Specific Highlights */
        .eco-card {{
            background: rgba(46, 139, 87, 0.1); /* Subtle green tint */
            border-color: rgba(46, 139, 87, 0.4);
        }}
        .eco-card h2 {{
            color: #66c2a5;
        }}

        .intro-card {{
            text-align: center;
            font-style: italic;
            background: transparent;
            border: none;
            box-shadow: none;
        }}

        /* Print Validations */
        @media print {{
            body {{
                background: white;
                color: black;
                padding: 0;
            }}
            .poster-container {{
                box-shadow: none;
                border: none;
                width: 100%;
                max-width: none;
                background: white;
            }}
            .card {{
                background: white;
                border: 2px solid #333;
                color: black;
                page-break-inside: avoid;
            }}
            h1, h2, .subtitle, strong {{
                color: black !important;
            }}
            .card-content {{
                color: black;
            }}
        }}
    </style>
</head>
<body>

    <div class="poster-container">
        <header>
            <h1>{subject_company}</h1>
            <div class="subtitle">{title} <br> {subtitle}</div>
            <div class="group-members">
                {group_members_html}
            </div>
        </header>

        <!-- LEFT COLUMN -->
        <div class="col-left">
            <div class="card">
                <h2>{history_title}</h2>
                <div class="card-content">
                    {history_content}
                </div>
            </div>

            <div class="card">
                <h2>{macro_title}</h2>
                <div class="card-content">
                    {macro_content}
                </div>
            </div>
        </div>

        <!-- CENTER COLUMN -->
        <div class="col-center">
            <div class="card eco-card">
                <h2>🌿 {eco_title}</h2>
                <div class="card-content">
                    {eco_content}
                </div>
            </div>
             <div class="card intro-card">
                <div class="card-content" style="font-size: 1.2rem; border-top: 1px solid #444; border-bottom: 1px solid #444; padding: 1rem;">
                    "Une IA utile, honnête et inoffensive."
                </div>
            </div>
            
             <div class="card">
                <h2>{strategy_title}</h2>
                <div class="card-content">
                    {strategy_content}
                </div>
            </div>
        </div>

        <!-- RIGHT COLUMN -->
        <div class="col-right">
             <div class="card">
                <h2>{internal_title}</h2>
                <div class="card-content">
                    {internal_content}
                </div>
            </div>

            <div class="card">
                <h2>{external_title}</h2>
                <div class="card-content">
                    {external_content}
                </div>
            </div>
        </div>

    </div>

</body>
</html>
"""

def generate_poster():
    output_filename = "poster.html"
    
    # Render the template
    html_content = HTML_TEMPLATE.format(**POSTER_DATA)
    
    # Write to file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Poster généré avec succès : {os.path.abspath(output_filename)}")
    print("Ouvrez ce fichier dans votre navigateur pour voir le résultat et l'imprimer en PDF.")

if __name__ == "__main__":
    generate_poster()
