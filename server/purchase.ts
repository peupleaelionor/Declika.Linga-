import { useStorage } from "nitro/storage";

export type Offer = "pdf" | "anki" | "formation" | "pack";

const FILES = {
  liste: {
    name: "Declika-Liste-Complete.pdf",
    label: "Liste complète",
    type: "application/pdf",
  },
  anki: {
    name: "Declika-Carnet.apkg",
    label: "Carnet Anki",
    type: "application/octet-stream",
  },
  csv: {
    name: "Declika-Carnet.csv",
    label: "Carnet Quizlet",
    type: "text/csv; charset=utf-8",
  },
  formation: {
    name: "Declika-Mini-formation.pdf",
    label: "Mini-formation",
    type: "application/pdf",
  },
  bonus: {
    name: "Declika-Bonus.pdf",
    label: "Bonus, faux amis",
    type: "application/pdf",
  },
} as const;

export type FileId = keyof typeof FILES;

const OFFER_FILES: Record<Offer, FileId[]> = {
  pdf: ["liste"],
  anki: ["anki", "csv"],
  formation: ["formation"],
  pack: ["liste", "anki", "csv", "formation", "bonus"],
};

const LINKS: Record<string, Offer> = {
  plink_1UdLrcBjrfvPUvltVoUaymX2: "pdf",
  plink_1UdLrGBjrfvPUvltrScd5TFz: "anki",
  plink_1UdLYZBjrfvPUvlt0KbkCFfa: "pack",
  plink_1UdNpLBjrfvPUvltUOSush4I: "formation",
};

const AMOUNTS: Record<number, Offer> = {
  1900: "pdf",
  1600: "anki",
  3900: "formation",
  5900: "pack",
};

const TITLES: Record<Offer, string> = {
  pdf: "Liste complète",
  anki: "Carnet Anki / Quizlet",
  formation: "Mini-formation",
  pack: "Pack complet",
};

export function isSessionId(value: string) {
  return /^cs_(live|test)_[A-Za-z0-9]+$/.test(value);
}

export async function readPurchase(sessionId: string) {
  const secret = process.env.STRIPE_SECRET_KEY?.trim();
  if (!secret) return { ok: false as const, reason: "unconfigured" as const };
  if (!isSessionId(sessionId)) return { ok: false as const, reason: "invalid" as const };

  const response = await fetch(
    `https://api.stripe.com/v1/checkout/sessions/${sessionId}`,
    { headers: { Authorization: `Bearer ${secret}` } },
  );
  if (!response.ok) return { ok: false as const, reason: "invalid" as const };

  const session = (await response.json()) as {
    payment_status?: string;
    amount_total?: number;
    payment_link?: string | null;
    metadata?: { offre?: string };
  };
  if (session.payment_status !== "paid") {
    return { ok: false as const, reason: "unpaid" as const };
  }

  const fromMeta = session.metadata?.offre;
  const offer =
    (fromMeta && fromMeta in OFFER_FILES ? (fromMeta as Offer) : undefined) ??
    (session.payment_link ? LINKS[session.payment_link] : undefined) ??
    (typeof session.amount_total === "number" ? AMOUNTS[session.amount_total] : undefined);

  if (!offer) return { ok: false as const, reason: "unknown" as const };

  const files = OFFER_FILES[offer].map((id) => ({
    id,
    label: FILES[id].label,
  }));
  return { ok: true as const, offer, title: TITLES[offer], files };
}

export async function readFileForPurchase(sessionId: string, fileId: string) {
  const purchase = await readPurchase(sessionId);
  if (!purchase.ok) return purchase;
  if (!(fileId in FILES) || !purchase.files.some((file) => file.id === fileId)) {
    return { ok: false as const, reason: "invalid" as const };
  }
  const file = FILES[fileId as FileId];
  const storage = useStorage();
  const key = `assets:deliverables/${file.name}`;
  const raw = (await storage.getItemRaw(key)) ?? (await storage.getItem(key));
  if (!raw) return { ok: false as const, reason: "missing" as const };
  const bytes =
    typeof raw === "string"
      ? new TextEncoder().encode(raw)
      : raw instanceof Uint8Array
        ? raw
        : new Uint8Array(raw as ArrayBuffer);
  return { ok: true as const, file, bytes };
}
