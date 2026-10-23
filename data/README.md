# Data

Datasets are not stored in Git because they are large. Download them yourself:

## N-BaIoT (main dataset)

1. Open https://archive.ics.uci.edu/dataset/442/detection+of+iot+botnet+attacks+n+baiot
2. Download the zip and extract it.
3. Put the CSV files of one device into a folder, for example `data/n-baiot/1/`:
   ```
   data/n-baiot/1/1.benign.csv
   data/n-baiot/1/1.mirai.scan.csv
   data/n-baiot/1/1.gafgyt.combo.csv
   ...
   ```
   (Some copies of the dataset have archives `mirai_attacks.rar` and `gafgyt_attacks.rar` per device; extract them into the same folder. The loader also understands labels in folder names.)

Labels are taken from the file name: `benign` → 0, `mirai` / `gafgyt` → 1.

## CICIoT2023 (second dataset, planned)

https://www.unb.ca/cic/datasets/iotdataset-2023.html

## Demo data

`python -m iotguard.experiment --demo` uses synthetic data generated in code. It is only for tests and demos, not for results.
