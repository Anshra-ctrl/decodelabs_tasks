# Phishing Awareness Analysis: Fake UAE Flag Day AED 200 Gift

Project 3, DecodeLabs Cyber Security Internship | Written by Anshra | Date of analysis: 1 November 2026

This is an analysis of a phishing message that was circulating on WhatsApp ahead of UAE Flag Day. It claimed that the UAE President was giving away AED 200 to everyone. I examined the link without opening it, listed the red flags, concluded it was malicious, and reported it. I completed this work as part of Project 3 of the cybersecurity internship at DecodeLabs.

## The message I analysed

A friend forwarded me a WhatsApp message claiming that the sender had "just received" a gift of AED 200 from the President, along with a link to claim it. My friend was only forwarding it, so I did not consider her a suspect. This is how mass phishing typically spreads: through people you trust, which makes you less cautious.

| | |
| --- | --- |
| Channel | WhatsApp |
| Claim | Everyone in the UAE receives AED 200 for Flag Day |
| Domain | `vjusb[.]buzz` |
| My verdict | Malicious (phishing) |
| Action | Block the domain and escalate. I reported it to the Abu Dhabi Police and the domain's registrar. |

## 1. Suspicious links and keywords

| What I found | Why it is suspicious |
| --- | --- |
| The domain `vjusb[.]buzz` | It is a `.buzz` address, not a `.gov.ae` or `.ae` one, so it is not a government site. |
| Domain registered on 31 October 2026 | It was one day old when I scanned it on 1 November. A government campaign would not launch on a brand-new domain. |
| The owner is hidden behind a privacy service | There is no way to see who runs the site. |
| TLS certificate issued on 1 November 2026 | The certificate was issued on the same day as my scan, so the site was set up just before the campaign. |
| `s=wa` in the URL | The link was built to be shared through WhatsApp. |
| Page title: "Everyone can receive AED 200 as a special gift to celebrate UAE Flag Day!" | A free money offer for everyone. |
| Button text: "Tap here to get it now" | A single call to action with no other information on the page. |
| Message text: "I just received mine!" | A fear-of-missing-out hook. |

Keywords to watch for: "AED 200", "gift", "everyone", "just received", "Tap here to get it now".

## 2. Red flags

1. **Brand and authority impersonation.** The page displayed du and e& logos, a photo of the President, and UAE flag imagery. Telecom logos have no reason to appear on a government payment.
2. **A free money offer.** Money for everyone, tied to an occasion, is the "greed" trigger in social engineering.
3. **A non-government domain.** A `.buzz` address was used for an offer that claims to come from the government.
4. **Brand-new infrastructure.** The domain was one day old, and the certificate was issued on the day of my scan.
5. **Social pressure.** I scanned it two days before Flag Day (3 November). The message claimed someone had already received the money.
6. **Built to spread.** The `s=wa` tag shows it was designed for WhatsApp forwards.
7. **Hiding behind Cloudflare.** All 5 IP addresses belonged to Cloudflare (AS13335), which hides the server. The scan showed the location as Ascension Island, which is just a Cloudflare artefact and says nothing about where the operator is actually based.
8. **A single-page app.** The page was built with Vue.js. The real destination of the button is loaded by script and is not visible in the plain HTML.

## 3. Why the message is unsafe

Each sign is weak on its own. Together, they point to phishing: a new domain, a new certificate, brand logos used without permission, and an offer that no real government would make through a forwarded link.

I did not visit the destination page, so what it wanted is an assessment, not something I saw. Pages of this type usually try to collect Emirates ID details, card numbers, or OTP codes, or direct victims into survey chains and ask them to share the link so that it spreads further.

The important lesson here was that urlscan.io returned the result "No classification" and Google Safe Browsing did not flag the domain. That does not mean the site is safe. Reputation systems lag behind campaigns by hours or days, and scammers exploit that gap. I reached my conclusion from the evidence itself: domain age, certificate date, brand abuse, hosting, and the nature of the offer.

## 4. Triage decision

Every message ends in one action: Safe means close it, Suspicious means warn the user, and Malicious means block the domain and escalate.

| Outcome | Action | This message |
| --- | --- | --- |
| Safe | Close | |
| Suspicious | Warn the user | |
| Malicious | Block the domain and escalate | **Yes** |

I advised my friend to delete the message, not to share it, and to contact her bank if she had entered any details.

## 5. Pause, Verify, Report

- **Pause:** I did not forward the message, and I did not open the link in a browser.
- **Verify:** I submitted the URL to urlscan.io for scanning and then checked the domain's WHOIS record. I also compared the message with how real UAE announcements are made, through official channels such as WAM and u.ae.
- **Report:** I filed a report through the Abu Dhabi Police portal (Aman service), indicating that no money was lost. I also reported the domain to its registrar, Spaceship, at 19:50 UTC on 1 November 2026, and received an automatic reply.

At the time of writing, both reports were still pending. I plan to rescan the URL to see how long it takes to go offline, and to report it through urlscan.io, Google Safe Browsing, and Cloudflare's abuse form.

## Evidence

I have written the indicators in defanged form (`hxxps` and `[.]`) so that nobody clicks them by accident.

| Type | Value |
| --- | --- |
| Domain | `vjusb[.]buzz` |
| URL | `hxxps://vjusb[.]buzz/dqWfbAJEcU/5772&s=wa&t=1793560536&` |
| Registered | 31 October 2026 (expires 31 October 2027) |
| Registrar | Spaceship, Inc. (IANA ID 3862) |
| TLS certificate | Issued 1 November 2026 by WE1, valid for 3 months |
| Main IP at scan | `104[.]21[.]46[.]181` (Cloudflare) |
| Delivery channel | WhatsApp |
| Page statistics | 36 requests, 7 domains, 5 IPs, 286 kB, 0 cookies |
| Scan | [urlscan.io result](https://urlscan.io/result/01a19891-6ed3-7089-8a86-db181ba38a20/) |

## What I learned

- A lack of warnings from automated tools does not mean a link is safe, especially for a brand-new domain.
- I should confirm details with a second source. urlscan.io tagged the page "5h old", but that only reflected when it was first seen. The WHOIS record gave the actual registration date.
- A Cloudflare address and a hidden owner do not reveal who runs the site. The most useful actions were reporting to the registrar and to Cloudflare.
- Scams exploit events and trusted people. I should evaluate the channel, not the forwarded message itself.

## Limitations

- I analysed a single message. This is a single case study, not a collection of samples.
- I did not open the destination page, so I cannot say for certain what data it requested.
- The takedown reports were still pending at the time of writing.

## Tools used

urlscan.io, a WHOIS lookup, the Abu Dhabi Police Aman portal, and a registrar abuse report.
