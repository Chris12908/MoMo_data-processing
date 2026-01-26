CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    amount DECIMAL(15,2) NOT NULL CHECK (amount > 0),
    currency VARCHAR(3) NOT NULL,
    fee DECIMAL(15,2) DEFAULT 0,
    balance DECIMAL(15,2),
    transaction_date DATETIME NOT NULL,
    service_center VARCHAR(50),
    status VARCHAR(20),

    CONSTRAINT fk_transactions_category
        FOREIGN KEY (category_id)
        REFERENCES transaction_categories(category_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

INSERT INTO transactions
(category_id, amount, currency, fee, balance, transaction_date, service_center, status)
VALUES
(1,4000,'RWF',20,15000,NOW(),'MTN','Completed'),
(5,3000,'RWF',20,12000,NOW(),'MTN','Completed'),
(2,2000,'RWF',20,14000,NOW(),'MTN','Completed'),
(3,1000,'RWF',0,13000,NOW(),'MTN','Completed'),
(1,7000,'RWF',50,6000,NOW(),'MTN','Failed');