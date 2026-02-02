# MoMo SMS REST API Documentation

## Overview
The REST API allows access to Mobile Money SMS transaction data in XML format and stored in a format of>
## Base URL
http://localhost:8000

---

## Endpoints

### GET /transactions
Returns all transactions.

**Response Codes**:
- 200 OK

**Error codes**
404 Not Found

### GET /transactions/{id}
Returns a single transaction by ID.

**Response Codes**:
- 200 OK

**Error codes**
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


##Response Example (created)
{
  "id": 1692,
  "type": "PAYMENT",
  "amount": 3000,
  "sender": "Alice",
  "receiver": "Shop",
  "timestamp": "2024-02-01"
}

#Error codes
400 Bad Request


###PUT /transactions/{id}
Updates an existing transaction by ID.

##Request Example:

```json

{
  "amount": 3500,
  "receiver": "New Shop"
}

##Response Example (200 OK):

{
  "id": 1692,
  "type": "PAYMENT",
  "amount": 3500,
  "sender": "Alice",
  "receiver": "New Shop",
  "timestamp": "2024-02-01"
}



##Error Codes:

400 Bad Request
404 Not Found


###DELETE /transactions/{id}
Deletes a transaction by ID.

##Request Example:
DELETE /transactions/1692 HTTP/2

##Response Example (200 OK):

{
  "message": "Transaction deleted"
}

##Error Codes:

404 Not Found

