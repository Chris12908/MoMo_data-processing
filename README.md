# EWD Group – MoMo data processing Project

# Team Name
EWD Group

## Project Description
This project is a full-stack application designed to process and analyze Mobile Money (MoMo) SMS data provided in XML format. The system will parse, clean, and categorize transaction data, store it in a relational database, and present insights through a simple frontend dashboard with tables and visualizations.

The project focuses on backend data processing (ETL), database management, frontend development, and collaborative software development using Agile practices.

we updated the database to handle mobile money transaction data receives via SMS. The system will store,process and alsp analyse information while maintaining the data integrity and supporting scalability.

# We have the core entities as follows:


Users -  senders and receivers

Transaction Categories - The types of mobile money operations

Transactions - Main transaction records

User_Transaction - The roles of the users in the transaction processes

System Logs - Tracks SMS processing and system activity.

# KEY CHARACTERISTICS

-Fully normalized design (3NF).
-Applied referential intergrity through primary and foreign key constraints.
-Handling sensitive financial data securely using decimal data types.
-Prepared  for future API intergration with JSON serialization.

# Sample functionality

-Fetch transactions along their associated categories.
-Identify participants within transactions.
-Determine the total amounts transmitted by each user.

# Security Rules

-Ensures unique phone numbers for users.
-Ensures valide roles for the senders and receivers.
-prevents false transaction amounts


## Team Members
- Chris Marcel Hakizimana
- Ridaa Isaro
- Ghislaine Marie Ineza
  
Below we have provided the links to the Architecture diagram and the updated Scrum board.

## Architecture Diagram link:
https://drive.google.com/file/d/1NctBSXok1VWAyXqtTaSW2YFQbw4JQwsE/view?usp=sharing
## scrum board link:
https://trello.com/invite/b/6965162b5006fa9fd2eebfdc/ATTI5be015b7274fc3e1d965632481e1d686DF324D4A/ewd-group-momo-data-processing-scrum-board


