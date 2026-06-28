# user-stories.md

## Epic 1 — Continuous Non-Invasive Monitoring

### US-1.1 — Finger-prick-free spot reading
**As a** Type 2 diabetic, **I want** to take a glucose reading by holding the sensor against my skin, **so that** I can check my blood sugar without lancing my finger.
- Reading completes in ≤ 30 s from sensor contact to displayed value.
- Result shown in both mg/dL and mmol/L per user locale setting.
- Reading is rejected with a clear retry prompt if skin contact/signal quality is below threshold.
- Captured reading is timestamped and persisted to the user's history.
- **Complexity: L**

### US-1.2 — Continuous background trend tracking
**As a** Type 1 diabetic, **I want** the device to sample glucose automatically every 5 minutes while worn, **so that** I see a continuous trend rather than isolated snapshots.
- Auto-sample interval configurable (1/5/15 min); default 5 min.
- Trend line renders rolling 3 h / 6 h / 24 h windows.
- Directional arrow (rising/steady/falling) shown with rate-of-change in mg/dL/min.
- Battery sufficient for ≥ 14 h of continuous 5-min sampling on one charge.
- **Complexity: L**

### US-1.3 — Sensor confidence indicator
**As a** user, **I want** each reading labeled with a confidence/accuracy indicator, **so that** I know when to trust the value vs. confirm another way.
- Each reading tagged High / Medium / Low confidence from signal-quality model.
- Low-confidence readings visually flagged and excluded from trend smoothing.
- Tooltip explains the likely cause (motion, poor contact, temperature).
- **Complexity: M**

---

## Epic 2 — Alerts & Safety

### US-2.1 — Hypo/hyper threshold alerts
**As a** caregiver of a diabetic child, **I want** to set high and low glucose thresholds that trigger alerts, **so that** I'm warned before a dangerous excursion.
- User-configurable low (default 70 mg/dL) and high (default 180 mg/dL) thresholds.
- Alert fires within 60 s of a qualifying reading via on-device sound + push.
- Alerts repeat/escalate if unacknowledged after 5 min.
- Urgent-low (< 54 mg/dL) alert overrides silent/do-not-disturb mode.
- **Complexity: M**

### US-2.2 — Predictive low-glucose warning
**As a** Type 1 diabetic, **I want** a warning before I actually go low based on my trend, **so that** I can act before symptoms hit.
- Predictive alert triggers when projected to cross low threshold within 20 min.
- Prediction uses ≥ 30 min of recent trend data; suppressed if data insufficient.
- False-alert rate target: ≤ 1 unnecessary predictive alert per 24 h in validation.
- **Complexity: L**

### US-2.3 — Caregiver remote alerting
**As a** remote caregiver, **I want** to receive the user's critical alerts on my own phone, **so that** I can respond even when not physically present.
- User can invite/revoke up to 5 follower accounts.
- Followers receive only critical (urgent-low/high) alerts by default; configurable.
- Follower view shows latest reading + timestamp, never raw PII beyond consented scope.
- Alert delivery confirmed with read receipt back to primary user.
- **Complexity: M**

---

## Epic 3 — Calibration & Accuracy Assurance

### US-3.1 — Optional fingerstick calibration
**As a** new user, **I want** to optionally calibrate against a fingerstick reading, **so that** the AI sensor tunes to my body chemistry.
- User can enter a reference BG value with timestamp.
- System accepts calibration only when trend is stable (rate < 1 mg/dL/min).
- Post-calibration accuracy delta shown vs. pre-calibration baseline.
- Calibration history viewable and revertible.
- **Complexity: M**

### US-3.2 — Accuracy self-check & drift detection
**As a** user, **I want** the device to detect when its readings are drifting, **so that** I'm prompted to recalibrate instead of trusting bad data.
- Drift detection flags sustained divergence from expected physiological patterns.
- Prompt to recalibrate appears after drift threshold is sustained ≥ 2 readings.
- Reported MARD (mean absolute relative difference) surfaced in settings.
- **Complexity: L**

---

## Epic 4 — Data, Sharing & Insights

### US-4.1 — Logbook & report export
**As a** diabetic patient, **I want** to export my glucose history as a report, **so that** I can share it with my endocrinologist.
- Export to PDF and CSV covering a user-selected date range.
- Report includes time-in-range %, average glucose, GMI, and excursion counts.
- Export completes locally without requiring cloud upload.
- **Complexity: S**

### US-4.2 — Time-in-range dashboard
**As a** user managing my A1c, **I want** a dashboard showing time-in-range, **so that** I can gauge control at a glance.
- Displays % time below/in/above range for 24 h, 7 d, 30 d.
- Target range editable; defaults to 70–180 mg/dL.
- Color-coded ambulatory glucose profile (AGP) chart rendered.
- **Complexity: M**

### US-4.3 — Meal & activity tagging
**As a** user, **I want** to tag meals, exercise, and insulin against my trend, **so that** I can learn what drives my excursions.
- User can add timestamped tags (meal/exercise/insulin/note) on the trend view.
- Tags overlay on the glucose curve.
- Filterable summary shows average post-event glucose change per tag type.
- **Complexity: M**

### US-4.4 — Consent-gated data privacy controls
**As a** privacy-conscious user, **I want** explicit control over where my health data goes, **so that** my medical data isn't shared without my consent.
- All cloud sync is opt-in; device-only mode fully functional.
- User can view, export, and permanently delete all stored data.
- Data sharing with followers/clinicians requires per-recipient consent.
- Consent changes take effect within one sync cycle and are logged.
- **Complexity: M**

---

**Coverage:** 13 stories across 4 epics — Monitoring (3), Alerts & Safety (3), Calibration & Accuracy (2), Data/Sharing/Insights (4). Complexity mix: 3×S/M-light, 6×M, 5×L — weighted toward the sensor-accuracy and predictive-alert work that carries the most regulatory and clinical risk.