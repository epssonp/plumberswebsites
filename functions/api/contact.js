const CONTACT_TO = "contact@plumberswebsites.com";
const MAX_NAME = 120;
const MAX_EMAIL = 254;
const MAX_SUBJECT = 200;
const MAX_MESSAGE = 5000;
const MIN_MESSAGE = 10;

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

function isValidEmail(value) {
  if (typeof value !== "string" || value.length === 0 || value.length > MAX_EMAIL) {
    return false;
  }
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

function sanitizeText(value, maxLength) {
  if (typeof value !== "string") {
    return "";
  }
  return value.trim().slice(0, maxLength);
}

async function verifyTurnstile(token, secret, remoteip) {
  const body = new URLSearchParams({
    secret,
    response: token,
  });
  if (remoteip) {
    body.set("remoteip", remoteip);
  }

  const response = await fetch(
    "https://challenges.cloudflare.com/turnstile/v0/siteverify",
    {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body,
    }
  );

  if (!response.ok) {
    return { success: false };
  }

  return response.json();
}

function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

async function sendViaResend(env, payload) {
  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return { ok: false, reason: "not_configured" };
  }

  const from =
    env.RESEND_FROM || `PlumbersWebsites.com <${CONTACT_TO}>`;
  const subjectLine =
    payload.subject ||
    `Contact form: ${payload.name}`;

  const text = [
    "New message from the PlumbersWebsites.com contact form.",
    "",
    `Name: ${payload.name}`,
    `Email: ${payload.email}`,
    payload.subject ? `Subject: ${payload.subject}` : "Subject: (none)",
    "",
    payload.message,
  ].join("\n");

  const html = `
    <p>New message from the PlumbersWebsites.com contact form.</p>
    <p><strong>Name:</strong> ${escapeHtml(payload.name)}</p>
    <p><strong>Email:</strong> ${escapeHtml(payload.email)}</p>
    <p><strong>Subject:</strong> ${escapeHtml(payload.subject || "(none)")}</p>
    <p><strong>Message:</strong></p>
    <p>${escapeHtml(payload.message).replace(/\n/g, "<br>")}</p>
  `.trim();

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from,
      to: [CONTACT_TO],
      reply_to: payload.email,
      subject: subjectLine,
      text,
      html,
    }),
  });

  if (!response.ok) {
    return { ok: false, reason: "delivery_failed" };
  }

  return { ok: true };
}

export async function onRequest(context) {
  const { request, env } = context;

  if (request.method === "GET") {
    return jsonResponse({
      turnstileSiteKey: env.TURNSTILE_SITE_KEY || null,
    });
  }

  if (request.method !== "POST") {
    return jsonResponse({ error: "Method not allowed." }, 405);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ error: "Invalid request." }, 400);
  }

  const honeypot = sanitizeText(body.company_website, 200);
  if (honeypot) {
    return jsonResponse({ ok: true });
  }

  const name = sanitizeText(body.name, MAX_NAME);
  const email = sanitizeText(body.email, MAX_EMAIL);
  const subject = sanitizeText(body.subject, MAX_SUBJECT);
  const message = sanitizeText(body.message, MAX_MESSAGE);

  if (!name) {
    return jsonResponse({ error: "Please enter your name." }, 400);
  }
  if (!isValidEmail(email)) {
    return jsonResponse({ error: "Please enter a valid email address." }, 400);
  }
  if (message.length < MIN_MESSAGE) {
    return jsonResponse(
      { error: "Please enter a message (at least 10 characters)." },
      400
    );
  }

  const turnstileSecret = env.TURNSTILE_SECRET_KEY;
  if (turnstileSecret) {
    const token = sanitizeText(body.turnstileToken, 2048);
    if (!token) {
      return jsonResponse({ error: "Please complete the verification check." }, 400);
    }

    const ip =
      request.headers.get("CF-Connecting-IP") ||
      request.headers.get("X-Forwarded-For") ||
      "";
    const verification = await verifyTurnstile(token, turnstileSecret, ip);
    if (!verification.success) {
      return jsonResponse({ error: "Verification failed. Please try again." }, 403);
    }
  }

  const delivery = await sendViaResend(env, { name, email, subject, message });
  if (!delivery.ok) {
    if (delivery.reason === "not_configured") {
      return jsonResponse(
        {
          error:
            "The contact form is not configured yet. Please email us directly at contact@plumberswebsites.com.",
        },
        503
      );
    }
    return jsonResponse(
      {
        error:
          "We could not send your message. Please try again or email contact@plumberswebsites.com directly.",
      },
      502
    );
  }

  return jsonResponse({ ok: true });
}
