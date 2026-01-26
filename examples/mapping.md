# SQL to JSON Mapping
Here's how our database tables transform into JSON for APIs:
Categories (transaction_categories → category)

Stores transaction types like "Mobile Recharge" or "Bill Payment"
Fields: category_id, category_name, description

Users (users → user)

Customer information for senders and receivers
Fields: user_id, username, phone_number

Transactions (transactions → transaction)

Main transaction records with amount, fees, and balance
The datetime field becomes an ISO string (e.g., "2024-01-26T14:30:00Z")
Can include nested category details instead of just category_id

Participants (user_transaction → participants array)

Shows who's involved in each transaction (sender/receiver)
Appears as an array of users with their roles

Logs (system_logs → system_logs)

Tracks SMS processing status and timestamps
Helps monitor system performance

Key Difference: SQL splits data across tables linked by IDs, while JSON nests related information together in one response.