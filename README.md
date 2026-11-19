# Declika

Page de vente des règles de cognats, du français vers l’anglais.

## Après le paiement

Les quatre Payment Links redirigent vers `https://declikalinga.vercel.app/merci?session_id={CHECKOUT_SESSION_ID}`.

La page affiche les boutons du produit acheté seulement si le paiement est confirmé. Il faut pour cela la variable serveur `STRIPE_SECRET_KEY` (clé secrète `sk_live_…`, pas de préfixe `VITE_`). Sans elle, l’acheteur reçoit quand même les fichiers par l’e-mail Stripe.

| Variable | Payment Link |
| --- | --- |
| `VITE_STRIPE_PDF` | `https://buy.stripe.com/9B6dR89dX4tz6Q74Ir8so02` |
| `VITE_STRIPE_ANKI` | `https://buy.stripe.com/aFaeVccq9aRXeizdeX8so01` |
| `VITE_STRIPE_FORMATION` | `https://buy.stripe.com/14AeVc61Le491vN5Mv8so03` |
| `VITE_STRIPE_PACK` | `https://buy.stripe.com/fZuaEWcq97FLdev0sb8so00` |

Le lien de la liste contient un `I` majuscule, pas un `l`. L’ancienne valeur renvoie une page Stripe introuvable.

Le nom affiché en haut du paiement est le nom public du compte (`JEVALIS`), pas le nom du produit. Stripe ne laisse pas le changer par API. Dans le tableau de bord : Paramètres → Détails de l’entreprise → nom public `Declika`, et descripteur de relevé `DECLIKA`.

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
