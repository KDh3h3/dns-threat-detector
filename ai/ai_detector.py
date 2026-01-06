import pandas as pd
from sklearn.ensemble import IsolationForest
from detectors.entropy_detector import calculate_entropy

def run_ai_detection(csv_path):
    df = pd.read_csv(csv_path)

    df["entropy"] = df["query"].apply(calculate_entropy)
    df["query_length"] = df["query"].apply(len)
    df["is_txt"] = df["qtype"].apply(lambda x: 1 if x == "TXT" else 0)
    df["is_nxdomain"] = df["response"].apply(lambda x: 1 if x == "NXDOMAIN" else 0)

    features = df[["entropy", "query_length", "is_txt", "is_nxdomain"]]

    model = IsolationForest(contamination=0.15, random_state=42)
    df["anomaly"] = model.fit_predict(features)

    return df[df["anomaly"] == -1]
