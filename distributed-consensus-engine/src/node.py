from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

NODE_ID = None
LEADER_ID = 1

ledger = []
heartbeat_time = time.time()

@app.route("/heartbeat", methods=["POST"])
def heartbeat():
    global heartbeat_time

    heartbeat_time = time.time()

    return jsonify({"status":"ok"})

@app.route("/transaction", methods=["POST"])
def transaction():

    data = request.json

    ledger.append(data)

    return jsonify({
        "status":"committed",
        "ledger_size": len(ledger)
    })

@app.route("/ledger", methods=["GET"])
def get_ledger():

    return jsonify(ledger)

def leader_monitor():

    global LEADER_ID

    while True:

        if time.time() - heartbeat_time > 5:
            print("Leader failure detected")

            LEADER_ID = NODE_ID

            print(f"Node {NODE_ID} elected leader")

        time.sleep(2)

if __name__ == "__main__":

    import os

    NODE_ID = int(os.getenv("NODE_ID","1"))

    threading.Thread(
        target=leader_monitor,
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=5000
    )