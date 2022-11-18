USE koolf;

INSERT INTO client (client_name,client_phone_number,client_email)
VALUES
    ('Tolulope Badmus', '0804-678-1234', 'non.arcu@protonmail.ca'),
    ('Oluwanimi Aflred', '0816-578-0034', 'nunc.lectus@icloud.edu'),
    ('Tobiloba Kokanmi', '0807-078-8834', 'nisi.dictum.augue@aol.couk'),
    ('Winifred Chike', '0800-678-1994', 'dui.augue.eu@icloud.com'),
    ('Ose Johnson', '0812-778-1964', 'tincidunt@outlook.ca');

INSERT INTO deliverable (deliverable_name,deliverable_description,base_price)
VALUES
    ('Radio Advert', 'Advertisement to be played on radio stations', 30000.00),
    ('T-shirt', 'Custom T-shirt with graphic designs', 4000.00),
    ('Cap', 'Custom face cap with graphic designs', 3000.00),
    ('Newspaper Advert', 'Advertisement to be printed in newspapers', 15000.00),
    ('Book', 'Custom book with designs on the book cover', 2500.00);

INSERT INTO orders (order_placement_date,order_fulfillment_date,client_id)
VALUES
    ('2021-12-12 10:13:09', '2021-12-20 22:31:57', 4),
    ('2021-12-26 10:11:15', '2022-01-07 21:08:08', 3),
    ('2022-09-17 10:54:18', '2022-10-01 13:35:12', 2),
    ('2022-10-07 06:38:09', '2022-10-12 22:32:34', 2),
    ('2022-11-10 21:41:27', '2022-12-01 06:50:40', 5);

INSERT INTO order_line (order_id,deliverable_id,quantity,specification,price)
VALUES
    (3, 4, 1, 'A small column at the back of the newspaper for a job vacancy', 17000.00),
    (1, 2, 100, 'Blue T-shirts with a logo', 500000.00),
    (4, 5, 73, 'Books for a birthday party', 182500.00),
    (4, 2, 73, 'Pink T-shirts with cake designs', 365000.00),
    (2, 3, 250, 'Plain black caps', 750000.00),
    (2, 1, 3, 'Front page advert for news', 180000.00),
    (5, 3, 50, 'Green caps with a logo', 200000.00);

INSERT INTO invoice (invoice_date,status,discount,amount,order_id)
VALUES
    ('2021-12-30 15:39:42', 1, 0.00, 500000.00, 1),
    ('2022-01-20 06:24:59', 1, 0.00, 930000.00, 2),
    ('2022-10-01 14:10:51', 1, 0.00, 17000.00, 3),
    ('2022-10-15 17:41:01', 1, 0.00, 547500.00, 4),
    ('2022-12-01 16:34:48', 0, 15.00, 200000.00, 5);

INSERT INTO payment (payment_date,payment_type,payment_amount,invoice_id)
VALUES
    ('2021-12-15 06:24:59', 'Cash', 500000.00, 1),
    ('2021-12-27 15:39:42', 'Card', 500000.00, 2),
    ('2022-01-18 04:10:51', 'Cheque', 430000.00, 2),
    ('2022-09-22 07:41:01', 'Cash', 17000.00, 3),
    ('2022-10-07 07:41:01', 'Cash', 200000.00, 4),
    ('2022-10-11 07:41:01', 'Cash', 200000.00, 4),
    ('2022-10-15 16:34:48', 'Card', 147500.00, 4);