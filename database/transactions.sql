CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    currency VARCHAR(5),
    fee DECIMAL(10,2) DEFAULT 0,
    balance DECIMAL(10,2),
    transaction_date DATETIME,
    FOREIGN KEY (category_id) REFERENCES transaction_categories(category_id)
);

INSERT INTO transactions (category_id, amount, currency, fee, balance, transaction_date) VALUES
(1,4000,'RWF',20,15000,NOW()),
(5,3000,'RWF',20,12000,NOW()),
(2,2000,'RWF',20,14000,NOW()),
(3,1000,'RWF',0,13000,NOW()),
(1,7000,'RWF',50,6000,NOW());