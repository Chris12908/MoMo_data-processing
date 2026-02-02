# EWD Group – MoMo Data Processing Project

## Team Name
**EWD Group**

## Team Members
* Chris Marcel Hakizimana
* Ridaa Isaro
* Ghislaine Marie Ineza

---

## Project Description

This project is a comprehensive Mobile Money (MoMo) transaction processing system that includes:

1. **XML Data Parsing**: Converts SMS transaction records from XML format to JSON
2. **REST API**: Secure CRUD endpoints for transaction management
3. **Authentication**: Basic Authentication security layer
4. **Data Structures & Algorithms**: Performance comparison between linear search and dictionary lookup
5. **Database Management**: Normalized relational database (3NF) for transaction data
6. **API Documentation**: Complete endpoint specifications and usage examples

The system processes Mobile Money SMS data, stores it in a relational database, and provides a RESTful API for accessing and managing transaction records.

---

## System Architecture

### Core Entities
- **Users**: Senders and receivers of transactions
- **Transaction Categories**: Types of mobile money operations
- **Transactions**: Main transaction records with amounts, timestamps, and participants
- **User_Transaction**: User roles in transaction processes
- **System Logs**: Tracks SMS processing and system activity

### Key Characteristics
- ✅ Fully normalized design (3NF)
- ✅ Referential integrity through primary and foreign key constraints
- ✅ Secure handling of financial data using decimal data types
- ✅ RESTful API with JSON serialization
- ✅ Basic Authentication for endpoint security

### Security Features
- Ensures unique phone numbers for users
- Validates sender and receiver roles
- Prevents invalid transaction amounts
- Basic Authentication for API access (username/password)

---

## Project Structure
```
MoMo_data-processing/
│
├── api/
│   └── api_server.py              # REST API server implementation
│
├── dsa/
│   ├── parse_xml.py               # XML to JSON parser
│   ├── search_algorithms.py       # Linear search vs Dictionary lookup comparison
│   └── transactions.json          # Parsed transaction data
│
├── docs/
│   └── api_docs.md                # Complete API documentation
│
├── screenshots/
│   ├── 01_successful_get_with_auth.png
│   ├── 02_unauthorized_wrong_credentials.png
│   ├── 03_successful_post.png
│   ├── 04_successful_put.png
│   └── 05_successful_delete.png
│
├── data/
│   └── modified_sms_v2.xml        # Original SMS transaction data
│
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git
- curl or Postman (for API testing)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd MoMo_data-processing
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:
```bash
pip install requests
```

### 3. Parse XML Data

Convert the XML SMS data to JSON format:
```bash
cd dsa
python parse_xml.py
```

This creates `transactions.json` file with all parsed transactions.

### 4. Start the API Server
```bash
cd api
python api_server.py
```

You should see:
```
Starting server on port 8000...
Server running at http://localhost:8000
```

**Keep this terminal window open** while testing the API.

### 5. Test the API

Open a new terminal and run test commands:

#### Test Authentication (should fail)
```bash
curl -v -X GET http://localhost:8000/transactions
```

#### Get All Transactions (with auth)
```bash
curl -v -X GET http://localhost:8000/transactions -u admin:password
```

#### Create New Transaction
```bash
curl -v -X POST http://localhost:8000/transactions \
  -u admin:password \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_type": "Send Money",
    "amount": 10000,
    "sender": "0712345678",
    "receiver": "0723456789",
    "timestamp": "2024-02-02 14:30:00"
  }'
```

#### Update Transaction
```bash
curl -v -X PUT http://localhost:8000/transactions/1 \
  -u admin:password \
  -H "Content-Type: application/json" \
  -d '{"amount": 15000}'
```

#### Delete Transaction
```bash
curl -v -X DELETE http://localhost:8000/transactions/1 \
  -u admin:password
```

---

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/transactions` | List all transactions | Yes |
| GET | `/transactions/{id}` | Get single transaction | Yes |
| POST | `/transactions` | Create new transaction | Yes |
| PUT | `/transactions/{id}` | Update transaction | Yes |
| DELETE | `/transactions/{id}` | Delete transaction | Yes |

### Authentication
- **Type**: Basic Authentication
- **Username**: `admin`
- **Password**: `password`

**Note**: Basic Auth is used for educational purposes. Production systems should use JWT or OAuth2.

---

## Data Structures & Algorithms

The project includes performance comparison between two search methods:

### Linear Search - O(n)
Scans through the list sequentially to find a transaction by ID.

### Dictionary Lookup - O(1)
Uses Python dictionary with transaction ID as key for instant access.

### Run DSA Comparison
```bash
cd dsa
python search_algorithms.py
```

**Results**: Dictionary lookup is significantly faster for large datasets (constant time vs linear time).

---

## API Documentation

Complete API documentation with request/response examples is available in:
```
docs/api_docs.md
```

Includes:
- Endpoint specifications
- Request examples
- Response examples
- Error codes
- Authentication details

---

## Testing & Validation

Test screenshots demonstrating all CRUD operations are located in:
```
screenshots/
```

Screenshots include:
1. Successful GET with authentication (200 OK)
2. Unauthorized request with wrong credentials (401)
3. Successful POST operation (201 Created)
4. Successful PUT operation (200 OK)
5. Successful DELETE operation (200 OK)

---

## Security Considerations

### Current Implementation
- **Basic Authentication**: Simple username/password validation
- **Limitations**: Credentials sent in base64 (easily decoded)

### Recommended Improvements
1. **JWT (JSON Web Tokens)**: Stateless authentication with expiring tokens
2. **OAuth2**: Industry-standard authorization framework
3. **HTTPS**: Encrypt all data in transit
4. **Password Hashing**: Store hashed passwords (bcrypt, argon2)
5. **Rate Limiting**: Prevent brute-force attacks
6. **API Keys**: For service-to-service communication

---

## Database Schema

### Sample Functionality
- Fetch transactions with associated categories
- Identify participants in transactions
- Calculate total amounts transmitted by each user
- Track transaction history with timestamps

---

## Resources

### Architecture Diagram
[View Architecture Diagram](https://drive.google.com/file/d/1NctBSXok1VWAyXqtTaSW2YFQbw4JQwsE/view?usp=sharing)

### Scrum Board
[View Trello Board](https://trello.com/invite/b/6965162b5006fa9fd2eebfdc/ATTI5be015b7274fc3e1d965632481e1d686DF324D4A/ewd-group-momo-data-processing-scrum-board)

---

## Troubleshooting

### Server won't start
- Check if port 8000 is already in use
- Verify Python version: `python --version`
- Check for syntax errors in API code

### 401 Unauthorized errors
- Verify credentials: username=`admin`, password=`password`
- Check Authorization header is being sent

### 404 Not Found errors
- Verify transaction ID exists
- Check endpoint URL is correct

### Connection Refused
- Ensure API server is running
- Check server is listening on port 8000

---

## Contributing

This is a team project following Agile/Scrum methodology. All team members contribute to:
- Backend development
- API implementation
- Database design
- Testing and documentation
- Code reviews

---

## License

This project is created for educational purposes as part of a university assignment.

---

## Contact

For questions or issues, please contact any team member:
- Chris Marcel Hakizimana
- Ridaa Isaro
- Ghislaine Marie Ineza

---

**Last Updated**: February 2, 2026
