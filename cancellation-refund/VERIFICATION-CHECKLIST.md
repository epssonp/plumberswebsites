# Cancellation & Refund Policy — verification checklist (internal)

Inspection date: 2026-10-18. Workspace: marketing site only. No Stripe, Worker, D1, or customer-app billing source in this repository.

## Evidence table

| Claim | Source | Status |
|-------|--------|--------|
| Monthly plan **$49**, billed monthly | `index.html` `#pricing` (~1044–1052), FAQ (~1292–1294) | **Verified (marketing)** |
| Annual plan **$399**, billed annually | `index.html` `#pricing` (~1103–1110), FAQ (~1293–1294) | **Verified (marketing)** |
| Preview before payment; payment after plan selection | `index.html` FAQ, pricing copy | **Verified (marketing)** |
| Published site under PlumbersWebsites domain | `index.html` FAQ ~1307–1317 | **Verified (marketing)** |
| Customer app sign-in | `https://app.plumberswebsites.com/sign-in` sitewide | **Verified (marketing)** |
| Automatic subscription renewal | — | **Unknown** |
| Initial charge timing | — | **Unknown** |
| Stripe product/price IDs | — | **Unknown** |
| Cancellation workflow (UI, URL, Customer Portal) | — | **Unknown** |
| Cancellation effective date (immediate vs period end) | — | **Unknown** |
| Refund eligibility, windows, partial refunds | — | **Unknown** |
| Refund request process and processing time | — | **Unknown** |
| Statutory withdrawal/cooling-off handling | — | **Owner / legal** |
| Failed payment retries (Stripe settings) | — | **Unknown** |
| Grace period before suspension | — | **Unknown** |
| Webhook-driven subscription status | — | **Unknown** |
| When publish is enabled/disabled | — | **Unknown** |
| Site online after cancel / expiry / failed payment | — | **Unknown** |
| Account/content access after cancel | — | **Unknown** |
| Subdomain release or retention | — | **Unknown** |
| Billing/support contact email | — | **Unknown** (`contact.html` placeholder) |
| Contracting legal entity | — | **Owner / legal** |

---

## Verified from the marketing repository

- **Plans and advertised prices:** $49/month (billed monthly) and $399/year (billed annually) in homepage pricing section and FAQ.
- **Product context:** Subscription follows website preview; publishing described as separate steps under PlumbersWebsites domain.
- **Account access:** Sign-in via customer application; no cancellation instructions in marketing HTML.

---

## Unknown because implementation is unavailable

Investigate in application + billing repositories (not present here):

- Stripe Products, Prices, Checkout Sessions, Customer Portal, and refund API usage.
- Whether subscriptions are `subscription` mode with auto-renewal and which billing anchor applies.
- First payment moment (checkout completion vs trial).
- In-app or Stripe-hosted cancellation path and whether cancel is at period end or immediate.
- Configured refund policy in Stripe Dashboard vs custom logic in Worker.
- `invoice.payment_failed`, retry schedule, dunning, and account/site suspension hooks.
- D1 or equivalent fields for `subscription_status`, `publish_enabled`, `site_live`.
- Jobs or webhooks that unpublish sites or revoke DNS/subdomain.
- Data export, profile edit access, and retention after subscription ends.
- Subdomain pool: reserved names, cooldown, reuse rules.

**Note:** `signin.js` references a Worker (`worker/cors.ts`) but Worker code is outside this repo.

---

## Owner decisions and legal review

| Decision | Why it cannot be inferred from marketing code |
|----------|-----------------------------------------------|
| Intended refund policy (none, pro-rata, 14-day, etc.) | Business policy + Stripe configuration |
| Cancellation effective date policy | Product + Stripe + consumer law |
| Post-cancel published site behavior | Product/ops choice + implementation |
| Subdomain retention after cancel | Product + DNS implementation |
| Mandatory rights (EU/UK withdrawal, US state laws) | Legal entity location + customer base |
| Legal business name and address on policy | Not published in repo |
| Verified billing support contact | Contact page incomplete |
| Approved effective date | Not approved |
| Alignment with draft Terms §5 and Privacy payment section | Cross-document review after facts known |

Do not mark any billing lifecycle item **verified** without code or Stripe Dashboard evidence.
