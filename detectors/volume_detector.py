def detect_volume_spikes(logs, threshold=5):
    ip_volume = {}

    for log in logs:
        ip_volume[log["src_ip"]] = ip_volume.get(log["src_ip"], 0) + 1

    return {ip: count for ip, count in ip_volume.items() if count >= threshold}
