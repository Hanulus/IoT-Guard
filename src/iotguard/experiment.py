"""Run the class imbalance experiment.

For every attack ratio, build a dataset, train both models and save
detection and resource metrics to a CSV file.

Examples:
    python -m iotguard.experiment --demo
    python -m iotguard.experiment --data data/n-baiot/device1 --n-total 20000
"""

import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from iotguard import data, detector

DEFAULT_RATIOS = [0.5, 0.2, 0.1, 0.05, 0.01]
MODELS = detector.MODEL_NAMES


def run(df, ratios, n_total, seed=42):
    rows = []
    for ratio in ratios:
        subset = data.make_imbalanced(df, ratio, n_total, seed)
        X, y = data.split_xy(subset)
        # stratify keeps the same attack ratio in train and test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, stratify=y, random_state=seed
        )
        for name in MODELS:
            model = detector.train(detector.build_model(name, seed), X_train, y_train)
            y_pred = detector.predict(model, X_test)
            row = {"model": name, "attack_ratio": ratio}
            row.update(detector.detection_metrics(y_test, y_pred))
            row.update(detector.resource_metrics(model, X_test))
            rows.append(row)
            print(f"ratio={ratio:<5} {name:<17} f1={row['f1']:.3f} recall={row['recall']:.3f}")
    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description="IoT-Guard imbalance experiment")
    parser.add_argument("--data", help="folder with N-BaIoT CSV files")
    parser.add_argument("--demo", action="store_true", help="use synthetic demo data")
    parser.add_argument("--n-total", type=int, default=10000)
    parser.add_argument("--max-rows-per-file", type=int, default=50000)
    parser.add_argument("--out", default="results/results.csv")
    args = parser.parse_args()

    if args.demo:
        df = data.make_demo_data()
        print("Using SYNTHETIC demo data (not real results)")
    elif args.data:
        df = data.load_folder(args.data, args.max_rows_per_file)
    else:
        parser.error("give --data <folder> or --demo")

    results = run(df, DEFAULT_RATIOS, args.n_total)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.out, index=False)
    print(f"Saved {len(results)} rows to {args.out}")


if __name__ == "__main__":
    main()
