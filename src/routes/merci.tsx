import { useEffect, useState } from "react";
import { createFileRoute } from "@tanstack/react-router";
import { Logo } from "@/components/logo";
import { contactEmail } from "@/content/site";

export const Route = createFileRoute("/merci")({
  component: Merci,
});

type FileLink = { id: string; label: string };

function Merci() {
  const [session, setSession] = useState("");
  const [title, setTitle] = useState("");
  const [files, setFiles] = useState<FileLink[]>([]);
  const [mode, setMode] = useState<"wait" | "files" | "mail">("wait");

  useEffect(() => {
    const id = new URLSearchParams(window.location.search).get("session_id") ?? "";
    if (!id) {
      setMode("mail");
      return;
    }
    setSession(id);
    fetch(`/api/achat?session_id=${encodeURIComponent(id)}`)
      .then(async (response) => {
        if (!response.ok) throw new Error("unpaid");
        return response.json() as Promise<{ title: string; files: FileLink[] }>;
      })
      .then((data) => {
        setTitle(data.title);
        setFiles(data.files);
        setMode("files");
      })
      .catch(() => setMode("mail"));
  }, []);

  return (
    <main className="min-h-screen bg-paper px-5 py-16 text-ink md:px-8 md:py-24">
      <div className="mx-auto max-w-xl">
        <a href="/" aria-label="Declika, retour à l’accueil">
          <Logo className="h-8 w-auto" />
        </a>
        <h1 className="text-display mt-16">C’est payé.</h1>
        {mode === "files" ? (
          <>
            <p className="mt-8 text-pretty text-lg leading-relaxed text-muted">
              {title}. Les fichiers sont là. Le même lien part aussi par e-mail, de la part de Stripe.
            </p>
            <div className="mt-10 flex flex-col gap-3">
              {files.map((file, index) => (
                <a
                  key={file.id}
                  className={index === 0 ? "btn btn-primary w-full" : "btn btn-ghost w-full"}
                  href={`/api/fichier?session_id=${encodeURIComponent(session)}&file=${file.id}`}
                >
                  Télécharger {file.label}
                </a>
              ))}
            </div>
          </>
        ) : (
          <>
            <p className="mt-8 text-pretty text-lg leading-relaxed text-muted">
              {mode === "wait"
                ? "Vérification du paiement."
                : "Le lien de téléchargement arrive par e-mail, envoyé par Stripe. Regarde aussi les courriers indésirables. Le message part dans les minutes qui suivent."}
            </p>
            {mode === "mail" ? (
              <ul className="mt-10 space-y-3 text-pretty">
                <li>Liste : un PDF de 17 pages.</li>
                <li>Carnet : un paquet Anki et un CSV.</li>
                <li>Formation : un PDF. Le corrigé est à la fin.</li>
                <li>Pack : ces fichiers, plus le bonus faux amis.</li>
              </ul>
            ) : null}
          </>
        )}
        <p className="mt-10 text-pretty text-muted">
          Rien n’est une vidéo. Si le mail n’est pas là dans une heure, écris à{" "}
          <a className="font-medium text-ink underline" href={`mailto:${contactEmail}`}>
            {contactEmail}
          </a>
          .
        </p>
        <a href="/" className="btn btn-ghost mt-10 w-full sm:w-auto">
          Revenir à l’accueil
        </a>
      </div>
    </main>
  );
}
