#!/usr/bin/env python3
"""Documents officiels Declika. Ils ne sont pas servis sur le site : on les joint à Stripe."""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables"
LOGO = ROOT / "public" / "logo-declika.png"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

NAVY = (10, 17, 40)
MUTED = (68, 80, 102)
LINE = (228, 231, 238)
PAPER = (250, 250, 250)
MINT = (100, 255, 218)

RULES = [
    {
        "fr": "-tion",
        "en": "-tion",
        "latin": "Les deux langues tiennent le mot du latin -tio, -tionem. Ce n’est pas un hasard de finale : c’est le même mot savant, passé des deux côtés.",
        "how": "La finale ne bouge pas. Tu retires seulement l’accent français. En américain, -isation s’écrit souvent -ization.",
        "pairs": [
            ("nation", "nation"), ("attention", "attention"), ("éducation", "education"),
            ("information", "information"), ("tradition", "tradition"), ("solution", "solution"),
            ("révolution", "revolution"), ("fonction", "function"), ("action", "action"),
            ("condition", "condition"), ("direction", "direction"), ("production", "production"),
            ("protection", "protection"), ("situation", "situation"), ("relation", "relation"),
            ("communication", "communication"), ("motivation", "motivation"), ("opération", "operation"),
            ("définition", "definition"), ("constitution", "constitution"), ("institution", "institution"),
            ("génération", "generation"), ("population", "population"), ("position", "position"),
        ],
        "gaps": [
            "organisation → organization (US) ou organisation (GB). Le sens ne change pas.",
            "caution n’est pas le même mot : en français, une garantie ; en anglais, de la prudence.",
        ],
    },
    {
        "fr": "-isme",
        "en": "-ism",
        "latin": "Du grec -ismos, passé par le latin -ismus. Le français a -isme, l’anglais -ism. Doctrines, arts, systèmes.",
        "how": "Tu remplaces -isme par -ism. Trois écarts reviennent souvent : ils prennent une syllabe de plus, ou une majuscule.",
        "pairs": [
            ("capitalisme", "capitalism"), ("réalisme", "realism"), ("optimisme", "optimism"),
            ("tourisme", "tourism"), ("journalisme", "journalism"), ("socialisme", "socialism"),
            ("féminisme", "feminism"), ("mécanisme", "mechanism"), ("organisme", "organism"),
            ("nationalisme", "nationalism"), ("modernisme", "modernism"), ("symbolisme", "symbolism"),
            ("racisme", "racism"), ("communisme", "communism"), ("héroïsme", "heroism"),
            ("pragmatisme", "pragmatism"), ("absolutisme", "absolutism"), ("cubisme", "cubism"),
            ("impressionnisme", "impressionism"), ("fascisme", "fascism"),
        ],
        "gaps": [
            "romantisme → romanticism. christianisme → Christianity. judaïsme → Judaism. bouddhisme → Buddhism.",
            "scepticisme → skepticism (US) ou scepticism (GB).",
        ],
    },
    {
        "fr": "-iste",
        "en": "-ist",
        "latin": "Même famille que -isme, pour la personne : celui qui pratique, qui adhère, ou qui exerce.",
        "how": "Tu remplaces -iste par -ist. Le féminin français ne change pas le mot anglais : une journaliste, a journalist.",
        "pairs": [
            ("artiste", "artist"), ("journaliste", "journalist"), ("spécialiste", "specialist"),
            ("dentiste", "dentist"), ("pianiste", "pianist"), ("guitariste", "guitarist"),
            ("économiste", "economist"), ("touriste", "tourist"), ("capitaliste", "capitalist"),
            ("socialiste", "socialist"), ("idéaliste", "idealist"), ("nationaliste", "nationalist"),
            ("terroriste", "terrorist"), ("violoniste", "violinist"), ("cycliste", "cyclist"),
            ("linguiste", "linguist"), ("chimiste", "chemist"), ("biologiste", "biologist"),
            ("généraliste", "generalist"), ("portraitiste", "portraitist"),
        ],
        "gaps": [
            "scientifique, nom, → scientist. L’adjectif scientifique → scientific.",
            "trompettiste ne donne pas trompetist : trumpeter. Garagiste ne suit pas.",
        ],
    },
    {
        "fr": "-ance / -ence",
        "en": "-ance / -ence",
        "latin": "Latin -antia et -entia. Le français a gardé -ance ou -ence. L’anglais aussi, sauf une famille qui passe à -ency.",
        "how": "D’abord, cherche le mot identique, sans accent. Si tu ne le trouves pas, essaie -ency : fréquence, urgence, agence, tendance.",
        "pairs": [
            ("importance", "importance"), ("différence", "difference"), ("patience", "patience"),
            ("violence", "violence"), ("présence", "presence"), ("distance", "distance"),
            ("absence", "absence"), ("conscience", "conscience"), ("intelligence", "intelligence"),
            ("influence", "influence"), ("science", "science"), ("silence", "silence"),
            ("évidence", "evidence"), ("conférence", "conference"), ("conséquence", "consequence"),
            ("existence", "existence"), ("expérience", "experience"), ("référence", "reference"),
            ("résistance", "resistance"), ("excellence", "excellence"),
        ],
        "gaps": [
            "fréquence → frequency. urgence → urgency. agence → agency. tendance → tendency.",
            "confiance → confidence. apparence → appearance. correspondance → correspondence.",
            "émergence → emergence (le fait d’apparaître). Emergency, c’est l’urgence-crise.",
            "naissance ne suit pas. Le mot courant est birth.",
        ],
    },
    {
        "fr": "-ique",
        "en": "-ic",
        "latin": "Latin -icus, grec -ikos. L’anglais raccourcit en -ic, parfois -ical pour l’adjectif.",
        "how": "Nom savant : -ique → -ic ou -ics. Adjectif : -ic, et souvent -ical quand l’anglais a les deux.",
        "pairs": [
            ("musique", "music"), ("logique", "logic"), ("électrique", "electric"),
            ("électronique", "electronic"), ("magique", "magic"), ("spécifique", "specific"),
            ("classique", "classic"), ("tragique", "tragic"), ("automatique", "automatic"),
            ("systématique", "systematic"), ("identique", "identical"), ("dramatique", "dramatic"),
            ("civique", "civic"), ("poétique", "poetic"), ("organique", "organic"),
            ("comique", "comic"), ("dynamique", "dynamic"), ("ironique", "ironic"),
        ],
        "gaps": [
            "économique → economic. Economical veut dire « économe », pas « qui relève de l’économie ».",
            "politique, adjectif → political. Le nom → politics ou policy.",
            "pratique, adjectif → practical. Le nom → practice.",
            "théorique → theoretical. historique → historical. critique, nom de personne → critic.",
            "numérique, au sens actuel, se dit digital. Numeric reste le sens mathématique.",
            "unique reste unique. Ce n’est pas unic.",
        ],
    },
    {
        "fr": "-ie",
        "en": "-y",
        "latin": "Latin et grec -ia. Le français écrit -ie, l’anglais -y. Sciences, arts, régimes, qualités.",
        "how": "Tu remplaces -ie par -y. Tu retires l’accent. Tu vérifies les deux ou trois mots qui ajoutent une syllabe.",
        "pairs": [
            ("énergie", "energy"), ("économie", "economy"), ("géographie", "geography"),
            ("industrie", "industry"), ("technologie", "technology"), ("philosophie", "philosophy"),
            ("biologie", "biology"), ("théorie", "theory"), ("catégorie", "category"),
            ("démocratie", "democracy"), ("géométrie", "geometry"), ("poésie", "poetry"),
            ("harmonie", "harmony"), ("mélodie", "melody"), ("stratégie", "strategy"),
            ("tragédie", "tragedy"), ("comédie", "comedy"), ("ironie", "irony"),
            ("psychologie", "psychology"), ("anatomie", "anatomy"),
            ("colonie", "colony"), ("académie", "academy"), ("photographie", "photography"),
            ("aristocratie", "aristocracy"),
        ],
        "gaps": [
            "galerie → gallery. chimie → chemistry. chirurgie → surgery. série → series.",
            "modestie → modesty. hypocrisie → hypocrisy. jalousie → jealousy. pharmacie → pharmacy.",
            "vie, amie, partie et envie ne suivent pas. famille → family, autre finale. librairie n’est pas library.",
        ],
    },
    {
        "fr": "-aire",
        "en": "-ary",
        "latin": "Latin -arius. L’anglais dit -ary, parfois -ar. Le sens du radical reste, l’orthographe bouge plus qu’ailleurs.",
        "how": "Essaie -ary. Si le mot sonne faux, essaie -ar : populaire, similaire, solaire, polaire, circulaire.",
        "pairs": [
            ("ordinaire", "ordinary"), ("vocabulaire", "vocabulary"), ("salaire", "salary"),
            ("primaire", "primary"), ("secondaire", "secondary"), ("contraire", "contrary"),
            ("nécessaire", "necessary"), ("militaire", "military"), ("volontaire", "voluntary"),
            ("temporaire", "temporary"), ("littéraire", "literary"), ("imaginaire", "imaginary"),
            ("élémentaire", "elementary"), ("dictionnaire", "dictionary"), ("commentaire", "commentary"),
            ("préliminaire", "preliminary"), ("planétaire", "planetary"), ("solaire", "solar"),
            ("populaire", "popular"), ("similaire", "similar"),
            ("circulaire", "circular"), ("culinaire", "culinary"), ("documentaire", "documentary"),
            ("légendaire", "legendary"),
        ],
        "gaps": [
            "sanitaire → sanitary. honoraire → honorary. humanitaire → humanitarian.",
            "révolutionnaire → revolutionary. missionnaire → missionary. fragmentaire → fragmentary.",
            "millionnaire → millionaire. milliardaire → billionaire, pas milliardary.",
            "anniversaire n’est pas anniversary dans l’usage courant : c’est souvent birthday.",
        ],
    },
    {
        "fr": "-té",
        "en": "-ty",
        "latin": "Latin -tas, -tatis. Liberté et liberty viennent tous deux de libertatem. La finale française -té et l’anglaise -ty sont le même héritage, pas une astuce d’orthographe.",
        "how": "Tu remplaces -té par -ty. Tu gardes les lettres du radical : qualité → quality, pas qualty. L’accent tombe.",
        "pairs": [
            ("liberté", "liberty"), ("qualité", "quality"), ("société", "society"),
            ("activité", "activity"), ("réalité", "reality"), ("identité", "identity"),
            ("sécurité", "security"), ("difficulté", "difficulty"), ("responsabilité", "responsibility"),
            ("université", "university"), ("curiosité", "curiosity"), ("possibilité", "possibility"),
            ("nationalité", "nationality"), ("personnalité", "personality"), ("cité", "city"),
            ("beauté", "beauty"), ("clarté", "clarity"), ("pureté", "purity"),
            ("unité", "unity"), ("diversité", "diversity"), ("densité", "density"),
            ("quantité", "quantity"), ("égalité", "equality"), ("autorité", "authority"),
        ],
        "gaps": [
            "capacité → capacity. priorité → priority. nécessité → necessity. communauté → community.",
            "majorité → majority. électricité → electricity. gravité → gravity. charité → charity.",
            "Ne suivent pas : santé, côté, été, bonté, fierté, volonté, moitié.",
            "vérité se dit truth. Verity existe, il est rare. publicité, « réclame », n’est pas publicity.",
            "amitié → amity, rare. Le mot courant est friendship.",
        ],
    },
    {
        "fr": "-eux",
        "en": "-ous",
        "latin": "Latin -osus. Sérieux et serious viennent de seriosus. La forme féminine -euse ne crée pas un second mot anglais.",
        "how": "Adjectif en -eux ou -euse : tu vises -ous. Tu vérifies le radical avant de coller la finale.",
        "pairs": [
            ("sérieux", "serious"), ("fameux", "famous"), ("dangereux", "dangerous"),
            ("nerveux", "nervous"), ("curieux", "curious"), ("furieux", "furious"),
            ("religieux", "religious"), ("généreux", "generous"), ("précieux", "precious"),
            ("nombreux", "numerous"), ("courageux", "courageous"), ("joyeux", "joyous"),
            ("mystérieux", "mysterious"), ("spacieux", "spacious"), ("ambitieux", "ambitious"),
            ("délicieux", "delicious"), ("prestigieux", "prestigious"), ("anxieux", "anxious"),
            ("envieux", "envious"), ("glorieux", "glorious"), ("studieux", "studious"),
            ("judicieux", "judicious"), ("harmonieux", "harmonious"), ("victorieux", "victorious"),
        ],
        "gaps": [
            "merveilleux → marvelous (US) ou marvellous (GB). hideux → hideous. monstrueux → monstrous.",
            "superstitieux → superstitious. vicieux → vicious. poreux → porous. visqueux → viscous.",
            "Ne suivent pas : heureux, vieux, honteux, paresseux, ennuyeux, chanceux.",
            "malicieux se dit mischievous. Malicious veut dire méchant. fastidieux se dit tedious. Fastidious veut dire difficile sur les détails.",
        ],
    },
    {
        "fr": "-eur",
        "en": "-or",
        "latin": "Latin -or. Pour les noms d’agent, le français a fait -eur et l’anglais a gardé -or : acteur et actor viennent d’actor. Plusieurs noms de qualité suivent le même latin.",
        "how": "Si le mot désigne une personne ou une fonction, vise -or. Si c’est une mesure du corps ou un sentiment très concret, ne force pas la finale.",
        "pairs": [
            ("acteur", "actor"), ("directeur", "director"), ("créateur", "creator"),
            ("professeur", "professor"), ("docteur", "doctor"), ("inventeur", "inventor"),
            ("éditeur", "editor"), ("auteur", "author"), ("spectateur", "spectator"),
            ("opérateur", "operator"), ("inspecteur", "inspector"), ("protecteur", "protector"),
            ("ambassadeur", "ambassador"), ("empereur", "emperor"), ("erreur", "error"),
            ("terreur", "terror"), ("faveur", "favor"), ("honneur", "honor"),
            ("odeur", "odor"), ("vigueur", "vigor"), ("rigueur", "rigor"),
            ("splendeur", "splendor"), ("moteur", "motor"), ("générateur", "generator"),
        ],
        "gaps": [
            "ingénieur → engineer. couleur → color. valeur → value. lecteur → reader.",
            "conducteur, au sens du train, → conductor. Au sens de celui qui conduit une voiture, driver est plus courant.",
            "facteur, « celui qui porte le courrier », n’est pas factor. Factor est le facteur mathématique.",
            "Ne suivent pas : bonheur, peur, douleur, fleur, cœur, largeur, longueur, hauteur, chaleur.",
        ],
    },
]

NEIGHBORS = [
    ("-el → -al", "Latin -alis. naturel → natural, culturel → cultural, formel → formal, personnel → personal, originel → original, industriel → industrial.", "actuel n’est pas actual. Actuel = en ce moment. Actual = réel. C’est le faux ami le plus coûteux de cette finale."),
    ("-able → -able", "La finale est déjà commune. acceptable → acceptable, probable → probable, notable → notable, responsable → responsible, confortable → comfortable.", "Le sens passe en général. Tu vérifies quand même le radical, pas seulement les cinq lettres."),
    ("-if → -ive", "Latin -ivus. actif → active, positif → positive, négatif → negative, créatif → creative, natif → native.", "Décisif → decisive. Le f français devient un v anglais, puis -e."),
    ("-ment, les noms", "moment → moment, document → document, argument → argument, instrument → instrument, monument → monument.", "Les adverbes en -ment ne sont pas des cognats automatiques : rapidement → rapidly, pas rapidment."),
]

FRIENDS = [
    ("actuel", "en ce moment", "actual", "réel, véritable"),
    ("actuellement", "en ce moment", "actually", "en fait"),
    ("éventuellement", "peut-être, le cas échéant", "eventually", "finalement"),
    ("assister à", "être présent", "to assist", "aider"),
    ("librairie", "magasin de livres", "library", "bibliothèque"),
    ("sensible", "qui ressent vite", "sensible", "raisonnable"),
    ("décevoir", "décevoir", "to deceive", "tromper"),
    ("attendre", "patienter", "to attend", "assister à"),
    ("prévenir", "avertir", "to prevent", "empêcher"),
    ("lecture", "le fait de lire", "lecture", "une conférence"),
    ("caution", "une garantie, un dépôt", "caution", "de la prudence"),
    ("avertissement", "un avertissement", "advertisement", "une publicité"),
    ("sympathique", "agréable", "sympathetic", "compatissant"),
    ("formation", "une formation, un apprentissage", "formation", "le fait de se former"),
    ("compréhensif", "qui comprend l’autre", "comprehensive", "complet, pas « gentil »"),
    ("coin", "un angle", "coin", "une pièce de monnaie"),
    ("pain", "du pain", "pain", "de la douleur"),
    ("chair", "la chair", "chair", "une chaise"),
    ("store", "un store", "store", "un magasin"),
    ("location", "souvent une location", "location", "un lieu"),
    ("entrée", "une entrée, au repas", "entrée", "aux États-Unis, souvent le plat"),
]

READINGS = [
    {
        "title": "Une note d’université",
        "text": (
            "The university administration published a formal communication on the protection of cultural diversity "
            "and national identity. The director described the situation as serious, not dangerous. "
            "A specialist in public education asked for clarity, equality and security. "
            "The institution refused a purely symbolic solution and demanded a practical definition of responsibility."
        ),
        "hits": [
            ("administration", "-tion"), ("communication", "-tion"), ("protection", "-tion"),
            ("cultural", "-el → -al"), ("diversity", "-té"), ("national", "-al"),
            ("identity", "-té"), ("director", "-eur"), ("situation", "-tion"),
            ("serious", "-eux"), ("dangerous", "-eux"), ("specialist", "-iste"),
            ("education", "-tion"), ("clarity", "-té"), ("equality", "-té"),
            ("security", "-té"), ("institution", "-tion"), ("solution", "-tion"),
            ("practical", "-ique"), ("definition", "-tion"), ("responsibility", "-té"),
        ],
    },
    {
        "title": "Une page de science",
        "text": (
            "Modern biology and chemistry describe energy, gravity and electricity with the same theoretical vocabulary. "
            "An organic mechanism is not a moral reality. The scientist insisted on evidence, experience and systematic observation. "
            "Photography of the colony revealed an extraordinary density of activity, and a mysterious absence of violence."
        ),
        "hits": [
            ("modern", "radical"), ("biology", "-ie"), ("chemistry", "écart de -ie"),
            ("energy", "-ie"), ("gravity", "-té"), ("electricity", "-té"),
            ("theoretical", "-ique"), ("vocabulary", "-aire"), ("organic", "-ique"),
            ("mechanism", "-isme"), ("moral", "-al"), ("reality", "-té"),
            ("scientist", "écart de -iste"), ("evidence", "-ence"), ("experience", "-ence"),
            ("systematic", "-ique"), ("photography", "-ie"), ("colony", "-ie"),
            ("extraordinary", "-aire"), ("density", "-té"), ("activity", "-té"),
            ("mysterious", "-eux"), ("absence", "-ence"), ("violence", "-ence"),
        ],
    },
    {
        "title": "Un portrait",
        "text": (
            "The ambitious professor was famous for his curiosity, his generosity and his rigorous humor. "
            "He was religious without being furious, serious without being vicious. "
            "His personality united liberty of judgment and a capacity for silence. "
            "Students called him judicious. They did not call him happy: heureux would have been the wrong rule."
        ),
        "hits": [
            ("ambitious", "-eux"), ("professor", "-eur"), ("famous", "-eux"),
            ("curiosity", "-té"), ("generosity", "-té"), ("rigorous", "latin -osus"),
            ("religious", "-eux"), ("furious", "-eux"), ("serious", "-eux"),
            ("vicious", "-eux"), ("personality", "-té"), ("liberty", "-té"),
            ("capacity", "-té"), ("silence", "-ence"), ("judicious", "-eux"),
        ],
    },
]


class Paper(FPDF):
    def __init__(self, running: str):
        super().__init__(format="A4", unit="mm")
        self.running = running
        self.set_auto_page_break(auto=True, margin=16)
        self.set_margins(14, 20, 14)
        self.add_font("Sans", "", SANS)
        self.add_font("Sans", "B", SANS_B)
        self.add_font("Serif", "", SERIF)
        self.add_font("Serif", "B", SERIF_B)

    def header(self):
        if self.page_no() == 1:
            return
        self.image(str(LOGO), 14, 7, h=6)
        self.set_font("Sans", "", 8)
        self.set_text_color(*MUTED)
        self.set_xy(14, 8)
        self.cell(182, 5, self.running, align="R")
        self.set_draw_color(*LINE)
        self.set_line_width(0.2)
        self.line(14, 15.5, 196, 15.5)

    def footer(self):
        self.set_y(-12)
        self.set_font("Sans", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 5, "Declika  ·  document officiel", align="L")
        self.set_xy(14, -12)
        self.cell(182, 5, f"{self.page_no():02d}", align="R")

    def start(self, title: str, subject: str):
        self.set_title(title)
        self.set_author("Declika")
        self.set_subject(subject)
        self.set_creator("Declika")
        self.add_page()

    def h1(self, text: str):
        self.set_x(14)
        self.set_font("Serif", "B", 18)
        self.set_text_color(*NAVY)
        self.multi_cell(182, 8, text)
        self.ln(1)

    def prose(self, text: str, size=10.5, gap=5.2):
        self.set_x(14)
        self.set_font("Serif", "", size)
        self.set_text_color(*NAVY)
        self.multi_cell(182, gap, text)
        self.ln(1.5)

    def muted(self, text: str):
        self.set_x(14)
        self.set_font("Sans", "", 9.5)
        self.set_text_color(*MUTED)
        self.multi_cell(182, 4.6, text)
        self.ln(1)

    def bridge(self, left: str, right: str):
        y = self.get_y() + 1
        self.set_fill_color(*NAVY)
        self.rect(14, y, 78, 12, "F")
        self.set_fill_color(*MINT)
        self.rect(96, y + 4.5, 12, 3, "F")
        self.set_fill_color(*NAVY)
        self.rect(112, y, 84, 12, "F")
        self.set_text_color(255, 255, 255)
        self.set_font("Sans", "B", 13)
        self.set_xy(14, y + 2.5)
        self.cell(78, 7, left, align="C")
        self.set_xy(112, y + 2.5)
        self.cell(84, 7, right, align="C")
        self.set_y(y + 15)

    def pairs(self, rows):
        self.set_font("Sans", "", 9)
        col_w = 88
        row_h = 5.1
        half = (len(rows) + 1) // 2
        left, right = rows[:half], rows[half:]
        y0 = self.get_y()
        for index, (fr, en) in enumerate(left):
            y = y0 + index * row_h
            self.set_xy(14, y)
            self.set_text_color(*NAVY)
            self.cell(44, row_h, fr)
            self.set_text_color(*MUTED)
            self.cell(44, row_h, en)
        for index, (fr, en) in enumerate(right):
            y = y0 + index * row_h
            self.set_xy(14 + col_w + 6, y)
            self.set_text_color(*NAVY)
            self.cell(44, row_h, fr)
            self.set_text_color(*MUTED)
            self.cell(44, row_h, en)
        lines = max(len(left), len(right))
        self.set_y(y0 + lines * row_h + 2)

    def gaps(self, lines):
        y = self.get_y() + 1
        self.set_fill_color(*PAPER)
        # height estimated then drawn after text? Draw a bar label instead of a filled box that can overflow.
        self.set_font("Sans", "B", 8.5)
        self.set_text_color(*NAVY)
        self.set_xy(14, y)
        self.cell(182, 5, "ÉCARTS  ·  NE PAS FORCER LA FINALE")
        self.set_y(y + 5.5)
        self.set_font("Sans", "", 9)
        self.set_text_color(*MUTED)
        for line in lines:
            self.set_x(14)
            self.multi_cell(182, 4.4, line)


def cover(pdf: Paper, kicker: str, title: str, deck: str):
    pdf.image(str(LOGO), 14, 16, h=10)
    pdf.set_draw_color(*MINT)
    pdf.set_line_width(1.1)
    pdf.line(14, 32, 70, 32)
    pdf.set_xy(14, 42)
    pdf.set_font("Sans", "", 10)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 6, kicker, new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(14)
    pdf.set_font("Serif", "B", 28)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(170, 12, title)
    pdf.ln(2)
    pdf.set_x(14)
    pdf.set_font("Serif", "", 12)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(160, 6.5, deck)
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 272, 210, 25, "F")
    pdf.set_xy(14, 280)
    pdf.set_font("Sans", "", 9)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 6, "Document officiel   ·   Français  →  anglais   ·   2026")


def build_list():
    pdf = Paper("Liste complète")
    pdf.start("Declika — Liste complète", "Dix finales pour reconnaître l’anglais à partir du français.")
    cover(
        pdf,
        "LISTE COMPLÈTE",
        "Dix finales.\nLe reste suit.",
        "Les mots fréquents, l’origine de la finale, et les écarts. "
        "Tu ne retiens pas une liste. Tu reconnais une famille.",
    )
    pdf.set_y(122)
    for index, rule in enumerate(RULES, start=1):
        col = (index - 1) % 2
        if col == 0:
            row_y = pdf.get_y()
        pdf.set_fill_color(*NAVY)
        pdf.rect(14 + col * 92, row_y, 86, 9, "F")
        pdf.set_xy(14 + col * 92, row_y)
        pdf.set_font("Sans", "B", 9)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(86, 9, f"  {index:02d}   {rule['fr']}  →  {rule['en']}")
        if col == 1:
            pdf.set_y(row_y + 12)

    pdf.add_page()
    pdf.h1("Comment lire une page")
    pdf.prose(
        "Chaque finale tient sur une page. En haut, d’où elle vient. Au milieu, des paires fréquentes, "
        "pas un dictionnaire. En bas, les écarts : les mots qui refusent la règle, et ceux qui la tordent."
    )
    pdf.prose(
        "Geste. Tu isoles la finale, pas le mot entier. Tu appliques la page. Si le sens obtenu est absurde, "
        "tu lis les écarts avant d’inventer une orthographe. L’accent français tombe presque toujours."
    )
    pdf.muted("Ordre du document : d’abord les finales qui changent le moins, ensuite celles qui demandent une vérification.")
    pdf.ln(2)
    pdf.set_font("Sans", "B", 9)
    pdf.set_text_color(*NAVY)
    pdf.set_x(14)
    pdf.cell(182, 6, "LES DIX PAGES")
    pdf.ln(7)
    for index, rule in enumerate(RULES, start=1):
        pdf.set_x(14)
        pdf.set_font("Sans", "B", 11)
        pdf.set_text_color(*NAVY)
        pdf.cell(18, 7, f"{index:02d}")
        pdf.set_font("Serif", "", 12)
        pdf.cell(70, 7, f"{rule['fr']}  →  {rule['en']}")
        pdf.ln(7.2)

    index = []
    for number, rule in enumerate(RULES, start=1):
        pdf.add_page()
        pdf.set_font("Sans", "", 9)
        pdf.set_text_color(*MUTED)
        pdf.set_x(14)
        pdf.cell(182, 5, f"Règle  {number:02d}  /  10")
        pdf.ln(6)
        pdf.h1(f"{rule['fr']}   →   {rule['en']}")
        pdf.bridge(rule["fr"], rule["en"])
        pdf.prose(rule["latin"], size=11, gap=5.4)
        pdf.muted(rule["how"])
        pdf.ln(1)
        pdf.pairs(rule["pairs"])
        pdf.gaps(rule["gaps"])
        for french, _english in rule["pairs"]:
            index.append((french, pdf.page_no()))

    pdf.add_page()
    pdf.h1("Quatre finales voisines")
    pdf.prose(
        "Elles ne font pas partie des dix. Elles rapportent assez pour tenir ici, à condition de ne pas les mélanger avec les pages précédentes."
    )
    for title, body, trap in NEIGHBORS:
        pdf.ln(2)
        pdf.set_x(14)
        pdf.set_font("Sans", "B", 12)
        pdf.set_text_color(*NAVY)
        pdf.cell(182, 7, title)
        pdf.ln(7)
        pdf.prose(body, size=10.5, gap=5)
        pdf.muted(trap)

    pdf.add_page()
    pdf.h1("Index des mots de la liste")
    pdf.muted("Le mot français, puis la page de sa finale. Les écarts cités dans le texte ne sont pas tous repris ici.")
    index.sort(key=lambda item: item[0])
    per_col = 46
    cols = 3
    col_w = 60
    row_h = 4.4
    start = 0
    while start < len(index):
        y0 = pdf.get_y() + 2
        chunk = index[start : start + per_col * cols]
        for j, (word, page) in enumerate(chunk):
            col = j // per_col
            row = j % per_col
            pdf.set_xy(14 + col * col_w, y0 + row * row_h)
            pdf.set_font("Sans", "", 8)
            pdf.set_text_color(*NAVY)
            pdf.cell(46, row_h, word)
            pdf.set_text_color(*MUTED)
            pdf.cell(12, row_h, f"{page:02d}")
        start += len(chunk)
        if start < len(index):
            pdf.add_page()
            pdf.h1("Index, suite")

    pdf.add_page()
    pdf.h1("Ce que ce document ne fait pas")
    pdf.prose("Il ne donne pas la prononciation. Il ne donne pas la grammaire. Il ne promet pas des milliers de mots sus en une soirée.")
    pdf.prose("Il sert à les reconnaître en lisant. Le carnet reprend les mêmes paires, pour les répéter. La mini-formation les fait retrouver sans la page sous les yeux. Le bonus du pack traite les faux amis et trois lectures.")
    pdf.prose("Quand deux orthographes existent, l’américaine est donnée en premier, la britannique est nommée. Rien ici n’est une liste fermée.")
    pdf.ln(3)
    pdf.set_x(14)
    pdf.set_font("Sans", "B", 8.5)
    pdf.set_text_color(*NAVY)
    pdf.cell(182, 6, "LES DIX FINALES, POUR S’EN SOUVENIR")
    pdf.ln(8)
    for index, rule in enumerate(RULES, start=1):
        col = (index - 1) % 2
        if col == 0:
            y = pdf.get_y()
        else:
            pdf.set_y(y)
        pdf.set_xy(14 + col * 92, pdf.get_y())
        pdf.set_fill_color(*NAVY)
        pdf.rect(14 + col * 92, pdf.get_y(), 86, 8, "F")
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Sans", "B", 9)
        pdf.cell(86, 8, f"  {index:02d}   {rule['fr']}  →  {rule['en']}", align="L")
        if col == 1:
            pdf.ln(10)
    path = OUT / "Declika-Liste-Complete.pdf"
    OUT.mkdir(parents=True, exist_ok=True)
    pdf.output(path)
    print(path, path.stat().st_size, "pages", pdf.page_no())
    return index


def build_formation():
    pdf = Paper("Mini-formation")
    pdf.start("Declika — Mini-formation", "Dix règles, exercices de reconnaissance.")
    cover(
        pdf,
        "MINI-FORMATION",
        "Retrouver\nla finale.",
        "Dix pages d’exercice. Les réponses sont à la fin, pas sous la question. "
        "Ce n’est pas un cours d’oral.",
    )
    pdf.set_y(128)
    pdf.set_font("Sans", "B", 8)
    pdf.set_text_color(*MUTED)
    pdf.set_x(14)
    pdf.cell(182, 5, "LES DIX EXERCICES")
    pdf.ln(7)
    for index, title in enumerate(
        [
            "-tion", "-isme", "-iste", "-ance / -ence", "-ique",
            "-ie", "-aire", "-té", "-eux", "-eur",
        ],
        start=1,
    ):
        col = (index - 1) % 2
        if col == 0:
            row_y = pdf.get_y()
        pdf.set_xy(14 + col * 92, row_y)
        pdf.set_font("Sans", "", 11)
        pdf.set_text_color(*NAVY)
        pdf.cell(92, 7, f"{index:02d}    {title}")
        if col == 1:
            pdf.set_y(row_y + 8)
    pdf.add_page()
    pdf.h1("Comment travailler")
    pdf.prose("Une page, une finale. Tu lis le rappel. Tu caches le bas du document. Tu écris l’anglais. Ensuite seulement, tu ouvres le corrigé.")
    pdf.prose("Si tu hésites entre deux finales, tu choisis la plus haute dans la liste : -tion avant -té, -ique avant une invention. L’écart se vérifie dans la liste complète, pas de mémoire.")
    exercises = [
        ("-tion → -tion", ["solution", "révolution", "protection", "génération", "institution", "définition", "population", "motivation"]),
        ("-isme → -ism", ["socialisme", "féminisme", "mécanisme", "organisme", "modernisme", "pragmatisme", "cubisme", "héroïsme"]),
        ("-iste → -ist", ["économiste", "violoniste", "biologiste", "touriste", "idéaliste", "linguiste", "chimiste", "terroriste"]),
        ("-ance / -ence", ["évidence", "existence", "résistance", "excellence", "intelligence", "conséquence", "conférence", "silence"]),
        ("-ique → -ic", ["électronique", "dramatique", "systématique", "identique", "organique", "ironique", "automatique", "poétique"]),
        ("-ie → -y", ["philosophie", "géométrie", "stratégie", "tragédie", "démocratie", "mélodie", "ironie", "anatomie"]),
        ("-aire → -ary / -ar", ["temporaire", "imaginaire", "élémentaire", "dictionnaire", "populaire", "similaire", "circulaire", "légendaire"]),
        ("-té → -ty", ["identité", "sécurité", "responsabilité", "curiosité", "diversité", "quantité", "beauté", "égalité"]),
        ("-eux → -ous", ["mystérieux", "ambitieux", "délicieux", "courageux", "judicieux", "harmonieux", "victorieux", "prestigieux"]),
        ("-eur → -or", ["spectateur", "inventeur", "ambassadeur", "inspecteur", "honneur", "vigueur", "erreur", "générateur"]),
    ]
    for index, (title, words) in enumerate(exercises, start=1):
        pdf.add_page()
        pdf.set_font("Sans", "", 9)
        pdf.set_text_color(*MUTED)
        pdf.set_x(14)
        pdf.cell(182, 5, f"Exercice  {index:02d}  /  10")
        pdf.ln(6)
        pdf.h1(title)
        pdf.prose("Écris le mot anglais. Si la finale ne suffit pas, note « écart » et passe. Tu vérifieras dans le corrigé.")
        pdf.ln(2)
        for number, word in enumerate(words, start=1):
            y = pdf.get_y()
            pdf.set_draw_color(*LINE)
            pdf.line(14, y, 196, y)
            pdf.set_xy(14, y + 1.5)
            pdf.set_font("Sans", "B", 12)
            pdf.set_text_color(*NAVY)
            pdf.cell(12, 8, f"{number:02d}")
            pdf.set_font("Serif", "", 13)
            pdf.cell(70, 8, word)
            pdf.set_draw_color(207, 212, 222)
            pdf.line(100, y + 8, 190, y + 8)
            pdf.set_y(y + 11)
        traps = [
            "Écart fréquent : organisation s’écrit organization en américain.",
            "Écart fréquent : romantisme → romanticism, pas romantism.",
            "Écart fréquent : scientifique, le nom, → scientist.",
            "Écart fréquent : fréquence → frequency, pas frequence.",
            "Écart fréquent : économique → economic, pas economical.",
            "Écart fréquent : chimie → chemistry, pas chimy.",
            "Écart fréquent : populaire → popular, pas populary.",
            "Écart fréquent : qualité → quality. Le a du radical reste.",
            "Écart fréquent : heureux ne devient pas heureous.",
            "Écart fréquent : ingénieur → engineer, pas ingenior.",
        ]
        pdf.ln(2)
        pdf.muted(traps[index - 1])

    pdf.add_page()
    pdf.h1("Corrigé")
    pdf.muted("Le mot anglais attendu. « Écart » signale une finale qui ne se colle pas telle quelle : le détail est dans la liste.")
    answers = [
        ["solution", "revolution", "protection", "generation", "institution", "definition", "population", "motivation"],
        ["socialism", "feminism", "mechanism", "organism", "modernism", "pragmatism", "cubism", "heroism"],
        ["economist", "violinist", "biologist", "tourist", "idealist", "linguist", "chemist", "terrorist"],
        ["evidence", "existence", "resistance", "excellence", "intelligence", "consequence", "conference", "silence"],
        ["electronic", "dramatic", "systematic", "identical", "organic", "ironic", "automatic", "poetic"],
        ["philosophy", "geometry", "strategy", "tragedy", "democracy", "melody", "irony", "anatomy"],
        ["temporary", "imaginary", "elementary", "dictionary", "popular", "similar", "circular", "legendary"],
        ["identity", "security", "responsibility", "curiosity", "diversity", "quantity", "beauty", "equality"],
        ["mysterious", "ambitious", "delicious", "courageous", "judicious", "harmonious", "victorious", "prestigious"],
        ["spectator", "inventor", "ambassador", "inspector", "honor", "vigor", "error", "generator"],
    ]
    for index, (title, words) in enumerate(exercises):
        if pdf.get_y() > 250:
            pdf.add_page()
        pdf.ln(2)
        pdf.set_x(14)
        pdf.set_font("Sans", "B", 11)
        pdf.set_text_color(*NAVY)
        pdf.cell(182, 6, f"{index + 1:02d}   {title}")
        pdf.ln(6)
        pdf.set_font("Sans", "", 9.5)
        for word, answer in zip(words, answers[index]):
            pdf.set_x(14)
            pdf.set_text_color(*MUTED)
            pdf.cell(55, 5, word)
            pdf.set_text_color(*NAVY)
            pdf.cell(0, 5, answer, new_x="LMARGIN", new_y="NEXT")

    path = OUT / "Declika-Mini-formation.pdf"
    pdf.output(path)
    print(path, path.stat().st_size, "pages", pdf.page_no())


def build_bonus():
    pdf = Paper("Bonus  ·  faux amis et lectures")
    pdf.start("Declika — Bonus", "Faux amis et lectures annotées. Inclus dans le pack.")
    cover(
        pdf,
        "BONUS  ·  PACK COMPLET",
        "Le mot juste,\npas le mot proche.",
        "Vingt-deux faux amis, puis trois lectures où les finales se rencontrent. "
        "Inclus dans le pack. Pas vendu à part.",
    )
    pdf.add_page()
    pdf.h1("Pourquoi le mot proche ment")
    pdf.prose(
        "Un cognat partage une origine. Il ne partage pas toujours le sens d’aujourd’hui. "
        "Les deux langues ont gardé la forme et ont laissé partir l’usage. "
        "C’est pour cela qu’un très bon lecteur français peut écrire eventually en voulant dire éventuellement."
    )
    pdf.prose(
        "La liste apprend à reconnaître. Cette page apprend à s’arrêter. "
        "Si le mot anglais existe, tu vérifies le sens avant de t’en servir. "
        "La finale ne suffit plus."
    )
    pdf.ln(2)
    pdf.set_font("Sans", "B", 8.5)
    pdf.set_text_color(*NAVY)
    pdf.set_x(14)
    pdf.cell(46, 6, "FRANÇAIS")
    pdf.cell(46, 6, "SENS")
    pdf.cell(46, 6, "ANGLAIS")
    pdf.cell(44, 6, "SENS")
    pdf.ln(6)
    pdf.set_font("Sans", "", 8.5)
    for fr, fr_sense, en, en_sense in FRIENDS:
        if pdf.get_y() > 265:
            pdf.add_page()
            pdf.set_font("Sans", "", 8.5)
        y = pdf.get_y()
        pdf.set_draw_color(*LINE)
        pdf.line(14, y, 196, y)
        pdf.set_xy(14, y + 0.8)
        pdf.set_text_color(*NAVY)
        pdf.cell(46, 5.2, fr)
        pdf.set_text_color(*MUTED)
        pdf.cell(46, 5.2, fr_sense)
        pdf.set_text_color(*NAVY)
        pdf.cell(46, 5.2, en)
        pdf.set_text_color(*MUTED)
        pdf.cell(44, 5.2, en_sense)
        pdf.ln(6.2)

    for reading in READINGS:
        pdf.add_page()
        pdf.h1(reading["title"])
        pdf.prose(reading["text"], size=12, gap=6.2)
        pdf.ln(2)
        pdf.set_x(14)
        pdf.set_font("Sans", "B", 8.5)
        pdf.set_text_color(*NAVY)
        pdf.cell(182, 6, "CE QUE TU PEUX RECONNAÎTRE")
        pdf.ln(7)
        pdf.pairs([(word, rule) for word, rule in reading["hits"]])
        pdf.muted("Lis d’abord sans rien souligner. Relis en nommant la finale. Le sens de la phrase prime sur la finale.")

    pdf.add_page()
    pdf.h1("Protocole, en une page")
    steps = [
        ("1", "Isoler la finale du mot anglais, pas le mot entier."),
        ("2", "La rapprocher d’une des dix pages de la liste."),
        ("3", "Si le sens de la phrase résiste, ouvrir les faux amis avant de conclure."),
        ("4", "Ne pas inventer l’orthographe française à partir d’une finale anglaise rare."),
        ("5", "Revenir au carnet seulement sur les finales qui ont résisté, pas sur tout le texte."),
    ]
    for number, text in steps:
        y = pdf.get_y() + 2
        pdf.set_fill_color(*NAVY)
        pdf.rect(14, y, 10, 10, "F")
        pdf.set_xy(14, y + 1.5)
        pdf.set_font("Sans", "B", 11)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(10, 7, number, align="C")
        pdf.set_xy(28, y + 1.2)
        pdf.set_font("Serif", "", 12)
        pdf.set_text_color(*NAVY)
        pdf.multi_cell(164, 6, text)
        pdf.set_y(y + 14)
    pdf.ln(4)
    pdf.prose("Le pack s’arrête là. L’application n’existe pas encore. Rien dans ce bonus ne la remplace, et rien ne la promet.")
    path = OUT / "Declika-Bonus.pdf"
    pdf.output(path)
    print(path, path.stat().st_size, "pages", pdf.page_no())


def build_carnet():
    def cell(value: str) -> str:
        if any(mark in value for mark in ",\"\n"):
            return '"' + value.replace('"', '""') + '"'
        return value

    rows = ["Français,Anglais,Règle"]
    for rule in RULES:
        for french, english in rule["pairs"]:
            rows.append(",".join(cell(part) for part in (french, english, rule["fr"])))
    path = OUT / "Declika-Carnet.csv"
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(path, path.stat().st_size, "cartes", len(rows) - 1)


if __name__ == "__main__":
    build_list()
    build_formation()
    build_bonus()
    build_carnet()
