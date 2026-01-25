CREATE TABLE system_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    sms_text TEXT,
    processed_status ENUM('Successfully completed','process failed','still pending'),
    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
);

INSERT INTO system_logs (transaction_id, sms_text, processed_status) VALUES
(1,'You successfully sent 5000 RWF to FIZZO','Successfully completed'),
(2,'You successfully sent 3000 RWF to JAY Z','Successfully completed'),
(3,'Cash in of 2000 RWF','Successfully completed'),
(4,'You successfully paid 1000 RWF','Successfully completed'),
(5,'Transaction process failed','process failed');