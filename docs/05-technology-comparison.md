# 5. Technology Comparison

Five key technical decisions. For each one, 2 to 3 alternatives are compared against the project requirements (section 6). Score: ✓ good, ~ acceptable, ✗ poor.

## 5.1 Language and ML library

| Criterion | **Python + scikit-learn** | Python + PyTorch | Go + ONNX runtime |
| --- | --- | --- | --- |
| Isolation Forest / Random Forest out of the box | ✓ | ✗ (must implement or add another lib) | ✗ (only inference of exported models) |
| Runs on Raspberry Pi without GPU | ✓ | ~ (large install) | ✓ |
| Fast prototyping and experiments | ✓ | ~ | ✗ |
| Memory footprint of runtime | ~ | ✗ | ✓ |
| My experience | ✓ | ~ | ✓ (Go used in backend courses) |

**Decision: Python + scikit-learn.** The research needs many quick experiments with classical models, and scikit-learn has both chosen models. Go could be used later for a small capture service if Python is too slow (risk R3).

## 5.2 Detection model

| Criterion | **Isolation Forest (baseline)** | **Random Forest** | Autoencoder (N-BaIoT / Kitsune style) |
| --- | --- | --- | --- |
| Needs attack labels | No | Yes | No |
| Expected accuracy on known attacks | ~ | ✓ | ✓ |
| Training and inference cost on CPU | ✓ low | ✓ low | ~ needs more compute |
| Model size | ✓ small | ~ grows with trees | ~ |
| Explainability for alerts | ~ | ✓ feature importance | ✗ |

**Decision: compare Isolation Forest (baseline) and Random Forest.** Together they cover unsupervised and supervised detection with low cost. An autoencoder is kept as an optional third model if time allows.

## 5.3 Data storage

| Criterion | **SQLite** | PostgreSQL | Plain CSV files |
| --- | --- | --- | --- |
| Setup on a Pi / single container | ✓ no server | ~ separate service | ✓ |
| Query alerts by device and time | ✓ SQL | ✓ SQL | ✗ |
| Concurrent writers | ~ | ✓ | ✗ |
| Memory usage | ✓ | ~ | ✓ |

**Decision: SQLite for alerts, CSV/Parquet for datasets and experiment results.** One home network has a small number of alerts, so a database server is not needed. PostgreSQL stays an option for multi site use.

## 5.4 Component interaction and user interface

| Criterion | **Streamlit dashboard + Python modules** | FastAPI REST + React | Prometheus + Grafana |
| --- | --- | --- | --- |
| Time to a working prototype | ✓ | ✗ | ~ |
| UI for non experts | ~ | ✓ | ✗ (engineer oriented) |
| Good for resource metrics over time | ~ | ~ | ✓ |
| Extra services to run | 1 | 2 | 2 |

**Decision:** Streamlit for the prototype UI (fast, Python only). A small FastAPI layer is planned between the detector and the UI for pre-defense 2. Prometheus + Grafana are used only to monitor CPU and memory during experiments (I already used them in the SRE course), not as the user UI.

## 5.5 Constrained runtime for experiments

| Criterion | **Docker with --cpus / --memory limits** | Raspberry Pi 4 | Virtual machine |
| --- | --- | --- | --- |
| Available now | ✓ | ~ (to be borrowed) | ✓ |
| Repeatable limits | ✓ | ✓ (real hardware) | ✓ |
| Realism for a home device | ~ | ✓ | ~ |
| Setup time | ✓ | ~ | ✗ |

**Decision: Docker limits as the main setup (1 CPU, 512 MB RAM), Raspberry Pi 4 as a confirmation run if a device is available.**
