import { useEffect, useState } from "react";
import { ArrowRight, Check, Menu, X } from "lucide-react";
import { Logo } from "@/components/logo";
import { Reveal } from "@/components/reveal";
import {
  comments,
  contactEmail,
  euros,
  faq,
  products,
  rules,
  upcomingLanguages,
} from "@/content/site";

const nav = [
  { href: "#methode", label: "La méthode" },
  { href: "#produits", label: "Produits" },
  { href: "#tarifs", label: "Tarifs" },
];

function BuyLink({
  href,
  children,
  variant = "primary",
  className = "",
}: {
  href: string;
  children: string;
  variant?: "primary" | "ghost";
  className?: string;
}) {
  const external = href.startsWith("http");
  return (
    <a
      href={href}
      className={`btn btn-${variant} ${className}`}
      {...(external ? { rel: "noopener noreferrer" } : {})}
    >
      {children}
    </a>
  );
}

function Header() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (!open) return;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") setOpen(false);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <header className="sticky top-0 z-30 border-b border-line bg-paper">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between gap-4 px-5 md:h-20 md:px-8">
        <a href="#haut" className="shrink-0" aria-label="Declika, retour en haut">
          <Logo className="h-7 w-auto md:h-8" />
        </a>

        <nav className="hidden items-center gap-8 md:flex" aria-label="Sections">
          {nav.map((item) => (
            <a
              key={item.href}
              href={item.href}
              className="text-sm font-medium text-ink/80 hover:text-ink"
            >
              {item.label}
            </a>
          ))}
        </nav>

        <div className="flex items-center gap-2">
          <a href="#tarifs" className="btn btn-primary px-4 sm:px-5">
            <span className="sm:hidden">Accès</span>
            <span className="hidden sm:inline">Obtenir l’accès</span>
          </a>
          <button
            type="button"
            className="grid size-11 place-items-center rounded-full border border-line md:hidden"
            aria-expanded={open}
            aria-controls="menu-mobile"
            aria-label={open ? "Fermer le menu" : "Ouvrir le menu"}
            onClick={() => setOpen((value) => !value)}
          >
            {open ? <X className="size-5" aria-hidden /> : <Menu className="size-5" aria-hidden />}
          </button>
        </div>
      </div>

      {open ? (
        <nav id="menu-mobile" className="border-t border-line px-5 py-3 md:hidden" aria-label="Sections">
          {nav.map((item) => (
            <a
              key={item.href}
              href={item.href}
              className="flex min-h-11 items-center text-base font-medium"
              onClick={() => setOpen(false)}
            >
              {item.label}
            </a>
          ))}
        </nav>
      ) : null}
    </header>
  );
}

function Specimen() {
  const rule = rules[1];

  return (
    <div className="rounded-2xl border border-line bg-card p-8 shadow-sheet md:p-10">
      <div className="flex items-baseline justify-between gap-4 text-sm font-medium text-muted">
        <p>Règle {rule.index} · extrait</p>
        <p>FR → EN</p>
      </div>
      <div className="mt-10 flex flex-wrap items-center gap-4">
        <p className="text-4xl font-semibold tracking-tight sm:text-5xl">-té</p>
        <span className="grid size-12 shrink-0 place-items-center rounded-full bg-mint text-ink" aria-hidden>
          <ArrowRight className="size-5" strokeWidth={2.25} />
        </span>
        <p className="text-4xl font-semibold tracking-tight sm:text-5xl">-ty</p>
      </div>
      <p className="mt-6 max-w-sm text-pretty text-muted">{rule.text}</p>
      <ul className="mt-8 divide-y divide-line border-t border-line">
        {rule.pairs.map(([fr, en]) => (
          <li key={fr} className="flex items-baseline justify-between gap-6 py-3">
            <span className="font-medium">{fr}</span>
            <span className="text-muted">{en}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function ProductCard({
  product,
}: {
  product: (typeof products)[number];
}) {
  const navy = product.tone === "navy";
  const cover = product.id === "pdf";
  const savings =
    "compareAt" in product && product.compareAt ? product.compareAt - product.price : 0;

  return (
    <article
      id={product.id}
      className={
        navy
          ? "on-navy flex h-full flex-col rounded-2xl bg-navy p-8 text-paper ring-2 ring-mint md:p-10"
          : "flex h-full flex-col rounded-2xl border border-line bg-card p-8 md:p-10"
      }
    >
      <div className={cover ? "grid h-full items-start gap-8 sm:grid-cols-[11.5rem_1fr]" : "flex h-full flex-col"}>
        {cover ? (
          <img
            src="/declika-guide.jpg"
            alt="Guide PDF Declika, couverture"
            width={1083}
            height={943}
            className="w-full max-w-44 justify-self-center rounded-lg shadow-sheet"
          />
        ) : null}
        <div className="flex h-full min-w-0 flex-col">
          <p
            className={
              navy
                ? "w-fit rounded-full bg-mint px-3 py-1 text-sm font-semibold text-ink"
                : "text-sm font-medium text-muted"
            }
          >
            {product.eyebrow}
          </p>
          <h3 className="mt-5 text-balance text-2xl font-semibold tracking-tight md:text-3xl">
            {product.title}
          </h3>
          <p className={navy ? "mt-4 text-pretty text-paper/75" : "mt-4 text-pretty text-muted"}>
            {product.description}
          </p>
          <ul className="mt-8 space-y-3">
            {product.benefits.map((benefit) => (
              <li key={benefit} className="flex gap-3">
                <Check
                  className={navy ? "mt-1 size-4 shrink-0 text-mint" : "mt-1 size-4 shrink-0"}
                  strokeWidth={2}
                  aria-hidden
                />
                <span className={navy ? "text-paper/90" : undefined}>{benefit}</span>
              </li>
            ))}
          </ul>
          <div className="mt-auto pt-10">
            <p className="flex items-baseline gap-3">
              <span className="text-4xl font-semibold tracking-tight tabular-nums">
                {euros(product.price)}
              </span>
              {savings > 0 ? (
                <s className="text-base text-paper/70 tabular-nums">{euros(product.compareAt!)}</s>
              ) : null}
            </p>
            {savings > 0 ? (
              <p className="mt-2 text-sm font-semibold text-mint">
                Économise {euros(savings)} par rapport aux produits séparés
              </p>
            ) : null}
            <p className={navy ? "mt-1 text-sm text-paper/75" : "mt-1 text-sm text-muted"}>
              Paiement unique
            </p>
            <BuyLink
              href={product.checkout}
              className={navy ? "btn-emphasis mt-6 w-full" : "mt-6 w-full"}
            >
              {product.cta}
            </BuyLink>
          </div>
        </div>
      </div>
    </article>
  );
}

const quiz = [
  {
    prompt: "Quelle terminaison anglaise correspond généralement à « -té » en français ?",
    options: ["-ty", "-tion", "-ous"],
    answer: 0,
  },
  {
    prompt: "« -tion » en français devient souvent quoi en anglais ?",
    options: ["-tion", "-ty", "-ous"],
    answer: 0,
  },
  {
    prompt: "« -eux » devient généralement :",
    options: ["-ous", "-ty", "-tion"],
    answer: 0,
  },
] as const;

const quizNote =
  "C’est exactement le type de règle que tu trouves dans la liste complète (10 règles + exceptions).";

function MethodQuiz({ checkout }: { checkout: string }) {
  const [step, setStep] = useState(0);
  const [picked, setPicked] = useState<number | null>(null);
  const question = quiz[step];
  const answered = picked !== null;
  const correct = picked === question.answer;
  const last = step === quiz.length - 1;

  return (
    <div className="mt-16 max-w-2xl rounded-2xl border border-line bg-paper p-6 md:p-8">
      <p className="text-sm font-medium text-muted">
        Question {step + 1} sur {quiz.length}
      </p>
      <h3 className="mt-3 text-2xl font-semibold tracking-tight">Teste la méthode</h3>
      <p className="mt-6 text-pretty text-lg font-medium">{question.prompt}</p>
      <div className="mt-6 grid gap-3 sm:grid-cols-3" role="group" aria-label={question.prompt}>
        {question.options.map((option, index) => {
          const isAnswer = index === question.answer;
          const isPicked = index === picked;
          const tone = answered && isAnswer
            ? "border-ink bg-mint"
            : answered && isPicked
              ? "border-ink bg-card"
              : "border-line bg-card hover:border-ink";
          return (
            <button
              key={option}
              type="button"
              disabled={answered}
              onClick={() => setPicked(index)}
              aria-pressed={isPicked}
              className={`min-h-12 rounded-xl border px-4 py-3 text-left text-base font-semibold ${tone}`}
            >
              {option}
              {answered && isAnswer ? <span className="sr-only">, bonne réponse</span> : null}
            </button>
          );
        })}
      </div>
      {answered ? (
        <div className="mt-6">
          <p className="font-medium">
            {correct
              ? `Oui. C’est « ${question.options[question.answer]} ».`
              : `Non. C’est « ${question.options[question.answer]} ».`}
          </p>
          <p className="mt-2 max-w-xl text-pretty text-muted">{quizNote}</p>
          {last ? (
            <BuyLink href={checkout} className="mt-6 w-full sm:w-auto">
              Obtenir la liste complète
            </BuyLink>
          ) : (
            <button
              type="button"
              className="btn btn-ghost mt-6 w-full sm:w-auto"
              onClick={() => {
                setStep((value) => value + 1);
                setPicked(null);
              }}
            >
              Question suivante
            </button>
          )}
        </div>
      ) : null}
    </div>
  );
}

function LanguageCard({ language }: { language: string }) {
  const [open, setOpen] = useState(false);
  const [done, setDone] = useState(false);
  const id = `alerte-${language}`;

  return (
    <li className="flex flex-col rounded-xl border border-line bg-card px-4 py-4">
      <div className="flex items-center justify-between gap-2">
        <p className="font-medium">{language}</p>
        <p className="shrink-0 rounded-full border border-line px-2 py-0.5 text-xs font-medium text-muted">
          Bientôt
        </p>
      </div>
      {done ? (
        <p className="mt-4 text-sm text-muted">C’est noté.</p>
      ) : open ? (
        <form
          className="mt-4 flex flex-col gap-2"
          onSubmit={(event) => {
            event.preventDefault();
            setDone(true);
          }}
        >
          <label htmlFor={id} className="sr-only">
            E-mail pour {language}
          </label>
          <input
            id={id}
            name="email"
            type="email"
            required
            autoComplete="email"
            placeholder="ton@email.fr"
            className="h-11 w-full rounded-lg border border-line bg-paper px-3 text-sm outline-none"
          />
          <button type="submit" className="btn btn-ghost min-h-11 w-full px-3 text-sm">
            Envoyer
          </button>
        </form>
      ) : (
        <button
          type="button"
          className="btn btn-ghost mt-4 min-h-11 w-full px-3 text-sm"
          onClick={() => setOpen(true)}
        >
          M’avertir
        </button>
      )}
    </li>
  );
}

export function LandingPage() {
  const pdf = products[0];
  const pack = products[1];
  const rest = products.slice(2);

  return (
    <div id="haut" className="min-h-screen bg-paper text-ink">
      <a href="#contenu" className="skip-link">
        Aller au contenu
      </a>
      <Header />
      <main id="contenu">
        <section className="relative overflow-hidden">
          <div
            aria-hidden
            className="hero-glow"
          />
          <div className="relative mx-auto grid max-w-6xl items-center gap-16 px-5 py-24 md:grid-cols-12 md:px-8 md:py-32">
            <div className="md:col-span-7">
              <p className="inline-flex items-center gap-2 text-sm font-medium">
                <span className="size-1.5 rounded-full bg-mint" aria-hidden />
                La méthode qui explose le vocabulaire
              </p>
              <h1 className="text-display mt-6 max-w-3xl">
                Les règles qui te font gagner des milliers de mots
              </h1>
              <p className="mt-6 max-w-xl text-pretty text-lg leading-relaxed text-muted">
                Declika te donne les règles simples de cognats pour passer du français à
                l’anglais (et bientôt d’autres langues) en quelques secondes.
              </p>
              <div className="mt-10 flex flex-col gap-3 sm:flex-row">
                <BuyLink href={pdf.checkout} className="w-full sm:w-auto">
                  {pdf.cta}
                </BuyLink>
                <a href="#methode" className="btn btn-ghost w-full sm:w-auto">
                  Voir la méthode
                </a>
              </div>
              <p className="mt-5 text-sm text-muted">
                Liste complète · {euros(pdf.price)} · paiement unique
              </p>
            </div>
            <div className="md:col-span-5">
              <img
                src="/hero-mark.png"
                alt=""
                width={480}
                height={475}
                className="mb-8 w-40 md:w-52"
              />
              <Specimen />
            </div>
          </div>
        </section>

        <section id="produits" className="scroll-mt-24 px-5 py-24 md:px-8 md:py-32">
          <div className="mx-auto max-w-6xl">
            <Reveal>
              <p className="text-sm font-medium text-muted">Offres</p>
              <h2 className="text-title mt-4 max-w-2xl">
                Un principe, quatre formats
              </h2>
              <p className="mt-5 max-w-2xl text-pretty text-lg text-muted">
                Le PDF porte la méthode. Le carnet la fait répéter. La formation la met
                en ordre. Le pack réunit les trois.
              </p>
            </Reveal>

            <div id="tarifs" className="scroll-mt-24 mt-16 grid gap-6 lg:grid-cols-12">
              <Reveal className="lg:col-span-7">
                <ProductCard product={pdf} />
              </Reveal>
              <Reveal className="lg:col-span-5" delay={0.06}>
                <ProductCard product={pack} />
              </Reveal>
              {rest.map((product, index) => (
                <Reveal key={product.id} className="lg:col-span-6" delay={0.08 + index * 0.05}>
                  <ProductCard product={product} />
                </Reveal>
              ))}
            </div>

            <Reveal>
              <aside className="mt-6 flex flex-col gap-4 rounded-2xl border border-line bg-card px-8 py-7 md:flex-row md:items-center md:justify-between md:px-10">
                <div className="max-w-2xl">
                  <p className="text-sm font-medium text-muted">Application</p>
                  <h3 className="mt-2 text-2xl font-semibold tracking-tight">Bientôt sur téléphone</h3>
                  <p className="mt-3 text-pretty text-muted">
                    La même méthode, sans document à ouvrir. Elle n’est pas en vente.
                    Les quatre formats ci-dessus le sont.
                  </p>
                </div>
                <p className="text-sm font-semibold">Bientôt</p>
              </aside>
            </Reveal>
          </div>
        </section>

        <section id="methode" className="scroll-mt-24 border-y border-line bg-card">
          <div className="mx-auto max-w-6xl px-5 py-24 md:px-8 md:py-32">
            <Reveal>
              <p className="text-sm font-medium text-muted">La méthode</p>
              <h2 className="text-title mt-4 max-w-2xl">
                Trois finales. Le principe est là.
              </h2>
              <p className="mt-5 max-w-2xl text-pretty text-lg text-muted">
                Une terminaison française indique la terminaison anglaise. En voici
                trois. La liste complète en tient dix, exceptions comprises.
              </p>
            </Reveal>

            <div className="mt-16 grid gap-12 md:grid-cols-3 md:gap-10">
              {rules.map((rule, index) => (
                <Reveal key={rule.index} delay={index * 0.05}>
                  <article className="border-t border-ink pt-6">
                    <p className="text-sm font-medium text-muted">{rule.index}</p>
                    <h3 className="mt-4 text-2xl font-semibold tracking-tight">{rule.title}</h3>
                    <p className="mt-3 text-pretty text-muted">{rule.text}</p>
                    <ul className="mt-8 divide-y divide-line border-t border-line">
                      {rule.pairs.map(([fr, en]) => (
                        <li key={fr} className="flex items-baseline justify-between gap-4 py-3">
                          <span className="font-medium">{fr}</span>
                          <span className="text-muted">{en}</span>
                        </li>
                      ))}
                    </ul>
                  </article>
                </Reveal>
              ))}
            </div>
            <p className="mt-12 max-w-2xl text-sm text-muted">
              « Qualité » ne devient pas « qualty ». Une règle ouvre la famille ; le PDF
              marque les écarts d’orthographe.
            </p>
            <MethodQuiz checkout={pdf.checkout} />
            <img
              src="/methode-croissance.jpg"
              alt="Apprendre la règle, l’appliquer, puis relier les finales. La reconnaissance progresse."
              width={1375}
              height={829}
              className="mt-16 w-full"
            />
          </div>
        </section>

        <section className="px-5 py-24 md:px-8 md:py-32" aria-labelledby="retours-title">
          <div className="mx-auto grid max-w-6xl gap-12 md:grid-cols-12 md:gap-16">
            <Reveal className="md:col-span-5">
              <img
                src="/communaute.jpg"
                alt="Silhouettes de lecteurs reliées par les mêmes règles"
                width={925}
                height={431}
                className="w-full max-w-md"
              />
              <p className="mt-8 text-sm font-medium text-muted">Lecteurs</p>
              <h2 id="retours-title" className="text-title mt-4">
                En quelques mots
              </h2>
              <p className="mt-5 text-pretty text-lg text-muted">
                Trois retours, après le PDF ou le carnet.
              </p>
            </Reveal>
            <div className="md:col-span-7">
              <ul className="divide-y divide-line border-y border-line">
                {comments.map((comment, index) => (
                  <Reveal key={comment.handle} delay={index * 0.04}>
                    <li className="grid gap-3 py-8 md:grid-cols-[9.5rem_1fr] md:gap-10">
                      <div>
                        <p className="font-medium">{comment.handle}</p>
                        <p className="text-sm text-muted">{comment.time}</p>
                      </div>
                      <p className="text-pretty text-lg leading-relaxed">{comment.text}</p>
                    </li>
                  </Reveal>
                ))}
              </ul>
            </div>
          </div>
        </section>

        <section id="faq" className="scroll-mt-24 px-5 pb-24 md:px-8 md:pb-32" aria-labelledby="faq-title">
          <div className="mx-auto max-w-3xl">
            <Reveal>
              <p className="text-sm font-medium text-muted">Questions</p>
              <h2
                id="faq-title"
                className="text-title mt-4"
              >
                Avant d’acheter
              </h2>
            </Reveal>
            <div className="mt-10 border-t border-line">
              {faq.map((item) => (
                <details key={item.q} className="border-b border-line">
                  <summary className="flex list-none items-center justify-between gap-6 py-6 text-lg font-medium">
                    {item.q}
                    <span className="faq-plus grid size-8 shrink-0 place-items-center text-2xl font-light leading-none" aria-hidden>
                      +
                    </span>
                  </summary>
                  <p className="max-w-2xl pb-6 text-pretty leading-relaxed text-muted">{item.a}</p>
                </details>
              ))}
            </div>
          </div>
        </section>

        <section className="on-navy bg-navy text-paper">
          <div className="mx-auto max-w-6xl px-5 py-24 md:px-8 md:py-32">
            <Reveal>
              <h2 className="text-title max-w-3xl">
                Les règles tiennent en quelques pages. Le vocabulaire qu’elles ouvrent, non.
              </h2>
              <div className="mt-10 flex flex-col gap-3 sm:flex-row">
                <BuyLink href={pdf.checkout} className="w-full sm:w-auto">
                  {pdf.cta}
                </BuyLink>
                <BuyLink href={pack.checkout} variant="ghost" className="w-full sm:w-auto">
                  {pack.cta}
                </BuyLink>
              </div>
            </Reveal>
          </div>
        </section>

        <section className="border-t border-line px-5 py-16 md:px-8 md:py-20" aria-labelledby="avenir-title">
          <div className="mx-auto max-w-6xl">
            <h2 id="avenir-title" className="text-2xl font-semibold tracking-tight">
              L’avenir de Declika
            </h2>
            <p className="mt-3 max-w-xl text-pretty text-muted">
              L’anglais est notre point de départ. D’autres langues arrivent.
            </p>
            <ul className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
              {upcomingLanguages.map((language) => (
                <LanguageCard key={language} language={language} />
              ))}
            </ul>
          </div>
        </section>
      </main>

      <footer className="border-t border-line px-5 py-12 md:px-8">
        <div className="mx-auto flex max-w-6xl flex-col gap-10 md:flex-row md:items-end md:justify-between">
          <div>
            <Logo className="h-8 w-auto" />
            <p className="mt-4 max-w-sm text-pretty text-sm text-muted">
              Cognats, du français vers l’anglais. Le même principe est prévu pour
              d’autres langues.
            </p>
          </div>
          <div className="flex flex-col gap-6 sm:flex-row sm:items-end sm:gap-16">
            <nav className="flex flex-col gap-2 text-sm" aria-label="Pied de page">
              <a href="#methode" className="hover:underline">
                La méthode
              </a>
              <a href="#produits" className="hover:underline">
                Produits
              </a>
              <a href="#tarifs" className="hover:underline">
                Tarifs
              </a>
              <a href="#faq" className="hover:underline">
                Questions
              </a>
            </nav>
            <div className="text-sm text-muted">
              <a className="font-medium text-ink hover:underline" href={`mailto:${contactEmail}`}>
                {contactEmail}
              </a>
              <p className="mt-2">© 2026 Declika</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
