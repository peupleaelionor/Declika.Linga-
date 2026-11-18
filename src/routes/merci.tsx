import { createFileRoute } from "@tanstack/react-router";
import { Logo } from "@/components/logo";
import { contactEmail } from "@/content/site";

export const Route = createFileRoute("/merci")({
  component: Merci,
});

function Merci() {
  return (
    <main className="min-h-screen bg-paper px-5 py-16 text-ink md:px-8 md:py-24">
      <div className="mx-auto max-w-xl">
        <a href="/" aria-label="Declika, retour à l’accueil">
          <Logo className="h-8 w-auto" />
        </a>
        <h1 className="text-display mt-16">C’est payé.</h1>
        <p className="mt-8 text-pretty text-lg leading-relaxed text-muted">
          Le lien de téléchargement arrive par e-mail, envoyé par Stripe. Regarde aussi
          les courriers indésirables. Le message part dans les minutes qui suivent.
        </p>
        <ul className="mt-10 space-y-3 text-pretty">
          <li>Liste : un PDF de 17 pages.</li>
          <li>Carnet : un CSV, 222 cartes. Anki : Fichier, Importer, séparateur virgule.</li>
          <li>Formation : un PDF de 15 pages. Le corrigé est à la fin.</li>
          <li>Pack : ces trois fichiers, plus le bonus faux amis.</li>
        </ul>
        <p className="mt-10 text-pretty text-muted">
          Rien n’est une vidéo. Si le mail n’est pas là dans une heure, écris à{" "}
          <a className="font-medium text-ink underline" href={`mailto:${contactEmail}`}>
            {contactEmail}
          </a>
          .
        </p>
        <a href="/" className="btn btn-primary mt-10 w-full sm:w-auto">
          Revenir à l’accueil
        </a>
      </div>
    </main>
  );
}
