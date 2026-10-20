# Terms of Service — verification checklist (internal)

Inspection date: 2026-10-18. Workspace: marketing site (`plumberswebsites`) only. No application, Worker, Stripe, or D1 source in this repository.

## Evidence table

| Claim | Source | Status |
|-------|--------|--------|
| Monthly plan **$49**, billed monthly | `index.html` `#pricing` (lines ~1034–1052), FAQ ~1292–1297 | **Verified (marketing)** |
| Annual plan **$399**, billed annually | `index.html` `#pricing` (~1088–1110), FAQ ~1292–1297 | **Verified (marketing)** |
| Annual saves $189 vs 12×$49 | `index.html` pricing card (~1113–1115), FAQ ~1295–1297 | **Verified (marketing)** |
| Preview before payment; no payment required to preview | `index.html` hero, FAQ, pricing copy; `features/index.html`; `signin.html` | **Verified (marketing)** |
| Six designs; five-page site (Home, Services, Our Approach, About, Contact) | `index.html` FAQ; `features/index.html` | **Verified (marketing)** |
| Publish on address under PlumbersWebsites domain; process guides setup | `index.html` FAQ ~1307–1317 | **Verified (marketing)** |
| Example published subdomain `protonplumbing.plumberswebsites.com` | `index.html` invitation preview link | **Verified (marketing)** |
| Business info fields (name, phone, email optional, services, areas, hours, emergency) | `features/index.html` tables/lists | **Verified (marketing)** |
| No invented testimonials; uses customer-supplied details | `index.html` FAQ ~1323–1334 | **Verified (marketing)** |
| Account sign-in via email magic link; no password on described flow | `signin.html`, `signin.js` | **Verified (marketing)** |
| Magic link API `POST /api/auth/magic-link` with `accountEmail` | `signin.js` | **Verified (marketing)** |
| Sign-in link ~15 minutes, one-time use | `signin.html` success tips | **Verified (marketing)** |
| Customer app at `https://app.plumberswebsites.com` | CTAs sitewide; `signin.js` `APP_ORIGIN` | **Verified (marketing)** |
| Cloudflare Pages-style `_redirects` on marketing site | `_redirects` | **Verified (config)** |
| Automatic subscription renewal | — | **Unknown** |
| First payment timing (at checkout vs after trial) | — | **Unknown** |
| Stripe or other payment processor | — | **Unknown** (no Stripe in repo) |
| Cancellation UI, effective date, end-of-period | — | **Unknown** |
| Failed payment retries, grace period, suspension | — | **Unknown** |
| Refund rules | — | **Unknown** (`cancellation-refund.html` placeholder only) |
| Publish eligibility rules (paid status, etc.) | — | **Unknown** |
| Subdomain validation, uniqueness, assignment API | — | **Unknown** |
| Site availability after cancel or failed payment | — | **Unknown** |
| In-app profile/website update flow | — | **Unknown** |
| Account termination, takedown, deletion | — | **Unknown** |
| Acceptable-use enforcement | — | **Unknown** |
| Terms acceptance mechanism (clickwrap, checkout assent) | — | **Unknown** |
| Contracting legal entity, address, governing law | — | **Owner / legal** |
| Support/legal contact | — | **Unknown** (`contact.html` placeholder) |
| `/cancellation-refund/` canonical route | Footer links only; no `cancellation-refund/index.html` or `_redirects` entry | **Incomplete route** |

---

## A. Verified from source code

See evidence table rows marked **Verified (marketing)** or **Verified (config)**.

---

## B. Unknown because source is unavailable or insufficient

- All billing lifecycle behavior (renewal, proration, taxes, invoices, payment method storage).
- Payment processor identity and checkout UX.
- Cancellation, refunds, and statutory withdrawal rights (no policy content in repo).
- Publishing gate, DNS/subdomain provisioning, and post-subscription site state.
- Customer website editing after publish; export or portability.
- Service-initiated suspension/termination criteria and timelines.
- Record of terms acceptance.
- Application session management beyond magic-link request behavior.

**Limitation:** Comments in `signin.js` reference `worker/cors.ts` but that Worker code is not present in this workspace.

---

## C. Owner decisions and legal review required

| Item | Evidence needed |
|------|-----------------|
| Contracting legal entity and address | Company registration, letterhead, Stripe account entity |
| Governing law, jurisdiction, dispute resolution | Legal counsel instruction |
| Confirm $49 / $399 remain current list prices | Pricing source of truth (Stripe Products/Prices) |
| Auto-renewal disclosures and consent | Stripe subscription settings + checkout copy |
| Cancellation mechanics and effective date | App UI + Stripe Customer Portal / API behavior |
| Refunds and mandatory consumer rights | Business policy + applicable law |
| Published site when subscription ends | Worker/D1 + hosting rules |
| IP: customer content vs platform templates/designs | Legal + product definition |
| Suspension/termination policy | Internal ops + app enforcement |
| Limitation of liability and indemnity | Legal draft with jurisdiction review |
| Terms change notice process | Product + email practices |
| Verified support/legal contact | Published contact page or support email |
| Terms acceptance mechanism | Checkout/account flow screenshots + logs |

Do not treat any row as verified without inspecting the application and billing implementation repositories.
