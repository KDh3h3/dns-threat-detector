import math

def calculate_entropy(domain):
    domain = domain.split('.')[0]
    if len(domain) == 0:
        return 0
    probabilities = [domain.count(c) / len(domain) for c in set(domain)]
    return -sum(p * math.log2(p) for p in probabilities)

def detect_high_entropy(domains, threshold=3.5):
    suspicious = []
    for d in domains:
        entropy = calculate_entropy(d)
        if entropy > threshold:
            suspicious.append({"domain": d, "entropy": round(entropy, 2)})
    return suspicious
