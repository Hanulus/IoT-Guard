# IoT-Guard

Lightweight machine learning based anomaly and intrusion detection for smart home and small office IoT networks.

Diploma project, Software Engineering, Astana IT University (2026–2027).

## About the project

Smart home devices (cameras, doorbells, plugs, baby monitors) are easy targets for botnets like Mirai, and their owners usually have no way to notice that a device was hacked. Research papers report 95 to 99% detection accuracy for IoT intrusion detection, but mostly on balanced lab datasets and powerful machines. In a real home attacks are rare and the detector has to run on cheap hardware.

IoT-Guard watches the traffic of IoT devices, detects unusual behaviour with lightweight models and shows simple alerts to the owner. The research part measures **how class imbalance changes the detection quality and the resource cost** of such a detector on constrained hardware.

| | |
| --- | --- |
| **Problem** | Home and small office owners cannot tell when an IoT device is compromised; published detectors are evaluated on unrealistic, balanced data |
| **Target users** | Home owners with smart devices, small offices without a security team; researchers as a secondary group |
| **Expected outcomes** | Working detector + dashboard, reproducible imbalance experiment, recommendations for a home setup |
| **Research question** | How does class imbalance in IoT traffic data affect the accuracy and resource efficiency of a lightweight anomaly detection model on resource-constrained smart home hardware? |

## Team

| Role | Name | Responsibility |
| --- | --- | --- |
| Student | Chingiz Uraimov ([Hanulus](https://github.com/Hanulus)), SE-2405 | Individual project: research, design, implementation, testing, documentation |
| Supervisor | Abzal Kyzyrkanov ([abzzall](https://github.com/abzzall)) | Supervision and review of key deliverables |

## Scope

In scope: network traffic features (no payloads), public datasets N-BaIoT and CICIoT2023, Isolation Forest and Random Forest, web dashboard, resource measurement in Docker and on Raspberry Pi.
Out of scope: deep packet inspection, automatic blocking on the router, large GPU models. Details: [docs/01](docs/01-project-proposal.md#scope).

## Current status (pre-defense 1, 24 Oct 2026)

| Part | Status |
| --- | --- |
| Analysis and design documents (sections 1 to 11) | Done, see the table below |
| Data loader, imbalance sampling, two detectors, experiment runner | Implemented, 7 unit tests pass |
| Dashboard prototype (Streamlit) | Working in demo mode |
| Experiments on real N-BaIoT data | Next step (DIP-14) |
| User interviews | Done: 5 written interviews, findings used in requirements (DIP-4) |
| Live traffic capture, alert store, API | Planned for pre-defense 2 |

## Documentation

| # | Pre-defense component | Document |
| --- | --- | --- |
| 1 | Project proposal | [docs/01-project-proposal.md](docs/01-project-proposal.md) |
| 2 | Evidence of relevance | [docs/02-evidence-of-relevance.md](docs/02-evidence-of-relevance.md), [interviews](docs/interviews/interviews-2026-10-24.md) |
| 3 | Literature review (16 sources, 13 scientific) | [docs/03-literature-review.md](docs/03-literature-review.md) |
| 4 | Existing system comparison (5 systems, 8 criteria) | [docs/04-existing-system-comparison.md](docs/04-existing-system-comparison.md) |
| 5 | Technology comparison (5 decisions) | [docs/05-technology-comparison.md](docs/05-technology-comparison.md) |
| 6 | Requirements specification | [docs/06-requirements-specification.md](docs/06-requirements-specification.md) |
| 7 | Architecture and diagrams | [docs/07-architecture.md](docs/07-architecture.md), sources in [diagrams/src](diagrams/src) |
| 8 | UX / prototype | [docs/08-ux-prototype.md](docs/08-ux-prototype.md) |
| 9 | Verification and evaluation plan | [docs/09-verification-and-evaluation-plan.md](docs/09-verification-and-evaluation-plan.md) |
| 10 | Project management and risks | [docs/10-project-management-and-risks.md](docs/10-project-management-and-risks.md) |
| 11 | Supervisor feedback | [docs/11-supervisor-feedback.md](docs/11-supervisor-feedback.md) |

**YouTrack:** https://iot-guard.youtrack.cloud (project key `DIP`). Backup of the task list: [docs/youtrack-tasks.csv](docs/youtrack-tasks.csv).

## Technologies

Python 3.10+, scikit-learn (Isolation Forest, Random Forest), pandas, Streamlit, pytest. Planned: SQLite, FastAPI, Docker, Prometheus and Grafana for resource monitoring. Reasons: [docs/05](docs/05-technology-comparison.md).

## Repository structure

```
IoT-Guard/
├── src/iotguard/          source code
│   ├── data.py            load N-BaIoT, build imbalanced subsets, demo data
│   ├── detector.py        models, detection and resource metrics
│   ├── experiment.py      imbalance experiment (CLI)
│   └── dashboard.py       Streamlit prototype
├── tests/                 pytest unit tests
├── docs/                  pre-defense documents 01 to 11, interviews, task list
├── diagrams/src/          editable diagram sources (.mmd, .svg)
├── diagrams/png/          exported diagrams
├── prototype/mockups/     UX mockups (HTML sources + PNG) and prototype screenshots
├── config/                configuration example (no secrets)
├── data/                  datasets are downloaded here (not in Git)
└── results/               experiment output (not in Git)
```

## How to run

```bash
git clone https://github.com/Hanulus/IoT-Guard.git
cd IoT-Guard
python -m venv .venv
# Windows: .venv\Scripts\activate    Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest
```

Run the experiment on synthetic demo data (no download needed):

```bash
# Windows PowerShell: $env:PYTHONPATH="src"    Linux/macOS: export PYTHONPATH=src
python -m iotguard.experiment --demo
```

Run on real N-BaIoT data (download first, see [data/README.md](data/README.md)):

```bash
python -m iotguard.experiment --data data/n-baiot/1 --n-total 20000
```

Start the dashboard:

```bash
streamlit run src/iotguard/dashboard.py
```

## Development workflow

- `main` holds the reviewed version. Every task has a YouTrack ID (`DIP-n`), a branch `DIP-n-short-name` and a pull request that references the task.
- Pull requests describe what changed and how it was checked. The supervisor reviews selected pull requests at checkpoints.
- Submitted versions are tagged: `pre-defense-1`, `pre-defense-2`, `final-pre-defense`.

## Known limitations

- Experiments so far ran only on synthetic demo data to check the pipeline; no research results yet.
- The supervisor review of pre-defense 1 is still in progress. Interviews so far cover home users only, not small offices.
- Live traffic capture is designed but not implemented.
