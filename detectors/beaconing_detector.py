from collections import defaultdict

def detect_beaconing(logs, min_hits=4):
    domain_hits = defaultdict(int)

    for log in logs:
        domain_hits[log["query"]] += 1

    return [domain for domain, count in domain_hits.items() if count >= min_hits]
