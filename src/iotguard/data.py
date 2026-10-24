"""Loading and preparing IoT traffic data.

The main dataset is N-BaIoT (UCI ML Repository, dataset 442).
Every CSV file in N-BaIoT has 115 numeric features and no label column,
so the label is taken from the file name:
    *benign*            -> 0 (normal traffic)
    *mirai* / *gafgyt*  -> 1 (attack traffic)
"""

from pathlib import Path

import numpy as np
import pandas as pd

LABEL = "label"


def label_from_filename(name):
    """Return 0 for benign files, 1 for attack files, None for other files."""
    name = name.lower()
    if "benign" in name:
        return 0
    if "mirai" in name or "gafgyt" in name or "bashlite" in name:
        return 1
    return None


def load_folder(folder, max_rows_per_file=None):
    """Read all labelled CSV files from a folder (searches subfolders too)."""
    frames = []
    for path in sorted(Path(folder).rglob("*.csv")):
        # the label can be in the file name or in the parent folder name
        label = label_from_filename(path.name)
        if label is None:
            label = label_from_filename(path.parent.name)
        if label is None:
            continue
        df = pd.read_csv(path, nrows=max_rows_per_file)
        df[LABEL] = label
        frames.append(df)

    if not frames:
        raise FileNotFoundError(f"No benign/attack CSV files found in {folder}")
    return pd.concat(frames, ignore_index=True)


def make_imbalanced(df, attack_ratio, n_total, seed=42):
    """Sample a subset where attack rows make up `attack_ratio` of all rows.

    Example: attack_ratio=0.05 and n_total=10000 gives
    9500 benign rows and 500 attack rows.
    """
    if not 0 < attack_ratio < 1:
        raise ValueError("attack_ratio must be between 0 and 1")

    n_attack = int(round(n_total * attack_ratio))
    n_benign = n_total - n_attack

    benign = df[df[LABEL] == 0]
    attack = df[df[LABEL] == 1]
    if len(benign) < n_benign or len(attack) < n_attack:
        raise ValueError("Not enough rows for this ratio, use a smaller n_total")

    part = pd.concat([
        benign.sample(n_benign, random_state=seed),
        attack.sample(n_attack, random_state=seed),
    ])
    # shuffle rows
    return part.sample(frac=1, random_state=seed).reset_index(drop=True)


def make_demo_data(n_rows=20000, n_features=20, seed=0):
    """Create SYNTHETIC data with the same layout as N-BaIoT.

    Used only for unit tests and for a quick demo when the real dataset is
    not downloaded. Numbers produced on this data are not research results.
    """
    rng = np.random.default_rng(seed)
    n_attack = n_rows // 2
    n_benign = n_rows - n_attack

    benign = rng.normal(0.0, 1.0, size=(n_benign, n_features))
    # attack traffic: shifted mean and higher variance in some features
    attack = rng.normal(0.0, 1.0, size=(n_attack, n_features))
    attack[:, : n_features // 2] += rng.normal(1.5, 0.5, size=(n_attack, n_features // 2))

    columns = [f"f{i}" for i in range(n_features)]
    df = pd.DataFrame(np.vstack([benign, attack]), columns=columns)
    df[LABEL] = [0] * n_benign + [1] * n_attack
    return df


def split_xy(df):
    """Split a dataframe into features X and labels y."""
    return df.drop(columns=[LABEL]), df[LABEL]
