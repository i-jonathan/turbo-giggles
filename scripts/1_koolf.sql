CREATE SCHEMA `koolf`;
USE `koolf`;
CREATE TABLE client (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_phone_number VARCHAR(50) NOT NULL,
    client_email VARCHAR(255) NOT NULL,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_email UNIQUE (client_email)
);
CREATE TABLE deliverable (
     deliverable_id INT AUTO_INCREMENT PRIMARY KEY,
     deliverable_name VARCHAR(255) NOT NULL,
     deliverable_description TEXT NOT NULL,
     base_price DECIMAL(15, 2)
);
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_placement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_fulfillment_date TIMESTAMP,
    client_id INT,
    CONSTRAINT order_client_null_fk FOREIGN KEY (client_id) REFERENCES client (client_id)
);
CREATE TABLE order_line (
    order_line_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    quantity INT NOT NULL,
    specification TEXT,
    price DECIMAL(15, 2) NOT NULL,
    deliverable_id INT,
    CONSTRAINT order_line_deliverable_null_fk FOREIGN KEY (deliverable_id) REFERENCES deliverable (deliverable_id),
    CONSTRAINT order_line_order_null_fk FOREIGN KEY (order_id) REFERENCES orders (order_id)
);
CREATE TABLE invoice (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_date TIMESTAMP NOT NULL,
    status tinyINT(1) DEFAULT 0,
    discount DECIMAL(5, 2),
    amount DECIMAL(15, 2) NOT NULL,
    order_id INT,
    CONSTRAINT invoice_order_null_fk FOREIGN KEY (order_id) REFERENCES orders (order_id)
);
CREATE TABLE payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    payment_amount DECIMAL(15, 2) NOT NULL,
    payment_type VARCHAR(20) NOT NULL,
    invoice_id INT,
    CONSTRAINT payment_invoice_null_fk FOREIGN KEY (invoice_id) REFERENCES invoice (invoice_id)
);
