# 1. Project Proposal

## Title

**IoT-Guard: Lightweight Machine Learning Based Anomaly and Intrusion Detection for Smart Home IoT Networks**

Research focus: how class imbalance in IoT traffic affects the accuracy and the resource cost of a lightweight detector running on cheap hardware.

## Team and supervision

| Role | Name | Group / Department | GitHub |
| --- | --- | --- | --- |
| Student (individual project) | Chingiz Uraimov | SE-2405, Astana IT University | [Hanulus](https://github.com/Hanulus) |
| Supervisor | Abzal Kyzyrkanov | Astana IT University | [abzzall](https://github.com/abzzall) |

## Problem statement

Smart home devices such as IP cameras, doorbells, baby monitors and smart plugs often ship with weak default settings and rarely get security updates. The Mirai botnet showed that hundreds of thousands of such devices can be taken over and used for large DDoS attacks (Antonakakis et al., 2017). The owner of a home or a small office usually has no tool that tells them that one of their devices started to behave strangely.

Research on machine learning intrusion detection for IoT reports very high accuracy, often above 95 to 99% (Meidan et al., 2018; Al-Sarem et al., 2022; Naeem et al., 2025). But most of these results are measured on curated, roughly balanced benchmark data and on lab machines. In a real home, attacks are rare compared to normal traffic, and the detector has to run on something small like a router or a Raspberry Pi. It is not clear how much of the reported accuracy survives in those conditions and how much CPU, memory and time the detector really needs.

## Target users

| User group | What they need |
| --- | --- |
| Home owners with several smart devices | A simple signal "this device behaves unusually" without reading packet logs |
| Small offices (5 to 30 people) without a security team | Cheap monitoring of cameras, printers and other IoT devices on the office network |
| Students and researchers | A reproducible way to test how detectors behave under imbalance and limited resources |

Primary users for this diploma are home owners and small offices. Researchers are a secondary group because the experiment part is also a research contribution.

## Aim

To design and build a lightweight anomaly detection system for smart home and small office IoT networks, and to measure how class imbalance changes its detection quality and resource cost on constrained hardware.

## Objectives

1. Review existing research, datasets and tools for IoT intrusion detection (done for pre-defense 1, see [03](03-literature-review.md), [04](04-existing-system-comparison.md)).
2. Prepare N-BaIoT (and CICIoT2023 as a second dataset) and build versions of the data with 50%, 20%, 10%, 5% and 1% attack traffic.
3. Train and compare two lightweight detectors: Isolation Forest (baseline, needs no attack labels) and Random Forest.
4. Measure precision, recall, F1, false positive rate, latency, memory and model size for every imbalance level.
5. Run the detector under limited resources (Docker with 1 CPU and 512 MB RAM, and a Raspberry Pi 4 if available).
6. Build a working prototype: detector service, alert storage and a web dashboard for the owner.
7. Evaluate the system against the requirements and the baseline, and describe when the detector is good enough for a real home.

## Expected outcomes

- A working prototype (detector + dashboard) that can be run with one command.
- A reproducible experiment script and a results table that answer the research question.
- Practical recommendations: which model and settings to use for a home network with rare attacks.
- Diploma thesis text and the repository with full history.

## Scope

| In scope | Out of scope |
| --- | --- |
| Network traffic based detection (flow and packet statistics) | Deep packet inspection of encrypted payloads |
| Public datasets N-BaIoT and CICIoT2023 for training and evaluation | Collecting a large new dataset from real homes |
| Lightweight classical ML models (Isolation Forest, Random Forest) | Large deep learning models that need a GPU |
| Alerts on a dashboard, optional Telegram notification | Automatic blocking of devices on the router (only shown as a planned feature) |
| Resource measurement in Docker and on Raspberry Pi | Testing on many different commercial routers |

## Engineering complexity

The project is not only a model in a notebook. It includes a data pipeline for a dataset with 115 features and millions of rows, two detection models, an experiment runner with resource measurement, a service that scores traffic windows, alert storage, a dashboard, containerisation with resource limits, and automated tests. The research part (imbalance vs resource cost) adds a controlled experimental design with baselines and repeated runs.

## Connection to earlier work

The topic was first explored in the Research Methods and Tools course (September to October 2026): a literature review with 10 sources (Assignment 1) and the research question (Assignment 2). Those results were moved into this repository on 23 October 2026 and extended for the diploma.
