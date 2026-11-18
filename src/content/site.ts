/**
 * Textes, prix et liens Declika.
 * Les URL de paiement viennent des variables Vercel :
 * VITE_STRIPE_PDF, VITE_STRIPE_ANKI, VITE_STRIPE_FORMATION, VITE_STRIPE_PACK
 * (Payment Links https://buy.stripe.com/… ou Checkout https://checkout.stripe.com/…).
 * Sans variable, le bouton renvoie à la section tarifs.
 */

export const contactEmail = "bonjour@declika.com";

function stripeLink(value: string | undefined): string {
  const url = value?.trim() ?? "";
  if (/^https:\/\/(buy|checkout)\.stripe\.com\/[A-Za-z0-9/_-]{4,}(\?[A-Za-z0-9=&_%.-]*)?$/.test(url)) {
    return url;
  }
  return "#tarifs";
}

export const checkout = {
  pdf: stripeLink(import.meta.env.VITE_STRIPE_PDF),
  anki: stripeLink(import.meta.env.VITE_STRIPE_ANKI),
  formation: stripeLink(import.meta.env.VITE_STRIPE_FORMATION),
  pack: stripeLink(import.meta.env.VITE_STRIPE_PACK),
};

export const prices = {
  pdf: 19,
  anki: 16,
  formation: 39,
  pack: 59,
} as const;

const separateTotal = prices.pdf + prices.anki + prices.formation;

export const rules = [
  {
    index: "01",
    title: "-tion reste -tion",
    text: "La finale la plus stable. Le mot français se reconnaît presque tel quel.",
    pairs: [
      ["éducation", "education"],
      ["nation", "nation"],
      ["attention", "attention"],
    ],
  },
  {
    index: "02",
    title: "-té devient -ty",
    text: "La finale change, le sens reste. Le PDF signale les écarts d’orthographe.",
    pairs: [
      ["liberté", "liberty"],
      ["qualité", "quality"],
      ["société", "society"],
    ],
  },
  {
    index: "03",
    title: "-eur devient -or",
    text: "Les noms de rôle et d’agent basculent d’une lettre. Les exceptions sont à part.",
    pairs: [
      ["acteur", "actor"],
      ["directeur", "director"],
      ["créateur", "creator"],
    ],
  },
] as const;

export const products = [
  {
    id: "pdf",
    eyebrow: "Offre principale",
    title: "Liste PDF complète",
    description:
      "Dix finales, les écarts, et les mots fréquents. Un document dense, fait pour être relu.",
    benefits: [
      "Dix finales, de la plus fidèle à la plus fine",
      "Paires français → anglais, classées par règle",
      "Les exceptions, isolées, pour ne pas brouiller le geste",
    ],
    price: prices.pdf,
    cta: "Obtenir la liste complète",
    checkout: checkout.pdf,
    tone: "light" as const,
  },
  {
    id: "pack",
    eyebrow: "Meilleure offre",
    title: "Pack complet",
    description:
      "Le PDF, le carnet et la mini-formation. Un seul paiement, les trois formats, sans rien laisser de côté.",
    benefits: [
      "Tout ce que Declika vend aujourd’hui",
      "Bonus inclus : faux amis et lectures annotées",
      "Un seul paiement",
    ],
    price: prices.pack,
    compareAt: separateTotal,
    cta: "Obtenir le pack",
    checkout: checkout.pack,
    tone: "navy" as const,
  },
  {
    id: "anki",
    eyebrow: "Révision",
    title: "Carnet Anki / Quizlet",
    description:
      "Les mêmes paires que le PDF, rangées par règle, prêtes à importer. Le document explique. Le carnet fait répéter.",
    benefits: [
      "Un paquet prêt pour Anki",
      "Le même paquet pour Quizlet",
      "Cartes rangées par finale, pas par ordre alphabétique",
    ],
    price: prices.anki,
    cta: "Obtenir le carnet",
    checkout: checkout.anki,
    tone: "light" as const,
  },
  {
    id: "formation",
    eyebrow: "Parcours",
    title: "Mini-formation « 1000 mots en 10 règles »",
    description:
      "Dix finales, dans l’ordre où elles rapportent le plus, avec des exercices de reconnaissance. Ce n’est pas un cours d’oral.",
    benefits: [
      "Un ordre de lecture, pas une pile de fiches",
      "Des exercices courts, sur des mots nouveaux",
      "Le même geste, à refaire en lisant un texte",
    ],
    price: prices.formation,
    cta: "Obtenir la formation",
    checkout: checkout.formation,
    tone: "light" as const,
  },
];

export const comments = [
  {
    label: "En lisant",
    text: "Société, qualité, liberté : trois mots, une finale. On les reconnaît sans s’arrêter sur chacun.",
  },
  {
    label: "Au carnet",
    text: "Vingt cartes, toutes sur -té. L’ordre alphabétique ne sert pas : les cartes suivent la règle.",
  },
  {
    label: "Aux exceptions",
    text: "Sans la page des exceptions, « qualité » devient « qualty ». Le PDF marque l’écart.",
  },
] as const;

export const upcomingLanguages = ["Japonais", "Allemand", "Espagnol", "Italien", "Swahili"] as const;

export const faq = [
  {
    q: "Faut-il déjà parler anglais ?",
    a: "Non. Tu pars du français que tu connais. Les finales indiquent le mot anglais. La prononciation et la grammaire ne sont pas le sujet.",
  },
  {
    q: "En quoi est-ce différent d’une liste de vocabulaire ?",
    a: "Une liste se retient mot à mot. Ici, une finale ouvre une famille. Tu réappliques la même règle à des mots qui ne figurent pas dans le document.",
  },
  {
    q: "« Des milliers de mots », c’est littéral ?",
    a: "C’est le stock réel de cognats entre le français et l’anglais, pas un objectif de mémorisation en une soirée. Les règles servent à les reconnaître en lisant.",
  },
  {
    q: "Le carnet reprend-il le PDF ?",
    a: "Oui. Les mêmes paires, triées par règle, prêtes pour Anki et pour Quizlet. Le PDF explique le geste. Le carnet le répète.",
  },
  {
    q: "Que couvre la mini-formation ?",
    a: "Dix finales, dans un ordre qui compte, avec des exercices de reconnaissance. Tu n’y apprendras pas à tenir une conversation.",
  },
  {
    q: "Comment reçoit-on les fichiers ?",
    a: "Juste après le paiement, par un lien de téléchargement. Selon l’offre : le PDF, les cartes, la formation, ou les trois. Le tout se lit sur téléphone et sur ordinateur.",
  },
  {
    q: "L’application est-elle incluse dans le pack ?",
    a: "Non. L’application n’est pas en vente. Le pack contient le PDF, le carnet, la mini-formation et le bonus faux amis. Rien d’autre.",
  },
  {
    q: "Et si le format ne me convient pas ?",
    a: `Écris à ${contactEmail} sous 14 jours. La demande est lue, et le fichier non utilisé est remboursé.`,
  },
] as const;

export function euros(amount: number) {
  return `${amount}\u00A0€`;
}
