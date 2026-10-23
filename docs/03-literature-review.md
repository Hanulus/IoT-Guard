# 3. Literature Review

## 3.1 Search method

Sources were searched in IEEE Xplore, MDPI, Google Scholar and arXiv with combinations of: *IoT intrusion detection*, *smart home anomaly detection*, *botnet detection*, *N-BaIoT*, *class imbalance*, *lightweight*, *edge*. Inclusion: peer reviewed paper or a well known preprint with a clear method and results, English, related to IoT or smart home networks. Most technical sources are from 2019 to 2026. A few older works are kept because they are foundational (the dataset, the algorithms and the Mirai analysis).

16 sources are used: 13 scientific publications and 3 technical sources (tool documentation).

## 3.2 Structured analysis table

| # | Source | Type | Problem / method | Data | Main result | Limitation | Use in IoT-Guard |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Meidan et al. (2018) | Journal (IEEE Pervasive Computing) | Per device deep autoencoders trained on benign traffic | N-BaIoT, 9 devices, Mirai and BASHLITE | Detected all attacks with very low false alarm rate in the lab | Lab infection, no imbalance study, no resource cost | Main dataset, idea of training on benign traffic only |
| 2 | Neto et al. (2023) | Journal (Sensors) | New large dataset and ML benchmark | CICIoT2023, 105 devices, 33 attacks | Gives baseline results for binary and multi class tasks | Very large, attack share is high in the raw data | Second dataset to check generalisation |
| 3 | Mirsky et al. (2018) | Conference (NDSS) | Kitsune: online ensemble of small autoencoders | Real IP camera and IoT network traces | Runs online, tested on Raspberry Pi | Unsupervised only, tuned for one network | Existing system in comparison, shows Pi is realistic |
| 4 | Antonakakis et al. (2017) | Conference (USENIX Security) | Measurement study of the Mirai botnet | Real telemetry over months | Explains how cheap IoT devices are infected | Not a detection method | Motivation, attack patterns for alerts |
| 5 | Al-Sarem et al. (2022) | Journal (Sensors) | Mutual information feature selection + RF, XGBoost, SVM, kNN | N-BaIoT | About 99% accuracy with fewer features | Balanced lab data | Supports small feature sets and RF |
| 6 | Naeem et al. (2025) | Preprint (arXiv) | Attention based CNN-BiLSTM | N-BaIoT | About 99% accuracy | Heavy model, no resource numbers | Shows DL gives similar accuracy to classical ML on this data |
| 7 | Xue et al. (2025) | Journal (Informatica) | XGBoost tuned with a metaheuristic optimiser | Smart home IoT data | Accuracy grows from 95.3% to 98.7% | Extra tuning cost not measured on device | Candidate model for comparison later |
| 8 | Chen et al. (2023) | Journal (Electronics) | CWGAN to generate attack samples in few shot cases | Smart home IDS data | 3 to 22% accuracy gain for 8 classifiers | Synthetic samples may not match real attacks | Shows rare attacks are a real problem |
| 9 | Choukhairi et al. (2026) | Journal (IAES IJ-AI) | Transfer learning CNN-LSTM with PSO | IoTID20 | Very high accuracy | Training set balanced by oversampling | Direct support for the imbalance research gap |
| 10 | Ali et al. (2023) | Journal (Al-Mustansiriyah J. Sci.) | Face recognition intruder detection on Raspberry Pi | 844 own images | 97.6% accuracy on Pi | Physical intrusion, small data | Example of deployment on constrained hardware |
| 11 | Cook et al. (2019) | Survey (IEEE IoT Journal) | Review of anomaly detection for IoT time series | Many | Lists methods and open problems | Not network specific | Background, missing real world benchmarks |
| 12 | DeMedeiros et al. (2023) | Survey (Sensors) | Review of AI anomaly detection in IoT and sensor networks | Many | Classifies ML / DL methods | No experiments | Background, gap on realistic evaluation |
| 13 | Fährmann et al. (2024) | Survey (IEEE Access) | Anomaly detection in smart environments | Many | Taxonomy of anomaly types | No experiments | Background, defines anomaly types for alerts |
| 14 | Liu, Ting & Zhou (2008) | Conference (IEEE ICDM) | Isolation Forest algorithm | Benchmark sets | Fast, linear time, low memory anomaly detection | Weaker when anomalies are not "few and different" | Baseline model |
| 15 | Chawla et al. (2002) | Journal (JAIR) | SMOTE oversampling for imbalanced data | Benchmark sets | Better minority class recall | Can create unrealistic samples | Planned option to handle imbalance, compared with no resampling |
| 16 | Zeek, Suricata, Snort project documentation | Technical | Rule based and scripting network monitors | N/A | Mature open source tools | Need expert setup, signatures miss new behaviour | Existing systems comparison |

## 3.3 Critical synthesis

**Detection works well on benchmarks.** Studies on N-BaIoT reach around 99% accuracy with very different models: autoencoders (1), classical ML with feature selection (5) and attention based DL (6). When many different models get almost the same result, it suggests that the dataset is easy to separate under lab conditions, not that one model is clearly better. For IoT-Guard this means a simple model like Random Forest is a reasonable choice, and the interesting question is not "which model is the most accurate" but "under which conditions does accuracy drop".

**Imbalance is usually removed, not studied.** Several papers balance the data before training (9) or generate extra attack samples (8, 15). This helps the score, but real home traffic is mostly normal. Surveys (11, 12, 13) say that evaluation under realistic conditions is missing. None of the reviewed technical papers reports how precision and false alarms change when the attack share goes down to a few percent.

**Resource cost is rarely reported.** Kitsune (3) and the Pi based intruder detector (10) are exceptions that show small hardware can run a detector. Most accuracy papers (5, 6, 7, 9) do not report latency, memory or model size, so it is unclear if their models are usable in a home.

**Unsupervised vs supervised.** Training only on benign traffic (1, 3, 14) does not need attack labels and can catch new behaviour, which fits a home where nobody labels traffic. Supervised models (5, 7) are usually more accurate on known attacks. IoT-Guard compares both, with Isolation Forest as the baseline.

**Limitations the project takes into account.**
- Results on N-BaIoT may be optimistic, so CICIoT2023 is used as a second dataset (2).
- Accuracy alone is misleading under imbalance, so precision, recall, F1 and false positive rate are reported (section 9).
- Resampling (SMOTE) can hide the problem, so it is tested as an option and not used by default (15).

## 3.4 Research gap and question

Gap: there is little evidence on how the accuracy and the resource cost of lightweight IoT detectors change together when attack traffic is rare and the hardware is limited.

Research question: *How does class imbalance in IoT traffic data affect the accuracy and resource efficiency of a lightweight anomaly detection model deployed on resource-constrained smart home hardware?*

Hypotheses: H1, recall and precision drop as the attack share decreases. H2, latency and memory stay mostly the same across imbalance levels because they depend on the number of features and rows, not on the class balance.

## References

1. Meidan, Y., Bohadana, M., Mathov, Y., Mirsky, Y., Breitenbacher, D., Shabtai, A., & Elovici, Y. (2018). N-BaIoT: Network-based detection of IoT botnet attacks using deep autoencoders. *IEEE Pervasive Computing, 17*(3), 12–22. https://doi.org/10.1109/MPRV.2018.03367731 (preprint: https://arxiv.org/abs/1805.03409)
2. Neto, E. C. P., Dadkhah, S., Ferreira, R., Zohourian, A., Lu, R., & Ghorbani, A. A. (2023). CICIoT2023: A real-time dataset and benchmark for large-scale attacks in IoT environment. *Sensors, 23*(13), 5941. https://doi.org/10.3390/s23135941
3. Mirsky, Y., Doitshman, T., Elovici, Y., & Shabtai, A. (2018). Kitsune: An ensemble of autoencoders for online network intrusion detection. *Proceedings of NDSS 2018*. https://arxiv.org/abs/1802.09089
4. Antonakakis, M., et al. (2017). Understanding the Mirai botnet. *26th USENIX Security Symposium*, 1093–1110. https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis
5. Al-Sarem, M., Saeed, F., Alkhammash, E. H., & Alghamdi, N. S. (2022). An aggregated mutual information based feature selection with machine learning methods for enhancing IoT botnet attack detection. *Sensors, 22*(1), 185. https://doi.org/10.3390/s22010185
6. Naeem, A., Khan, M. A., Alasbali, N., Ahmad, J., Khattak, A. A., & Khan, M. S. (2025). Efficient IoT intrusion detection with an improved attention-based CNN-BiLSTM architecture. *arXiv*. https://doi.org/10.48550/arXiv.2503.19339
7. Xue, S., Liu, X., Zhang, M., & Gu, L. (2025). Metaheuristic-enhanced XGBoost framework for intrusion detection in smart home IoT systems. *Informatica, 49*(34), 281–296. https://doi.org/10.31449/inf.v49i34.8837
8. Chen, Y., Wang, J., Yang, T., Li, Q., & Nijhum, N. A. (2023). An enhancement method in few-shot scenarios for intrusion detection in smart home environments. *Electronics, 12*(15), 3304. https://doi.org/10.3390/electronics12153304
9. Choukhairi, M., Choukhairi, O., Fakhri, Y., & Choukri, A. (2026). A transfer hybrid deep learning approach for advanced intrusion detection in IoT-based smart home security. *IAES International Journal of Artificial Intelligence, 15*(3), 2750–2760. https://doi.org/10.11591/ijai.v15.i3.pp2750-2760
10. Ali, H. H., Naif, J. R., & Humood, W. R. (2023). A new smart home intruder detection system based on deep learning. *Al-Mustansiriyah Journal of Science, 34*(2), 60–69. https://doi.org/10.23851/mjs.v34i2.1267
11. Cook, A., Mısırlı, G., & Fan, Z. (2019). Anomaly detection for IoT time-series data: A survey. *IEEE Internet of Things Journal, 7*(7), 6481–6494. https://doi.org/10.1109/JIOT.2019.2958185
12. DeMedeiros, K., Hendawi, A., & Alvarez, M. (2023). A survey of AI-based anomaly detection in IoT and sensor networks. *Sensors, 23*(3), 1352. https://doi.org/10.3390/s23031352
13. Fährmann, D., Martín, L., Sánchez, L., & Damer, N. (2024). Anomaly detection in smart environments: A comprehensive survey. *IEEE Access, 12*, 66540–66567. https://doi.org/10.1109/ACCESS.2024.3396459
14. Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008). Isolation forest. *2008 Eighth IEEE International Conference on Data Mining*, 413–422. https://doi.org/10.1109/ICDM.2008.17
15. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research, 16*, 321–357. https://doi.org/10.1613/jair.953
16. Technical documentation: Zeek (https://docs.zeek.org), Suricata (https://docs.suricata.io), Snort 3 (https://www.snort.org/documents).
