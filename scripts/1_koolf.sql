CREATE SCHEMA `koolf`;

USE `koolf`;

-- client: table
CREATE TABLE IF NOT EXISTS `client` (
    `client_id` int NOT NULL AUTO_INCREMENT,
    `client_name` varchar(255) NOT NULL,
    `client_phone_number` varchar(50) NOT NULL,
    `client_email` varchar(255) NOT NULL,
    `date_joined` datetime DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`client_id`),
    UNIQUE KEY `unique_email` (`client_email`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- deliverable: table
CREATE TABLE IF NOT EXISTS `deliverable` (
    `deliverable_id` int NOT NULL AUTO_INCREMENT,
    `deliverable_name` varchar(255) NOT NULL,
    `deliverable_description` text NOT NULL,
    `base_price` decimal(15,2) DEFAULT NULL,
    PRIMARY KEY (`deliverable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- invoice: table
CREATE TABLE IF NOT EXISTS `invoice` (
    `invoice_id` int NOT NULL AUTO_INCREMENT,
    `invoice_date` datetime NOT NULL,
    `status` tinyint(1) DEFAULT '0',
    `discount` decimal(5,2) DEFAULT NULL,
    `amount` decimal(15,2) NOT NULL,
    `order_id` int NOT NULL,
    PRIMARY KEY (`invoice_id`),
    KEY `invoice_order_null_fk` (`order_id`),
    CONSTRAINT `invoice_order_null_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- order_line: table
CREATE TABLE IF NOT EXISTS `order_line` (
    `order_line_id` int NOT NULL AUTO_INCREMENT,
    `order_id` int NOT NULL,
    `quantity` int NOT NULL,
    `specification` text,
    `price` decimal(15,2) NOT NULL,
    `deliverable_id` int NOT NULL,
    PRIMARY KEY (`order_line_id`),
    KEY `order_line_deliverable_null_fk` (`deliverable_id`),
    KEY `order_line_order_null_fk` (`order_id`),
    CONSTRAINT `order_line_deliverable_null_fk` FOREIGN KEY (`deliverable_id`) REFERENCES `deliverable` (`deliverable_id`),
    CONSTRAINT `order_line_order_null_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- orders: table
CREATE TABLE IF NOT EXISTS `orders` (
    `order_id` int NOT NULL AUTO_INCREMENT,
    `order_placement_date` datetime DEFAULT CURRENT_TIMESTAMP,
    `order_fulfillment_date` datetime DEFAULT NULL,
    `client_id` int NOT NULL,
    PRIMARY KEY (`order_id`),
    KEY `order_client_null_fk` (`client_id`),
    CONSTRAINT `order_client_null_fk` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- payment: table
CREATE TABLE IF NOT EXISTS `payment` (
    `payment_id` int NOT NULL AUTO_INCREMENT,
    `payment_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `payment_amount` decimal(15,2) NOT NULL,
    `payment_type` varchar(20) NOT NULL,
    `invoice_id` int NOT NULL,
    PRIMARY KEY (`payment_id`),
    KEY `payment_invoice_null_fk` (`invoice_id`),
    CONSTRAINT `payment_invoice_null_fk` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`invoice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

