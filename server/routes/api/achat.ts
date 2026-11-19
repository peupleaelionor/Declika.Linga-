import { defineHandler, getRequestURL } from "h3";
import { readPurchase } from "../../purchase";

export default defineHandler(async (event) => {
  const sessionId = getRequestURL(event).searchParams.get("session_id") ?? "";
  const purchase = await readPurchase(sessionId);
  if (!purchase.ok) {
    const status = purchase.reason === "unconfigured" ? 503 : 403;
    return new Response(JSON.stringify({ ok: false }), {
      status,
      headers: { "content-type": "application/json" },
    });
  }
  return new Response(
    JSON.stringify({ ok: true, title: purchase.title, files: purchase.files }),
    { headers: { "content-type": "application/json", "cache-control": "no-store" } },
  );
});
