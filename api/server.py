from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import base64

DATA_FILE = os.path.join("dsa", "transactions.json")
USERNAME = "admin"
PASSWORD = "password"

def load_transactions():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_transactions(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
def check_auth(self):
    if not is_autheticated (self.headers):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="MoMo API"')
        self.end_headers()
        self.wfile.write(b"unauthorized")
        return false
        return true
            

class MoMoAPIHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    # GET
    def do_GET(self):
        if not self.check_auth():
            return
            
        transactions = load_transactions()

        if self.path == "/transactions":
            self.send_json(transactions)

        elif self.path.startswith("/transactions/"):
            try:
                tx_id = int(self.path.split("/")[-1])
                tx = next((t for t in transactions if t["id"] == tx_id), None)

                if tx:
                    self.send_json(tx)
                else:
                    self.send_json({"error": "Transaction not found"}, 404)
            except ValueError:
                self.send_json({"error": "Invalid ID"}, 400)
        else:
            self.send_json({"error": "Endpoint not found"}, 404)

    # POST
    def do_POST(self):
        if not self.check_auth():
            return
            
        if self.path == "/transactions":
            transactions = load_transactions()

            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body)

            new_id = max(tx["id"] for tx in transactions) + 1
            data["id"] = new_id

            transactions.append(data)
            save_transactions(transactions)

            self.send_json(data, 201)

    # PUT
    def do_PUT(self):
        if not self.check_auth():
            return
            
        if self.path.startswith("/transactions/"):
            try:
                tx_id = int(self.path.split("/")[-1])
                transactions = load_transactions()

                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                updated_data = json.loads(body)

                for tx in transactions:
                    if tx["id"] == tx_id:
                        tx.update(updated_data)
                        save_transactions(transactions)
                        self.send_json(tx)
                        return

                self.send_json({"error": "Transaction not found"}, 404)
            except ValueError:
                self.send_json({"error": "Invalid ID"}, 400)

    # DELETE
    def do_DELETE(self):
        if not self.check_auth():
            return
            
        if self.path.startswith("/transactions/"):
            try:
                tx_id = int(self.path.split("/")[-1])
                transactions = load_transactions()

                for i, tx in enumerate(transactions):
                    if tx["id"] == tx_id:
                        transactions.pop(i)
                        save_transactions(transactions)
                        self.send_json({"message": "Transaction deleted"})
                        return

                self.send_json({"error": "Transaction not found"}, 404)
            except ValueError:
                self.send_json({"error": "Invalid ID"}, 400)

def run():
    server = HTTPServer(("localhost", 8000), MoMoAPIHandler)
    print("API running at http://localhost:8000")
    server.serve_forever()

if __name__ == "__main__":
    run()

