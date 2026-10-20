# Privacy Policy — verification checklist (internal)

Last updated with marketing-repo inspection: 2026-10-18.

Status key: **Verified** | **Documented (marketing copy)** | **Unknown**

## Legal identity and contact

| Item | Status | Notes |
|------|--------|-------|
| Registered legal entity name | Unknown | Footer uses “PlumbersWebsites.com” only |
| Company registration / address | Unknown | Not in repository |
| Privacy contact email or postal address | Unknown | `/contact/` is placeholder |
| Data Protection Officer | Unknown | |
| Country of incorporation | Unknown | |
| Approved policy effective date | Unknown | Draft uses “last revised” only |

## Product and data categories

| Item | Status | Notes |
|------|--------|-------|
| Account email for sign-in | Verified | `signin.html`, `signin.js`, homepage CTAs |
| Magic link API path | Verified | `POST` `https://app.plumberswebsites.com/api/auth/magic-link` with `accountEmail` |
| Sign-in link ~15 min / one-time use | Documented | `signin.html` success tips |
| No password on described sign-in flow | Documented | `signin.html`, marketing copy |
| Uniform response for magic-link requests | Documented | `signin.html` privacy note |
| Business profile fields | Documented | `features/index.html` table; homepage FAQ |
| Six designs, five pages | Documented | Homepage FAQ |
| Preview before paid plan | Documented | Homepage, Features, About |
| Pricing $49/mo, $399/yr | Documented | Homepage FAQ |
| Published URL under PlumbersWebsites domain | Documented | Homepage FAQ; demo subdomain on homepage |
| Customer app origin | Verified | `https://app.plumberswebsites.com` |

## Automatic collection, cookies, analytics

| Item | Status | Notes |
|------|--------|-------|
| Marketing `script.js` | Verified | Mobile menu only; no analytics |
| Third-party analytics on marketing pages | Not found | No gtag/plausible/etc. in inspected HTML/JS |
| Cloudflare Pages hosting | Documented | `_redirects` format; not wrangler in repo |
| Edge/server logs (IP, UA) | Unknown | Expected for any host; retention not verified |
| App/session cookies | Unknown | Magic-link POST uses `credentials: 'omit'` (`signin.js`); app sessions not in repo |

## Backend, payments, email (app / worker)

| Item | Status | Notes |
|------|--------|-------|
| Worker name, D1 database | Unknown | Not in this repository |
| Email provider (e.g. Resend) | Unknown | |
| Stripe / checkout flow | Unknown | No Stripe references in repo |
| Stored payment metadata | Unknown | |
| Token/session retention | Unknown | |
| Account deletion workflow | Unknown | |

## Sharing, security, retention, rights

| Item | Status | Notes |
|------|--------|-------|
| Subprocessor list | Partial | Hosting/app inferred; names unverified |
| Encryption / certifications | Unknown | |
| Retention periods | Unknown | |
| GDPR / US state law applicability | Unknown | Pending legal entity and processing map |
| Privacy request procedure | Unknown | |
