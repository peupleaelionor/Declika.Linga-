#!/usr/bin/env python3
"""Build the Declika word-ending list. Not served on the site: attach it to the Stripe Payment Link."""

from pathlib import Path

from fpdf import FPDF

NAVY = (10, 17, 40)
MUTED = (68, 80, 102)
LINE = (228, 231, 238)
PAPER = (250, 250, 250)
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

RULES = [
    {
        "fr": "-tion",
        "en": "-tion",
        "text": "La finale la plus stable. Le mot se reconnaît presque tel quel.",
        "pairs": [
            ("nation", "nation"),
            ("attention", "attention"),
            ("éducation", "education"),
            ("information", "information"),
            ("tradition", "tradition"),
        ],
        "except": "L’orthographe américaine change parfois le s en z : organisation → organization.",
    },
    {
        "fr": "-isme",
        "en": "-ism",
        "text": "Les noms de doctrine et de courant passent presque toujours.",
        "pairs": [
            ("capitalisme", "capitalism"),
            ("réalisme", "realism"),
            ("optimisme", "optimism"),
            ("tourisme", "tourism"),
            ("journalisme", "journalism"),
        ],
        "except": "Peu d’exceptions. Vérifie le sens : un -isme français n’a pas toujours d’équivalent courant.",
    },
    {
        "fr": "-iste",
        "en": "-ist",
        "text": "La personne, le métier ou le partisan. Le geste est le même que pour -isme.",
        "pairs": [
            ("artiste", "artist"),
            ("journaliste", "journalist"),
            ("spécialiste", "specialist"),
            ("dentiste", "dentist"),
            ("pianiste", "pianist"),
        ],
        "except": "Quelques métiers ne suivent pas : médecin n’est pas dans cette finale.",
    },
    {
        "fr": "-ance, -ence",
        "en": "-ance, -ence",
        "text": "Les noms abstraits gardent souvent la même finale, avec l’accent en moins.",
        "pairs": [
            ("importance", "importance"),
            ("différence", "difference"),
            ("patience", "patience"),
            ("violence", "violence"),
            ("présence", "presence"),
        ],
        "except": "Confiance devient confidence, pas confiance. Naissance ne suit pas la finale.",
    },
    {
        "fr": "-ique",
        "en": "-ic",
        "text": "Adjectifs et noms savants. La finale se raccourcit.",
        "pairs": [
            ("musique", "music"),
            ("logique", "logic"),
            ("publique", "public"),
            ("électrique", "electric"),
            ("magique", "magic"),
            ("spécifique", "specific"),
        ],
        "except": "Politique devient political. Économique devient economic. Economical veut dire « économe » : ce n’est pas le même mot.",
    },
    {
        "fr": "-ie",
        "en": "-y",
        "text": "Surtout les noms de domaine, de science et d’état.",
        "pairs": [
            ("énergie", "energy"),
            ("économie", "economy"),
            ("géographie", "geography"),
            ("industrie", "industry"),
            ("technologie", "technology"),
        ],
        "except": "Vie, amie et partie ne suivent pas. Famille devient family, hors de cette finale.",
    },
    {
        "fr": "-aire",
        "en": "-ary",
        "text": "Utile pour les adjectifs et une partie des noms. L’orthographe bouge plus que la finale.",
        "pairs": [
            ("ordinaire", "ordinary"),
            ("vocabulaire", "vocabulary"),
            ("salaire", "salary"),
            ("primaire", "primary"),
            ("sanitaire", "sanitary"),
        ],
        "except": "Nécessaire devient necessary. Millionnaire devient millionaire, pas millionary.",
    },
    {
        "fr": "-té",
        "en": "-ty",
        "text": "La finale change, le sens reste. C’est l’une des plus rentables, et l’une des plus piégeuses.",
        "pairs": [
            ("liberté", "liberty"),
            ("qualité", "quality"),
            ("société", "society"),
            ("activité", "activity"),
            ("réalité", "reality"),
        ],
        "except": "Qualité ne devient pas qualty. Santé, côté, été et bonté ne suivent pas. Beauté devient beauty.",
    },
    {
        "fr": "-eux",
        "en": "-ous",
        "text": "Les adjectifs de caractère et de qualité. La forme féminine -euse suit le même mot anglais.",
        "pairs": [
            ("sérieux", "serious"),
            ("fameux", "famous"),
            ("dangereux", "dangerous"),
            ("nerveux", "nervous"),
            ("curieux", "curious"),
        ],
        "except": "Heureux et vieux ne suivent pas. Précieux devient precious.",
    },
    {
        "fr": "-eur",
        "en": "-or",
        "text": "À réserver aux noms de rôle et d’agent. Le mot désigne alors une personne ou une fonction.",
        "pairs": [
            ("acteur", "actor"),
            ("directeur", "director"),
            ("créateur", "creator"),
            ("professeur", "professor"),
            ("docteur", "doctor"),
        ],
        "except": "Ingénieur devient engineer. Couleur devient color. Bonheur, peur et douleur ne suivent pas.",
    },
]


class Liste(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Sans", "", 9)
        self.set_text_color(*MUTED)
        self.set_xy(18, 10)
        self.cell(0, 6, "Declika  ·  Français vers l’anglais")
        self.set_draw_color(*LINE)
        self.line(18, 17, 192, 17)
        self.set_y(22)

    def footer(self):
        self.set_y(-14)
        self.set_font("Sans", "", 9)
        self.set_text_color(*MUTED)
        self.cell(0, 8, f"{self.page_no()} / {{nb}}", align="R")


def main():
    pdf = Liste(format="A4", unit="mm")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)
    pdf.add_font("Sans", "", FONT)
    pdf.add_font("Sans", "B", FONT_B)
    pdf.add_page()

    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 48, "F")
    pdf.set_xy(18, 14)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Sans", "B", 22)
    pdf.cell(0, 10, "Declika", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(18)
    pdf.set_font("Sans", "", 12)
    pdf.cell(0, 7, "Liste complète", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(18)
    pdf.set_text_color(100, 255, 218)
    pdf.set_font("Sans", "", 11)
    pdf.cell(0, 7, "Français  →  anglais")

    pdf.set_y(60)
    pdf.set_text_color(*NAVY)
    pdf.set_font("Sans", "B", 16)
    pdf.multi_cell(0, 8, "Dix finales, de la plus fidèle à la plus fine.")
    pdf.ln(2)
    pdf.set_font("Sans", "", 11)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(
        0,
        6,
        "Tu repères la fin du mot français. Tu appliques la finale anglaise. Tu vérifies l’exception avant de conclure. "
        "La prononciation et la grammaire ne sont pas le sujet. Les paires ci-dessous sont des mots fréquents, pas une liste fermée : "
        "la règle sert à reconnaître des mots qui n’y figurent pas.",
    )
    pdf.ln(4)
    pdf.set_font("Sans", "", 11)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(
        0,
        6,
        "Ordre du document : d’abord les finales qui changent le moins, ensuite celles qui demandent une vérification.",
    )

    for index, rule in enumerate(RULES, start=1):
        if pdf.get_y() > 235:
            pdf.add_page()
        pdf.ln(8)
        y = pdf.get_y()
        pdf.set_fill_color(*NAVY)
        pdf.rect(18, y, 1.2, 8, "F")
        pdf.set_xy(22, y)
        pdf.set_font("Sans", "B", 13)
        pdf.set_text_color(*NAVY)
        pdf.cell(0, 8, f"{index:02d}    {rule['fr']}   →   {rule['en']}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_x(22)
        pdf.set_font("Sans", "", 11)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(0, 6, rule["text"])
        pdf.ln(1)
        for french, english in rule["pairs"]:
            row_y = pdf.get_y()
            pdf.set_draw_color(*LINE)
            pdf.line(22, row_y, 192, row_y)
            pdf.set_xy(22, row_y + 1.5)
            pdf.set_font("Sans", "", 11)
            pdf.set_text_color(*NAVY)
            pdf.cell(80, 7, french)
            pdf.set_text_color(*MUTED)
            pdf.cell(0, 7, english, new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(*LINE)
        pdf.line(22, pdf.get_y(), 192, pdf.get_y())
        pdf.ln(2)
        pdf.set_x(22)
        pdf.set_font("Sans", "", 10)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(0, 5, "Exceptions.  " + rule["except"])

    if pdf.get_y() > 220:
        pdf.add_page()
    pdf.ln(12)
    pdf.set_font("Sans", "B", 13)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 7, "Le geste, en lisant")
    pdf.ln(1)
    pdf.set_font("Sans", "", 11)
    pdf.set_text_color(*MUTED)
    for step in (
        "1.  Isoler la finale du mot français, pas le mot entier.",
        "2.  Appliquer la règle la plus haute dans cette liste.",
        "3.  Si le sens obtenu est absurde, regarder l’exception avant d’inventer une orthographe.",
    ):
        pdf.set_x(22)
        pdf.multi_cell(0, 6, step)
    pdf.ln(4)
    pdf.set_x(18)
    pdf.multi_cell(
        0,
        6,
        "Ce document ne promet pas des milliers de mots mémorisés en une soirée. "
        "Il sert à les reconnaître quand tu lis.",
    )

    out = Path(__file__).resolve().parents[1] / "deliverables" / "Declika-Liste-Complete.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(out)
    print(out, out.stat().st_size)
    write_carnet(out.parent)
    write_formation(out.parent)


EXERCISES = [
    ("-tion", [("solution", "solution"), ("révolution", "revolution"), ("fonction", "function")]),
    ("-isme", [("socialisme", "socialism"), ("féminisme", "feminism"), ("minimalisme", "minimalism")]),
    ("-iste", [("guitariste", "guitarist"), ("économiste", "economist"), ("fleuriste", "florist")]),
    ("-ance, -ence", [("distance", "distance"), ("conscience", "conscience"), ("absence", "absence")]),
    ("-ique", [("classique", "classic"), ("tragique", "tragic"), ("fantastique", "fantastic")]),
    ("-ie", [("philosophie", "philosophy"), ("biologie", "biology"), ("théorie", "theory")]),
    ("-aire", [("secondaire", "secondary"), ("militaire", "military"), ("contraire", "contrary")]),
    ("-té", [("identité", "identity"), ("sécurité", "security"), ("difficulté", "difficulty")]),
    ("-eux", [("furieux", "furious"), ("religieux", "religious"), ("généreux", "generous")]),
    ("-eur", [("inventeur", "inventor"), ("éditeur", "editor"), ("auteur", "author")]),
]


def write_carnet(folder: Path):
    def cell(value: str) -> str:
        if any(mark in value for mark in ",\"\n"):
            return '"' + value.replace('"', '""') + '"'
        return value

    rows = ["Français,Anglais,Règle"]
    for rule in RULES:
        for french, english in rule["pairs"]:
            rows.append(",".join(cell(part) for part in (french, english, rule["fr"])))
    path = folder / "Declika-Carnet.csv"
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(path, path.stat().st_size)


def write_formation(folder: Path):
    pdf = Liste(format="A4", unit="mm")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)
    pdf.add_font("Sans", "", FONT)
    pdf.add_font("Sans", "B", FONT_B)
    pdf.add_page()

    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 42, "F")
    pdf.set_xy(18, 12)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Sans", "B", 20)
    pdf.cell(0, 9, "Declika", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(18)
    pdf.set_font("Sans", "", 12)
    pdf.cell(0, 7, "Mini-formation  ·  1000 mots en 10 règles")

    pdf.set_y(54)
    pdf.set_text_color(*NAVY)
    pdf.set_font("Sans", "B", 14)
    pdf.multi_cell(0, 7, "Dix finales, dans l’ordre où elles rapportent.")
    pdf.ln(1)
    pdf.set_font("Sans", "", 11)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(
        0,
        6,
        "Ce n’est pas un cours d’oral. Pour chaque finale : la règle, puis trois mots à reconnaître. "
        "La réponse est juste dessous. Cache-la, réponds, puis vérifie. "
        "Le détail des exceptions est dans la liste complète.",
    )

    for index, (ending, pairs) in enumerate(EXERCISES, start=1):
        if pdf.get_y() > 240:
            pdf.add_page()
        pdf.ln(7)
        pdf.set_font("Sans", "B", 13)
        pdf.set_text_color(*NAVY)
        pdf.multi_cell(0, 7, f"{index:02d}    {ending}")
        pdf.set_x(18)
        pdf.set_font("Sans", "", 11)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(0, 6, "Reconnais la finale, puis le mot anglais.")
        for french, english in pairs:
            y = pdf.get_y()
            pdf.set_draw_color(*LINE)
            pdf.line(22, y, 192, y)
            pdf.set_xy(22, y + 1.2)
            pdf.set_text_color(*NAVY)
            pdf.cell(80, 7, french)
            pdf.set_text_color(*MUTED)
            pdf.cell(0, 7, english, new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(*LINE)
        pdf.line(22, pdf.get_y(), 192, pdf.get_y())

    pdf.ln(10)
    pdf.set_font("Sans", "", 11)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(
        0,
        6,
        "Refais le geste sur un texte. Si le mot obtenu n’a pas de sens, ouvre l’exception dans la liste. "
        "N’invente pas l’orthographe.",
    )

    path = folder / "Declika-Mini-formation.pdf"
    pdf.output(path)
    print(path, path.stat().st_size)


if __name__ == "__main__":
    main()

