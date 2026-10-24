"""Prototype dashboard (Streamlit).

Run from the repository root:
    streamlit run src/iotguard/dashboard.py

Page 1 "Alerts" replays test traffic through a trained model and shows
which rows would raise an alert. Page 2 "Experiment" shows the results
CSV produced by experiment.py.
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

# make "import iotguard" work when started with "streamlit run"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from iotguard import data, detector  # noqa: E402

RESULTS_FILE = Path("results/results.csv")

st.set_page_config(page_title="IoT-Guard", layout="wide")
st.title("IoT-Guard")
st.caption("Prototype. Demo mode uses synthetic traffic, not real household data.")

page = st.sidebar.radio("Page", ["Alerts", "Experiment"])
data_folder = st.sidebar.text_input("N-BaIoT folder (empty = demo data)", "")
model_name = st.sidebar.selectbox("Model", detector.MODEL_NAMES)
attack_ratio = st.sidebar.select_slider(
    "Attack share in traffic", options=[0.01, 0.05, 0.1, 0.2, 0.5], value=0.05
)


@st.cache_data
def load(folder):
    if folder:
        return data.load_folder(folder, max_rows_per_file=20000)
    return data.make_demo_data()


if page == "Alerts":
    df = data.make_imbalanced(load(data_folder), attack_ratio, n_total=5000)
    X, y = data.split_xy(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=1)
    model = detector.train(detector.build_model(model_name), X_train, y_train)
    pred = detector.predict(model, X_test)
    m = detector.detection_metrics(y_test, pred)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows checked", len(X_test))
    c2.metric("Alerts raised", int(pred.sum()))
    c3.metric("Recall", f"{m['recall']:.2f}")
    c4.metric("Precision", f"{m['precision']:.2f}")

    # keep the table readable: only the first 5 traffic features
    alerts = X_test.iloc[:, :5].copy()
    alerts["predicted"] = pred
    alerts["actual"] = y_test.values
    alerts["result"] = alerts.apply(
        lambda r: "true alert" if r.predicted and r.actual
        else "false alarm" if r.predicted
        else "missed attack" if r.actual
        else "ok",
        axis=1,
    )
    st.subheader("Alert feed")
    show = st.multiselect("Show", ["true alert", "false alarm", "missed attack", "ok"],
                          default=["true alert", "false alarm", "missed attack"])
    cols = ["result", "predicted", "actual"] + list(alerts.columns[:5])
    st.dataframe(alerts.loc[alerts["result"].isin(show), cols].head(200), use_container_width=True)

else:
    if not RESULTS_FILE.exists():
        st.info("No results yet. Run: python -m iotguard.experiment --demo")
    else:
        res = pd.read_csv(RESULTS_FILE)
        st.subheader("F1-score vs attack share")
        st.line_chart(res.pivot(index="attack_ratio", columns="model", values="f1"))
        st.subheader("Latency (ms per 1000 rows)")
        st.bar_chart(res.pivot(index="attack_ratio", columns="model", values="latency_ms_per_1000_rows"))
        st.dataframe(res, use_container_width=True)
