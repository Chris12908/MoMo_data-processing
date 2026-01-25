CREATE TABLE transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(40) NOT NULL,
    description TEXT
);

INSERT INTO transaction_categories (category_name, description) VALUES
('Transfer','money sent to another user'),
('Cash In','added money to your account'),
('Cash Out','withdrew money from your account'),
('Bill Pay','paid your bills'),
('Airtime','Bought airtime'),
('Merchant','bought something from a merchant');