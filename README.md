# Declika

Page de vente des règles de cognats, du français vers l’anglais.

## Déployer sur Vercel

1. Importer ce dépôt : [github.com/peupleaelionor/Declika.Linga-](https://github.com/peupleaelionor/Declika.Linga-).
2. Laisser la commande de build sur `npm run build`.
3. Avant le déploiement qui doit encaisser, ajouter ces variables d’environnement, puis redéployer. Vite les lit au moment du build.

| Variable | Payment Link Stripe |
| --- | --- |
| `VITE_STRIPE_PDF` | Liste PDF complète |
| `VITE_STRIPE_ANKI` | Carnet Anki / Quizlet |
| `VITE_STRIPE_FORMATION` | Mini-formation |
| `VITE_STRIPE_PACK` | Pack complet |

Chaque valeur est une URL `https://buy.stripe.com/…` ou `https://checkout.stripe.com/…`.

Dans Stripe, pour chaque Payment Link :

1. Joindre le fichier de l’offre. Il part par e-mail après le paiement. Ne le publie pas sur le site.
2. Après le paiement, rediriger vers `https://TON-DOMAINE/merci`.

| Offre | Fichier à joindre |
| --- | --- |
| Liste PDF | `deliverables/Declika-Liste-Complete.pdf` |
| Carnet Anki / Quizlet | `deliverables/Declika-Carnet.apkg` et `deliverables/Declika-Carnet.csv` |
| Mini-formation | `deliverables/Declika-Mini-formation.pdf` |
| Pack | les trois fichiers ci-dessus, plus `deliverables/Declika-Bonus.pdf` |

Anki : ouvrir le `.apkg`. Quizlet : importer le CSV, séparateur virgule, colonnes Français / Anglais / Règle.

Coller l’URL du Payment Link dans Vercel, pas dans le code. Redéployer après avoir ajouté les variables : Vite les lit au moment du build.

Sans ces variables, les boutons d’achat ramènent à la section Tarifs. Ils ne pointent pas vers un faux paiement.

`DATABASE_URL` n’est pas nécessaire pour cette page.
