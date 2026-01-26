CREATE TABLE system_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT NOT NULL,
    sms_text TEXT,
    processed_status VARCHAR(20),
    log_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_logs_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES transactions(transaction_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO system_logs (transaction_id, sms_text, processed_status) VALUES
(1,'You successfully sent 5000 RWF','Completed'),
(2,'You successfully sent 3000 RWF','Completed'),
(3,'Cash in of 2000 RWF','Completed'),
(4,'Bill payment of 1000 RWF','Completed'),
(5,'Transaction failed','Failed');