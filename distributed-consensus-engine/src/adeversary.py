import requests
import random
import time

TARGETS = [
    "http://node1:5000",
    "http://node2:5000",
    "http://node3:5000"
]

while True:

    fake_tx = {
        "id": random.randint(1,1000),
        "amount": random.randint(1000,5000),
        "tampered": True
    }

    try:

        requests.post(
            random.choice(TARGETS)+"/transaction",
            json=fake_tx
        )

        print("Sent malicious transaction")

    except:
        pass

    time.sleep(10)