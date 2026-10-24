"""Two lightweight detectors and the code that measures them.

- Random Forest: supervised, learns from benign and attack examples.
- Isolation Forest: unsupervised, learns only from benign traffic and
  flags anything that looks unusual. This is the baseline because it does
  not need attack labels.
"""

import pickle
import time
import tracemalloc

from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


MODEL_NAMES = ["isolation_forest", "random_forest"]


def build_model(name, seed=42):
    if name == "random_forest":
        # small forest on purpose: it has to run on cheap hardware
        return RandomForestClassifier(n_estimators=50, max_depth=12, n_jobs=1, random_state=seed)
    if name == "isolation_forest":
        return IsolationForest(n_estimators=100, contamination="auto", random_state=seed)
    raise ValueError(f"Unknown model: {name}")


def train(model, X_train, y_train):
    if isinstance(model, IsolationForest):
        # unsupervised: train on normal traffic only
        model.fit(X_train[y_train == 0])
    else:
        model.fit(X_train, y_train)
    return model


def predict(model, X):
    """Return 0 (normal) or 1 (attack) for every row."""
    pred = model.predict(X)
    if isinstance(model, IsolationForest):
        # IsolationForest returns 1 for normal and -1 for anomaly
        pred = (pred == -1).astype(int)
    return pred


def detection_metrics(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }


def resource_metrics(model, X_test):
    """Model size, peak memory during prediction and latency per row."""
    size_kb = len(pickle.dumps(model)) / 1024

    tracemalloc.start()
    start = time.perf_counter()
    model.predict(X_test)
    total_s = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "model_size_kb": size_kb,
        "peak_memory_mb": peak / (1024 * 1024),
        "latency_ms_per_1000_rows": total_s * 1000 / len(X_test) * 1000,
    }
