import { defineHandler, getRequestURL } from "h3";
import { readFileForPurchase } from "../../purchase";

export default defineHandler(async (event) => {
  const url = getRequestURL(event);
  const sessionId = url.searchParams.get("session_id") ?? "";
  const fileId = url.searchParams.get("file") ?? "";
  const result = await readFileForPurchase(sessionId, fileId);
  if (!result.ok) {
    return new Response("Indisponible", { status: result.reason === "unconfigured" ? 503 : 403 });
  }
  return new Response(new Uint8Array(result.bytes), {
    headers: {
      "content-type": result.file.type,
      "content-disposition": `attachment; filename="${result.file.name}"`,
      "cache-control": "private, no-store",
    },
  });
});
