import json
import time

# Load parsed data
with open("transactions.json", "r", encoding="utf-8") as f:
    transactions = json.load(f)

# -------------------------
# Linear Search
# -------------------------
def linear_search(transactions, target_id):
    for tx in transactions:
        if tx["id"] == target_id:
            return tx
    return None

# -------------------------
# Dictionary Lookup
# -------------------------
tx_dict = {tx["id"]: tx for tx in transactions}

def dict_lookup(tx_dict, target_id):
    return tx_dict.get(target_id, None)

# -------------------------
# Performance Measurement
# -------------------------
def measure_performance():
    test_ids = [tx["id"] for tx in transactions[:20]]

    # Linear Search Time
    start_linear = time.time()
    for tid in test_ids:
        linear_search(transactions, tid)
    end_linear = time.time()

    # Dictionary Lookup Time
    start_dict = time.time()
    for tid in test_ids:
        dict_lookup(tx_dict, tid)
    end_dict = time.time()

    linear_time = end_linear - start_linear
    dict_time = end_dict - start_dict

    print("Performance Comparison (20 records):")
    print(f"Linear Search Time: {linear_time:.8f} seconds")
    print(f"Dictionary Lookup Time: {dict_time:.8f} seconds")

    return linear_time, dict_time


if __name__ == "__main__":
    measure_performance()
