# 9. Verification and Evaluation Plan

## 9.1 What has to be shown

1. The system works as specified (requirements in section 6 are met).
2. The research question is answered: how imbalance changes detection quality and resource cost.
3. The proposed setup is better than, or at least clearly compared with, a baseline.

## 9.2 Baselines

| Baseline | Why |
| --- | --- |
| **B1: Isolation Forest trained on benign traffic only** | Simple unsupervised detector that a home could use without labels. Random Forest must beat it to justify labels. |
| **B2: Balanced 50/50 benchmark condition** | The usual setting in the literature. All imbalanced results are compared to it to see how much performance is lost. |
| B3 (reference): results reported by Meidan et al. (2018) and Al-Sarem et al. (2022) on N-BaIoT | Check that our balanced results are in a similar range, so the pipeline is not broken. |

## 9.3 Metrics

| Metric | Why |
| --- | --- |
| Precision, recall, F1 for the attack class | Accuracy is misleading when attacks are rare |
| False positive rate | Directly tied to how annoying the system is for users (A3) |
| Latency per 1000 windows | NFR-2 |
| Peak memory during prediction, model size | NFR-1, constrained hardware |
| CPU usage (Prometheus / docker stats) | Resource cost on 1 core |

## 9.4 Experimental conditions

| Factor | Levels |
| --- | --- |
| Dataset | N-BaIoT (main), CICIoT2023 subset (generalisation check) |
| Attack share | 50%, 20%, 10%, 5%, 1% |
| Model | Isolation Forest, Random Forest (optional: Random Forest + SMOTE) |
| Hardware | Laptop without limits; Docker `--cpus=1 --memory=512m`; Raspberry Pi 4 if available |
| Repeats | 5 random seeds per condition, mean and standard deviation reported |

Train / test split: 70 / 30, stratified, so the test set keeps the same attack share as the condition. Data from one device is split by time order in the final runs to avoid leakage between close time windows.

## 9.5 Hypotheses and how they are tested

- **H1:** recall and precision decrease as the attack share decreases. Test: compare F1 at 50% vs 5% and 1% across 5 seeds (paired comparison, Wilcoxon test).
- **H2:** latency and memory do not change much across attack shares. Test: compare latency and memory across ratios; a difference under 10% is treated as "no practical change".

## 9.6 Testing plan

| Level | What | Tool | When |
| --- | --- | --- | --- |
| Unit | Data loading, labelling, ratio sampling, model output format, experiment output | pytest (7 tests now) | Every commit |
| Integration | Detector + alert store + dashboard with replayed traffic | pytest + test pcap | Pre-defense 2 |
| System | Full run in Docker with limits | docker compose, scripts | Pre-defense 2 |
| Acceptance | Each Must requirement checked against its criterion | Checklist in this file | Before final defense |
| Usability | 3 users look at the mockup / dashboard and explain the status | Short sessions | After interviews |

## 9.7 Acceptance checklist (filled during the project)

| Requirement | Result | Evidence |
| --- | --- | --- |
| FR-1 | Passed (unit test) | `tests/test_iotguard.py` |
| FR-2 | Passed (unit test) | `tests/test_iotguard.py` |
| FR-3 | Passed (unit test, demo data) | `tests/test_iotguard.py` |
| FR-4 | Passed (unit test) | `tests/test_iotguard.py` |
| FR-5, FR-6 | Passed (demo) | screenshots in section 8 |
| NFR-1, NFR-2 | Not yet measured | Docker runs planned |
| NFR-3 | Not yet measured | needs N-BaIoT runs |
| NFR-4 | Seed is fixed in code; double run check planned | |

## 9.8 Status

At pre-defense 1 only demo (synthetic) data has been run, to check that the pipeline works end to end. No research conclusions are drawn from it. The first real runs on N-BaIoT are task DIP-14.
