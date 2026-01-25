CREATE TABLE user_transactions (
    user_id INT,
    transaction_id INT,
    role ENUM('The sender','The receiver'),
    PRIMARY KEY (user_id, transaction_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
);


INSERT INTO user_transactions VALUES
(1,1,'The sender'),(2,1,'The receiver'),
(2,2,'The sender'),(3,2,'The receiver'),
(3,3,'The sender'),(4,3,'The receiver'),
(4,4,'The sender'),(5,4,'The receiver'),
(5,5,'The sender'),(1,5,'The receiver');