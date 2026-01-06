import pandas as pd
import matplotlib.pyplot as plt
from detectors.entropy_detector import calculate_entropy

def run_dashboard(csv_path):
    df = pd.read_csv(csv_path)

    # Top domains
    df["query"].value_counts().head(10).plot(kind="bar", title="Top Queried Domains")
    plt.tight_layout()
    plt.show()

    # Entropy
    df["entropy"] = df["query"].apply(calculate_entropy)
    df[df["entropy"] > 3.5]["entropy"].hist(bins=10)
    plt.title("High Entropy Domains")
    plt.xlabel("Entropy")
    plt.ylabel("Count")
    plt.show()

    # NXDOMAIN per IP
    df[df["response"] == "NXDOMAIN"]["src_ip"].value_counts().plot(
        kind="bar", title="NXDOMAIN Queries per Host"
    )
    plt.tight_layout()
    plt.show()
