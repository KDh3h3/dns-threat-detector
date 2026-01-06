def risk_score(entropy_hits, nxdomain_hits, volume_hits):
    return (
        len(entropy_hits) * 0.4 +
        len(nxdomain_hits) * 0.3 +
        len(volume_hits) * 0.3
    )
def risk_score(entropy_hits, nxdomain_hits, volume_hits):
    return (
        len(entropy_hits) * 0.4 +
        len(nxdomain_hits) * 0.3 +
        len(volume_hits) * 0.3
    )