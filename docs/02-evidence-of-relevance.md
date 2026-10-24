# 2. Evidence of Relevance

This section separates what is **verified** (backed by a source or by an interview) from what is still an **assumption**.

## 2.1 Evidence from published sources (verified)

| # | Finding | Source |
| --- | --- | --- |
| E1 | Mirai infected hundreds of thousands of IoT devices (cameras, DVRs, routers) mainly through default telnet passwords and was used for record DDoS attacks. | Antonakakis et al. (2017) |
| E2 | Ordinary commercial devices (doorbell, baby monitor, webcams, thermostat) can be infected in a lab and their traffic changes in a way that ML can detect. | Meidan et al. (2018) |
| E3 | IoT attack datasets are still being built because older ones do not cover enough devices and attacks; CICIoT2023 uses 105 real devices and 33 attacks. | Neto et al. (2023) |
| E4 | Surveys of IoT anomaly detection point to a lack of evaluation under realistic, real world conditions. | Cook et al. (2019); DeMedeiros et al. (2023); Fährmann et al. (2024) |
| E5 | Some high accuracy results are reached only after the training data was balanced with oversampling, while real smart home traffic is much more skewed. | Choukhairi et al. (2026) |

## 2.2 Interviews with potential users

Five people from the target group (home users with smart devices) answered the same 6 questions in writing on 24 October 2026. Questions and full answers: [interviews/interviews-2026-10-24.md](interviews/interviews-2026-10-24.md). Guide: [interviews/interview-guide.md](interviews/interview-guide.md).

Limitation: all five are home users from the student's own circle; small office users are not covered yet (planned for the next stage).

## 2.3 Summary of interview findings

| Code | Devices | Checked what devices send? | Strange behaviour | Alert format and channel | Acceptable false alarms | Hardware |
| --- | --- | --- | --- | --- | --- | --- |
| U1 | Smart TV, speaker, robot vacuum | No | TV slow to connect | Explanation of the problem, Telegram | Once a month | Box near router |
| U2 | Wi-Fi camera, TV, smart plugs | No | Camera turns off by itself | Explanation, phone push | Once a week | Program on PC |
| U3 | Speaker, Android TV | No | None | Short alert, details on demand, Telegram | Once a week | Box near router |
| U4 | Robot vacuum, Smart TV, smart bulbs | No | Vacuum loses connection | Device, what happened, what to do; phone push | Once a month | Program on PC |
| U5 | Security camera, speaker, PS5 | No | Camera stopped working in app | Device name and explanation, Telegram | Once a week at most | Box near router |

Main findings:

- **5 of 5** never checked what their devices send to the internet.
- **4 of 5** saw connection problems or devices behaving oddly, but could not tell whether it was a technical fault or something else. Nobody had a tool to check.
- **5 of 5** want to know **which device** has a problem; 4 of 5 also want a short **explanation**, and U4 also wants to know **what to do**.
- Channel: Telegram (3), phone push notification (2).
- False alarms: once a week at most (3), once a month (2). Two users said frequent false alarms would make them ignore the system.
- Hardware: box near the router (3), program on a computer (2). Users who chose the box said it must work automatically.

## 2.4 Assumptions and how they were checked

| # | Assumption | Status after interviews | Evidence |
| --- | --- | --- | --- |
| A1 | Home owners do not know what their IoT devices send over the network. | **Verified** | 5 of 5 never checked (Q2) |
| A2 | Users want a simple "normal / suspicious" signal, not technical logs. | **Partly verified, changed** | Users want the device name plus a short explanation and advice, not only a status (Q4) |
| A3 | Users accept a few false alarms per week but not per day. | **Verified, made stricter** | Nobody accepts daily false alarms; 2 of 5 want at most one per month (Q5) |
| A4 | A Raspberry Pi class box or a program on an existing PC is acceptable. | **Verified, both needed** | 3 prefer a box, 2 prefer a PC program (Q6) |
| A5 | In real homes attack traffic is a small share of all traffic. | Supported by literature (E4, E5), not measured by us | Experiment with 1 to 50% attack share |
| A6 | Small offices have the same needs as homes. | Not verified | Planned interviews with 1 to 2 office IT people |

## 2.5 How the evidence shapes the requirements

- E1, E2 → the detector must work per device and on network features only (FR-1, FR-2).
- E4, E5 → the evaluation must include imbalanced data and not only a 50/50 split (FR-8, section 9).
- A1, A2 → alerts must name the device and explain the problem in plain words with a suggested action (FR-5, FR-13).
- A3 → false alarm limit of at most one per week per home in normal use (NFR-9); this also supports the focus on precision under imbalance.
- A4 → the detector must run both on a Raspberry Pi class box and as a Docker container on a normal PC (NFR-1, NFR-2, NFR-6).
- Channel answers → Telegram notification moved from Could to Should (FR-11).
