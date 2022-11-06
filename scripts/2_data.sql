USE koolf;

INSERT INTO client (client_name,client_phone_number,client_email)
VALUES
    ('Fitzgerald Richmond','732-6577','non.arcu@protonmail.ca'),
    ('Brian Warner','829-1463','nunc.lectus@icloud.edu'),
    ('Reese Haynes','1-332-163-3183','nisi.dictum.augue@aol.couk'),
    ('Martha Parks','420-4767','dui.augue.eu@icloud.com'),
    ('Cameron Spears','1-716-224-0968','tincidunt@outlook.ca');

INSERT INTO deliverable (deliverable_name,deliverable_description,base_price)
VALUES
    ('pede','turpis egestas. Fusce aliquet magna a neque. Nullam ut nisi a odio', 4864.38),
    ('dolor.','vel est tempor bibendum. Donec felis', 2752.91),
    ('dis parturient','egestas nunc sed', 6433.86),
    ('Nullam','Etiam imperdiet dictum magna. Ut tincidunt orci quis lectus. Nullam suscipit,', 9328.90),
    ('consectetuer adipiscing','consectetuer mauris id sapien.', 8771.25);

INSERT INTO orders (order_placement_date,order_fulfillment_date,client_id)
VALUES
  ('2021-12-12 10:13:09','2022-03-23 22:31:57',4),
  ('2021-10-07 16:38:09','2022-01-07 22:32:34',2),
  ('2021-12-26 10:11:15','2022-02-07 21:08:08',3),
  ('2021-11-10 21:41:27','2022-03-08 06:50:40',5),
  ('2021-09-17 10:54:18','2022-01-06 15:35:12',2);

INSERT INTO order_line (order_id,deliverable_id,quantity,specification,price)
VALUES
    (3,4,319,'felis. Nulla tempor augue ac ipsum. Phasellus vitae mauris',0.3),
    (1,2,490,'elementum sem, vitae aliquam', 7456.06),
    (4,4,458,'ut lacus. Nulla tincidunt, neque vitae semper', 4166.39),
    (4,5,99,'Etiam imperdiet dictum magna. Ut tincidunt', 1907.09),
    (4,1,344,'ultricies ligula. Nullam enim. Sed nulla ante, iaculis', 5833.76);


INSERT INTO invoice (invoice_date,status,discount,amount,order_id)
VALUES
    ('2022-06-27 06:24:59',1,1.72, 0.3, 4),
    ('2021-11-25 15:39:42', 1, 8.00 , 7456.06, 1),
    ('2022-05-27 04:10:51', 1, 9.50 , 4166.39, 3),
    ('2022-04-03 07:41:01', 1, 9.44 , 1907.09, 5),
    ('2022-05-05 16:34:48', 0, 0.79 , 5833.76, 2);

INSERT INTO payment (payment_date,payment_type,payment_amount,invoice_id)
VALUES
    ('2022-06-27 06:24:59','Cash',0.37,2),
    ('2021-11-25 15:39:42','Card', 7456.06,2),
    ('2022-05-27 04:10:51','Cheque',4166.39,2),
    ('2022-04-03 07:41:01','Cash',1907.09,2),
    ('2022-05-05 16:34:48','Card',5833.76,2);