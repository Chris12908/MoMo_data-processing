# MoMo SMS REST API Documentation

## Overview
This REST API provides access to Mobile Money SMS transaction data parsed from XML and stored in JSON format.

## Base URL
http://localhost:8000

---

## Endpoints

### GET /transactions
Returns all transactions.

**Response Codes**: 
- 200 OK

---

### GET /transactions/{id}
Returns a single transaction by ID.

**Response Codes**: 
- 200 OK 
- 404 Not Found

---

### POST /transactions
Creates a new transaction.

**Request Body Example**:

```json
{
  "type": "PAYMENT",
  "amount": 3000,
  "sender": "Alice",
  "receiver": "Shop",
  "timestamp": "2024-02-01"
}

