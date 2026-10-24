# 2. Evidence of Relevance

This section separates what is **verified** (backed by a source or by an interview) from what is still an **assumption**. Interviews with potential users are being collected now; the table in 2.3 will be filled in as they are done.

## 2.1 Evidence from published sources (verified)

| # | Finding | Source |
| --- | --- | --- |
| E1 | Mirai infected hundreds of thousands of IoT devices (cameras, DVRs, routers) mainly through default telnet passwords and was used for record DDoS attacks. | Antonakakis et al. (2017) |
| E2 | Ordinary commercial devices (doorbell, baby monitor, webcams, thermostat) can be infected in a lab and their traffic changes in a way that ML can detect. | Meidan et al. (2018) |
| E3 | IoT attack datasets are still being built because older ones do not cover enough devices and attacks; CICIoT2023 uses 105 real devices and 33 attacks. | Neto et al. (2023) |
| E4 | Surveys of IoT anomaly detection point to a lack of evaluation under realistic, real world conditions. | Cook et al. (2019); DeMedeiros et al. (2023); Fährmann et al. (2024) |
| E5 | Some high accuracy results are reached only after the training data was balanced with oversampling, while real smart home traffic is much more skewed. | Choukhairi et al. (2026) |

## 2.2 Interviews with potential users (in progress)

Plan: 3 to 5 short interviews (10 to 15 minutes) with people from the target groups:

- 2 to 3 home owners with at least 3 smart devices (camera, smart speaker, plugs, robot vacuum, etc.)
- 1 to 2 people responsible for IT in a small office or a shop

Interview guide: [interviews/interview-guide.md](interviews/interview-guide.md). Notes of each interview are saved in `docs/interviews/` (no real names, only a role and a code like U1, U2).

## 2.3 Summary of interview findings

| Code | Role | Devices | Key points | Status |
| --- | --- | --- | --- | --- |
| U1 | | | | pending |
| U2 | | | | pending |
| U3 | | | | pending |

## 2.4 Assumptions and how they will be checked

| # | Assumption | Status | How it will be checked |
| --- | --- | --- | --- |
| A1 | Home owners do not know what their IoT devices send over the network. | Not verified | Interview questions Q4 to Q6 |
| A2 | Users want a simple "normal / suspicious" signal, not technical logs. | Not verified | Interview questions Q8 to Q10 |
| A3 | Users accept a few false alarms per week but not per day. | Not verified | Interview question Q11; used for NFR on false positive rate |
| A4 | A small box (Raspberry Pi class) or a Docker container on an existing PC is acceptable hardware. | Not verified | Interview question Q12 |
| A5 | In real homes attack traffic is a small share of all traffic (well below 50%). | Supported by literature (E4, E5), not measured by us | Experiment with 1 to 50% attack share |

## 2.5 How the evidence shapes the requirements

- E1, E2 → the detector must work per device and on network features only (FR-1, FR-2).
- E4, E5 → the evaluation must include imbalanced data and not only a 50/50 split (FR-8, section 9).
- A2, A3 → the dashboard must show a clear status and the false alarm rate is a non-functional requirement (FR-5, NFR-3).
- A4 → memory and latency limits (NFR-1, NFR-2).
