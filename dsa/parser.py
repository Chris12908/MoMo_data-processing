import xml.etree.ElementTree as ET
import json
import re
from datetime import datetime

def extract_amount(text):
    """Extract amount in RWF from SMS body"""
    match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s*RWF', text)
    if match:
        return int(match.group(1).replace(',', ''))
    return None

def extract_sender_receiver(text):
    sender = None
    receiver = None

    # patterns for received money
    rec_match = re.search(r'from ([A-Za-z\s]+)\s*\(', text)
    if rec_match:
        sender = rec_match.group(1).strip()

    # patterns for payment
    pay_match = re.search(r'payment of .* to ([A-Za-z\s]+)\s+\d+', text)
    if pay_match:
        receiver = pay_match.group(1).strip()

    return sender, receiver

def detect_transaction_type(text):
    text = text.lower()
    if "received" in text:
        return "RECEIVED"
    elif "payment" in text:
        return "PAYMENT"
    elif "deposit" in text:
        return "DEPOSIT"
    elif "withdraw" in text:
        return "WITHDRAW"
    else:
        return "UNKNOWN"

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    transactions = []
    tx_id = 1

    for sms in root.findall('sms'):
        body = sms.attrib.get('body', '')
        timestamp = sms.attrib.get('readable_date', '')
        address = sms.attrib.get('address', '')

        amount = extract_amount(body)
        sender, receiver = extract_sender_receiver(body)
        tx_type = detect_transaction_type(body)

        transaction = {
            "id": tx_id,
            "type": tx_type,
            "amount": amount,
            "sender": sender,
            "receiver": receiver,
            "timestamp": timestamp,
            "raw_message": body,
            "service": address
        }

        transactions.append(transaction)
        tx_id += 1

    return transactions


if __name__ == "__main__":
    data = parse_xml("modified_sms_v2.xml")

    # Save as JSON
    with open("transactions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Parsed {len(data)} transactions successfully.")
