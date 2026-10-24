# 6. Requirements Specification

Priority uses MoSCoW: **M** must, **S** should, **C** could. Every Must requirement has an acceptance criterion that can be checked by a test, a script output or a demo.

## 6.1 Functional requirements

| ID | Requirement | Priority | Acceptance criterion | Verified by |
| --- | --- | --- | --- | --- |
| FR-1 | The system loads N-BaIoT CSV files and labels them as benign or attack from the file name. | M | Folder with benign and mirai/gafgyt files loads; label counts match row counts of the files. | `test_load_folder`, `test_label_from_filename` |
| FR-2 | The system builds datasets with a given attack share (50, 20, 10, 5, 1%). | M | For ratio r and size n, the dataset has exactly round(n·r) attack rows. | `test_make_imbalanced_ratio` |
| FR-3 | The system trains Isolation Forest (on benign data only) and Random Forest. | M | Both models train and return labels 0/1 on test data. | `test_models_detect_demo_attacks` |
| FR-4 | The experiment runner saves precision, recall, F1, accuracy, latency, peak memory and model size for every model and ratio to CSV. | M | `results.csv` has one row per (model, ratio) and all metric columns. | `test_experiment_output_columns` |
| FR-5 | The dashboard shows the number of checked windows, raised alerts, recall and precision. | M | Demo: open the dashboard, the 4 numbers are visible and update when the model or ratio changes. | Manual demo, screenshot |
| FR-6 | The dashboard shows an alert feed with "true alert / false alarm / missed attack" and a filter. | M | Filter changes the visible rows. | Manual demo |
| FR-7 | The dashboard shows experiment charts (F1 and latency vs attack share). | S | Charts appear when `results/results.csv` exists. | Manual demo |
| FR-8 | The user can mark an alert as a false alarm and this is stored. | S | Marked alert stays marked after page reload. | Integration test (pre-defense 2) |
| FR-9 | The detector service scores live traffic windows from a mirrored port. | S | A test pcap replay produces alerts in the store. | Integration test (pre-defense 2) |
| FR-10 | The system groups traffic and alerts per device (IP / MAC). | S | Device list shows each device with its status. | Demo |
| FR-11 | The system sends a Telegram notification for a new alert. | S | Message arrives within 30 s of the alert. | Manual test |
| FR-12 | The experiment can apply SMOTE to the training set as an option. | C | Flag `--smote` changes the training class balance. | Unit test |
| FR-13 | Every alert shows the device name, a short plain-language explanation and a suggested action. | M | 3 users read sample alerts and can say which device and what to do. | Usability check |

## 6.2 Non-functional requirements

| ID | Requirement | Priority | Acceptance criterion |
| --- | --- | --- | --- |
| NFR-1 | Memory: the detector process fits in a 512 MB container. | M | Run in Docker with `--memory=512m` without OOM; peak memory is reported. |
| NFR-2 | Latency: scoring 1000 traffic windows takes less than 1 second on 1 CPU core. | M | `latency_ms_per_1000_rows` < 1000 in the constrained run. |
| NFR-3 | False alarms: at 5% attack share, the chosen model keeps precision ≥ 0.80 with recall ≥ 0.80 on N-BaIoT. | M | Value in results table; if not met it is reported as a finding, not hidden. |
| NFR-4 | Reproducibility: the full experiment runs with one command and a fixed random seed. | M | Two runs with the same seed give the same metrics. |
| NFR-5 | Security and privacy: no packet payloads, passwords or personal data are stored or committed. | M | Only numeric features are saved; `.gitignore` excludes data and secrets; code review. |
| NFR-6 | Portability: runs on Windows, Linux and Raspberry Pi OS with Python 3.10+. | S | Tested on at least two of them. |
| NFR-7 | Usability: a non expert understands the dashboard status in under 1 minute. | S | 3 users from interviews try the mockup and explain what they see. |
| NFR-8 | Maintainability: core modules have automated tests that pass in CI. | S | `pytest` passes; GitHub Actions workflow is green. |
| NFR-9 | False alarms: in normal home traffic the system raises at most one false alarm per week per home. | M | Replay of one week of benign traffic produces at most 1 false alert. |

## 6.3 Traceability

| Requirement | Source of the need |
| --- | --- |
| FR-1, FR-2, FR-4, NFR-3 | Research gap on imbalance (section 3, E4, E5) |
| FR-3 | Technology decision 5.2 |
| FR-5, FR-6, FR-10, FR-13, NFR-7 | Interviews U1 to U5, assumptions A1, A2 |
| FR-11, NFR-9 | Interviews (channel, acceptable false alarms), assumption A3 |
| NFR-1, NFR-2 | Constrained hardware, assumption A4, Kitsune (Pi) |
| NFR-5 | Repository rules and privacy of home users |
