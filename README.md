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

Dans Stripe : Produits → Payment Links, un lien par offre, téléchargement du fichier après paiement. Coller l’URL dans Vercel, pas dans le code.

Sans ces variables, les boutons d’achat ramènent à la section Tarifs. Ils ne pointent pas vers un faux paiement.

`DATABASE_URL` n’est pas nécessaire pour cette page.
