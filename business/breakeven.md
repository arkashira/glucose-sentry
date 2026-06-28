Generated `breakeven.md`. Summary of the key calls I made:

- **COGS:** ~**$0.85/active user/mo** (compute-dominated by inference + weekly personalization retrain), yielding ~83% net contribution margin on the cheapest paid tier.
- **Pricing:** 3 tiers split along the regulatory line — **Trend $19** (wellness, no medical claim), **Guardian $49** (diagnosed diabetics, hypo alerts, caregiver share), **Clinic/Pro $299** (per 10-patient RPM block, billing-code export).
- **CAC:** $25–80 consumer, $1.2K–3.5K clinic, **~$65 blended**.
- **LTV:** ~$220 Trend / ~$1,176 Guardian / ~$8,100 Pro → blended consumer **~$430**, LTV:CAC ≈ 6.6x.
- **Break-even:** ~$55K/mo fixed → **~1,720 paying users** at a realistic blend.
- **Path to $10K MRR:** lead with Guardian — **~204 subscribers** (~$13K acquisition spend), with 2–3 Pro clinic blocks to de-risk the regulated path.

Two opinionated stances baked in, both flagged in the doc:
1. **Modeled the software/AI layer, not the device** — Axentx ships software; treating sensor BOM as a pass-through keeps the 85% SaaS margin intact rather than dragging it to ~35–45% hardware margin.
2. **The whole model is gated on sensor accuracy (MARD ≤ ~15%)** — no pricing or growth tactic survives a bad non-invasive signal, so I called that out as the #1 risk to spend the first $10K MRR proving.