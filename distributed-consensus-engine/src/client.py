import requests
import time
import random

LEADER = "http://node1:5000"

while True:

    tx = {
        "tx_id": random.randint(10000,99999),
        "amount": random.randint(100,500)
    }

    try:

        response = requests.post(
            LEADER + "/transaction",
            json=tx
        )

        print(response.json())

    except Exception as e:

        print(e)

    time.sleep(3)