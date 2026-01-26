CREATE DATABASE IF NOT EXISTS momo_db;
USE momo_db;

SOURCE transaction_categories.sql;
SOURCE users.sql;
SOURCE transactions.sql;
SOURCE transaction_participants.sql;
SOURCE system_logs.sql;
