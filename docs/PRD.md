# Product Requirements Document – **glucose‑sentry**

---

## 1. Executive Summary

**glucose‑sentry** is a non‑invasive, AI‑powered blood‑sugar monitoring system that eliminates finger‑pricks and blood samples. Leveraging advanced optical/thermal sensors and on‑device inference (vLLM), the device continuously tracks glucose levels and delivers actionable insights to users and clinicians via a companion mobile app.

---

## 2. Problem Statement

- **High user friction**: Current glucose monitoring requires daily finger‑pricks, causing pain, inconvenience, and low adherence.
- **Fragmented data**: Users manually log readings, leading to incomplete datasets and sub‑optimal care decisions.
- **Limited accessibility**: Many patients lack continuous monitoring due to cost, device complexity, or lack of integration with care teams.

---

## 3. Target Users

| Persona | Pain Points | Desired Outcomes |
|---------|-------------|------------------|
| **Diabetic patients (type 1 & 2)** | Painful finger‑pricks, inconsistent logging, anxiety over hypoglycemia | Continuous, painless glucose tracking; real‑time alerts; data sync with EHR |
| **Caregivers & family members** | Difficulty monitoring loved ones, lack of actionable data | Remote monitoring dashboard, trend alerts, shareable reports |
| **Healthcare providers** | Incomplete patient data, time‑consuming chart reviews | Integrated glucose logs in EHR, predictive analytics, automated alerts |
| **Health‑tech startups** | Need for validated, low‑cost monitoring solutions | API access, SDK for custom apps, compliance with HIPAA/CE |

---

## 4. Goals & Success Metrics

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Accuracy** | Mean Absolute Error (MAE) vs. reference meter | < 5 mg/dL (≈ 0.3 mmol/L) |
| **User Adoption** | Monthly active users (MAU) | 10 k by Q4 2026 |
| **Clinical Validation** | FDA 510(k) clearance | Completed by Q2 2027 |
| **Data Integration** | % of readings synced to EHR | ≥ 95 % |
| **Revenue** | Unit sales | $2 M ARR by end of 2027 |

---

## 5. Key Features (Prioritized)

| # | Feature | Description | Priority | Dependencies |
|---|---------|-------------|----------|--------------|
| 1 | **Non‑invasive sensor suite** | Optical/thermal sensors + AI model (vLLM) to infer glucose | Must‑have | Hardware design, sensor calibration |
| 2 | **On‑device inference** | Real‑time glucose prediction with < 200 ms latency | Must‑have | vLLM integration, edge GPU |
| 3 | **Continuous monitoring** | 24/7 data capture with adaptive sampling | Must‑have | Battery optimization, firmware |
| 4 | **Mobile companion app** | iOS/Android app for viewing trends, alerts, sharing | Must‑have | Backend API, UI/UX |
| 5 | **EHR integration** | HL7/FHIR export, secure data sync | Should‑have | Compliance, API gateway |
| 6 | **Predictive alerts** | Hypo/Hyperglycemia risk scoring, trend analysis | Should‑have | ML model, user settings |
| 7 | **Data analytics dashboard** | For clinicians & caregivers | Nice‑to‑have | BI tooling, role‑based access |
| 8 | **Regulatory compliance** | HIPAA, CE, FDA 510(k) | Must‑have | Documentation, QA |
| 9 | **Battery & form factor** | < 8 h standby, wearable form | Must‑have | Power management |
|10 | **Firmware OTA updates** | Secure over‑the‑air updates | Nice‑to‑have | OTA infrastructure |

---

## 6. Scope

### In‑Scope

- Design & prototype of sensor hardware (optical/thermal).
- Development of AI inference pipeline using vLLM.
- Firmware for continuous data acquisition and edge inference.
- Mobile app (iOS/Android) with real‑time dashboards.
- Backend services: data ingestion, storage, analytics, EHR export.
- Regulatory documentation and testing for FDA 510(k) and CE.
- Initial pilot study with 50 users for clinical validation.

### Out‑of‑Scope

- Manufacturing of mass‑production hardware (handled by partner).
- Integration with non‑standard EHR systems beyond HL7/FHIR.
- Advanced AI features (e.g., personalized diet recommendations) beyond glucose prediction.
- Non‑US regulatory approvals (e.g., MDR in EU) beyond CE marking.

---

## 7. Technical Architecture

```
[Sensor Array] --> [Embedded MCU + Edge GPU] --> [vLLM Inference] --> [Local Storage]
          |                                               |
          +---> [Bluetooth Low Energy] --+--> [Mobile App] --+--> [Backend API]
                                         |                         |
                                         +--> [Cloud Storage] ----+--> [Analytics Engine]
```

- **Edge inference** uses vLLM for low‑latency predictions.
- **BLE** for secure data sync to mobile app.
- **Backend** built on AWS (Lambda, DynamoDB, SageMaker) with HIPAA‑compliant data lake.
- **Analytics** layer uses Spark for trend analysis and alert generation.

---

## 8. Milestones & Timeline

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| Prototype hardware | 2026‑07 | Functional sensor board |
| Firmware beta | 2026‑08 | Continuous sampling + inference |
| Mobile app MVP | 2026‑09 | Dashboard + alerts |
| Pilot study start | 2026‑10 | 50 users, data collection |
| FDA 510(k) submission | 2027‑01 | Complete documentation |
| CE marking | 2027‑02 | Certification |
| Commercial launch | 2027‑04 | Mass‑production handoff |

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Sensor calibration drift | Accuracy loss | Periodic calibration protocol, OTA firmware updates |
| Regulatory delays | Launch delay | Early engagement with FDA/EMA, dedicated compliance team |
| Battery life < 8 h | User churn | Optimize sampling rate, low‑power components |
| Data privacy breach | Legal penalties | End‑to‑end encryption, strict access controls |

---

## 10. Success Criteria

- **Accuracy**: MAE < 5 mg/dL in 90 % of readings.
- **User retention**: > 70 % of pilot users continue after 3 months.
- **Clinical adoption**: At least 3 hospitals integrate glucose‑sentry data into their EHR.
- **Revenue**: $2 M ARR within 12 months post‑launch.

---

## 11. Appendices

- **Glossary**: AI, vLLM, HL7, FHIR, 510(k), CE, etc.
- **Compliance Checklist**: HIPAA, GDPR, ISO 13485.
- **Reference Architecture Diagrams** (internal wiki link).

---

*Prepared by:*  
Senior Product & Engineering Lead, Axentx  
Date: 2026‑06‑17
