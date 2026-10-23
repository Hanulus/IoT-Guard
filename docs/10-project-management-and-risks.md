# 10. Project Management and Risks

## 10.1 Tools

- **Git repository:** https://github.com/Hanulus/IoT-Guard (`main` is the reviewed baseline, work is done in `DIP-<n>-<short-name>` branches and merged through pull requests).
- **YouTrack project:** key `DIP`, link in the README. The same task list is kept in [`youtrack-tasks.csv`](youtrack-tasks.csv) as a backup.
- **Supervisor access:** supervisor (GitHub `abzzall`) is invited as a collaborator and reviews selected pull requests at checkpoints.

## 10.2 Responsibilities

This is an individual project. Chingiz Uraimov is responsible for research, design, implementation, testing and documentation. The supervisor, Abzal Kyzyrkanov, reviews the key deliverables and decisions (section 11).

## 10.3 Milestones

| Milestone | Content | Target date |
| --- | --- | --- |
| M0 Topic and research question | RMT Assignments 1 and 2, topic agreed with supervisor | Oct 2026 (done) |
| M1 Pre-defense 1 | Proposal, reviews, requirements, architecture, prototype, plans | 24 Oct 2026 |
| M2 Real experiments | N-BaIoT runs for all ratios and models, first results | Nov 2026 |
| M3 Constrained runs | Docker limits and Raspberry Pi measurements | Dec 2026 |
| M4 Pre-defense 2 | Live traffic pipeline, alert store, API, results chapter draft | Date set by the department |
| M5 Final pre-defense | Complete system, evaluation, thesis text | Date set by the department |

## 10.4 Task list (YouTrack)

| ID | Task | Priority | Deadline | State |
| --- | --- | --- | --- | --- |
| DIP-1 | Set up repository structure, README, .gitignore | Major | 23 Oct 2026 | Done |
| DIP-2 | Write project proposal and scope | Critical | 23 Oct 2026 | Done |
| DIP-3 | Prepare evidence of relevance and interview guide | Major | 23 Oct 2026 | Done |
| DIP-4 | Conduct 3 to 5 user interviews and summarise | Critical | 31 Oct 2026 | Open |
| DIP-5 | Extend literature review to 15+ sources with analysis table | Critical | 23 Oct 2026 | Done |
| DIP-6 | Compare existing systems and technologies | Major | 23 Oct 2026 | Done |
| DIP-7 | Write requirements with priorities and acceptance criteria | Critical | 23 Oct 2026 | Done |
| DIP-8 | Create context, use case and component diagrams | Major | 23 Oct 2026 | Done |
| DIP-9 | Implement data loader and imbalance sampling with tests | Critical | 23 Oct 2026 | Done |
| DIP-10 | Implement detectors and experiment runner with tests | Critical | 23 Oct 2026 | Done |
| DIP-11 | Build dashboard prototype and UX mockups | Major | 23 Oct 2026 | Done |
| DIP-12 | Write verification and evaluation plan | Major | 23 Oct 2026 | Done |
| DIP-13 | Get supervisor feedback on pre-defense 1 materials | Critical | 24 Oct 2026 | In progress |
| DIP-14 | Run experiments on N-BaIoT (5 ratios × 2 models × 5 seeds) | Critical | 15 Nov 2026 | Open |
| DIP-15 | Add CICIoT2023 subset loader and runs | Major | 30 Nov 2026 | Open |
| DIP-16 | Constrained runs in Docker (1 CPU, 512 MB) with Prometheus | Critical | 10 Dec 2026 | Open |
| DIP-17 | Traffic collector and feature extractor for live traffic | Major | Pre-defense 2 | Open |
| DIP-18 | SQLite alert store and false alarm marking | Major | Pre-defense 2 | Open |
| DIP-19 | GitHub Actions CI for tests | Normal | 15 Nov 2026 | Open |

## 10.5 Risks

| ID | Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| R1 | N-BaIoT results are too optimistic (lab data) | High | Medium | Second dataset CICIoT2023; report this as a limitation |
| R2 | No Raspberry Pi available | Medium | Low | Docker with CPU and memory limits as the main setup |
| R3 | Python is too slow for live traffic on a Pi | Medium | Medium | Score windows in batches; move capture to Go if needed |
| R4 | Not enough interview participants | Medium | Medium | Ask classmates' families and small shops nearby; 3 is the minimum |
| R5 | Datasets are large (GBs) and slow to process on a laptop | High | Low | Use per device subsets and `--max-rows-per-file` |
| R6 | Scope creep (blocking, mobile app) | Medium | Medium | Out of scope list in section 1; only Must items before pre-defense 2 |
| R7 | Personal data or secrets committed by mistake | Low | High | `.gitignore` for data and `.env`; config examples only |

## 10.6 Dependencies

- DIP-14 depends on DIP-9, DIP-10 and on downloading N-BaIoT from the UCI repository.
- DIP-16 depends on DIP-14.
- DIP-17 and DIP-18 depend on the component design (DIP-8).
- Final requirements (NFR-3, NFR-7) depend on interview results (DIP-4).
