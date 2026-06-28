Generated `partner-targets.md`. Summary of the roadmap:

**8 partners, revenue-share ranked first:**

| Priority signal | Partner | Why |
|---|---|---|
| 🥇 Highest rev-share | Validic (#8) | Payer PMPM, $2–8/member/mo at scale |
| 🥈 | Healthie/Spruce (#5) | RPM CPT codes reimburse ~$50–60/patient/mo |
| 🥉 Immediate margin | Terra (#2), Nutritionix/Edamam (#7) | Affiliate/reseller margin, fast to ship |
| Cost-recovery | Stripe (#3), Twilio (#4) | Small referral %, but table-stakes |

**Sequencing logic:** Phase 0 = monetize + alert (S effort — Stripe/Twilio), Phase 1 = context + stickiness (M — Terra, HealthKit, food DBs), Phase 2 = clinical reimbursement (L — Dexcom, Healthie, Validic).

**The one thing I'd escalate to PRD:** the entire high-LTV tier (Validic, RPM) is gated on FDA/clinical device classification. If glucose-sentry ships as "wellness estimation" rather than a cleared diagnostic, those rev-share partners need a *trend/insight* framing, not *diagnostic*. That classification decision should be resolved before any Phase 2 engineering is committed — it's the single biggest blocker to the real money.

I also flagged **Terra (#2) as the highest-leverage single build** — one API unlocks ~300 wearables plus the contextual data your AI model needs.