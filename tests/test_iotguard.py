import pandas as pd
import pytest

from iotguard import data


def test_label_from_filename():
    assert data.label_from_filename("1.benign.csv") == 0
    assert data.label_from_filename("1.mirai.scan.csv") == 1
    assert data.label_from_filename("1.gafgyt.combo.csv") == 1
    assert data.label_from_filename("device_info.csv") is None


def test_make_imbalanced_ratio():
    df = data.make_demo_data(n_rows=4000)
    part = data.make_imbalanced(df, attack_ratio=0.05, n_total=1000)
    assert len(part) == 1000
    assert part[data.LABEL].sum() == 50


def test_make_imbalanced_bad_ratio():
    df = data.make_demo_data(n_rows=1000)
    with pytest.raises(ValueError):
        data.make_imbalanced(df, attack_ratio=1.5, n_total=100)


def test_load_folder(tmp_path):
    pd.DataFrame({"a": [1, 2], "b": [3, 4]}).to_csv(tmp_path / "1.benign.csv", index=False)
    pd.DataFrame({"a": [9], "b": [9]}).to_csv(tmp_path / "1.mirai.syn.csv", index=False)
    df = data.load_folder(tmp_path)
    assert len(df) == 3
    assert df[data.LABEL].tolist().count(1) == 1
