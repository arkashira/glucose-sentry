Generated `tech-spec.md` for **glucose-sentry** (v1).

Key opinionated calls baked in:

- **De-risked scope** — v1 ships the *software platform* (ingest + AI inference + dashboard + alerting), treating the non-invasive sensor as an external signal source. Wellness/"not-for-diagnosis" framing keeps us off the FDA/CE critical path while we prove the AI and UX.
- **Stack** — FastAPI (async streaming ingest) + PyTorch→ONNX CPU serving; Next.js dashboard; Postgres + **TimescaleDB** hypertables for the time-series.
- **Hosting** — $0/mo at 0–50 devices (Fly + Neon + Upstash + Vercel + R2); explicit upgrade triggers.
- **Data model** — separates `signal_frames` (raw) from derived `glucose_readings`, with `calibrations` driving per-user personalization and `model_versions` enabling instant rollback.
- **Security/PHI** — mTLS + per-device keys for ingest, JWT + Postgres RLS for users, append-only audit log, field-level encryption — HIPAA/GDPR-ready before clearance.
- **CI safety gate** — a `model-eval` job that **fails the build if MARD regresses >2%**, so accuracy can't silently degrade.

Two things worth flagging for downstream chain steps (architect/validation):
1. The hardware/sensor accuracy is the real product risk — this spec deliberately assumes frames arrive; whoever owns the sensor partnership/BOM needs a separate spec.
2. Market data came through empty (`{}`), so pricing/competitive positioning isn't reflected here — that belongs in the business-model section, not the tech spec.