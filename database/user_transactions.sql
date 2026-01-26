CREATE TABLE transaction_participants (
    transaction_id INT NOT NULL,
    user_id INT NOT NULL,
    role ENUM('the sender','the receiver') NOT NULL,

    PRIMARY KEY (transaction_id, user_id),

    CONSTRAINT fk_tp_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES transactions(transaction_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_tp_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO transaction_participants VALUES
(1,1,'the sender'),(1,2,'the receiver'),
(2,2,'the sender'),(2,3,'the receiver'),
(3,3,'the sender'),(3,4,'the receiver'),
(4,4,'the sender'),(4,5,'the receiver'),
(5,5,'the sender'),(5,1,'the receiver');