-- Nomor 1a
INSERT INTO operators (name)
VALUES ('Flexi'),('Esia'),('Indosat'),('Telkomsel'),('Axis');

-- Nomor 1b
INSERT INTO product_types (name)
VALUES ('Paket data'),('Pulsa'),('Kartu Perdana');

-- Nomor 1c
INSERT INTO products (product_type_id,operator_id,code,price,name,status)
VALUES (1,3,'IND_DATA_MALAM',50000.00,'Paket Malam',1),
(1,3,'IND_DATA_PUAS',100000.00,'Paket Data Sepuasnya',1);

-- Nomor 1d
INSERT INTO products (product_type_id,operator_id,code,price,name,status)
VALUES (2,1,'FLE_PULSA_50000',50000.00,'Pulsa 50000',1),
(2,1,'FLE_PULSA_20000',20000.00,'Pulsa 20000',1),
(2,1,'FLE_PULSA_10000',10000.00,'Pulsa 10000',1);

-- Nomor 1e
INSERT INTO products (product_type_id,operator_id,code,price,name,status)
VALUES (3,4,'TEL_PERDANA_50000',50000.00,'Perdana 50000',1),
(3,4,'TEL_PERDANA_20000',20000.00,'Perdana 20000',1),
(3,4,'TEL_PERDANA_10000',10000.00,'Perdana 10000',1);

-- Nomor 1f
INSERT INTO product_descriptions (description)
VALUES ('Paket indosat data malam'),('Paket indosat data sepuasnya'),
('Pulsa Flexi 50000'),('Pulsa Flexi 20000'),('Pulsa Flexi 10000'),
('Perdana Telkomsel 50000'),('Perdana Telkomsel 20000'),('Perdana Telkomsel 10000');

-- Nomor 1g
INSERT INTO payment_methods (name,status)
VALUES ('ATM',1),('Gopay',1),('DANA',1);

-- Nomor 1h
INSERT INTO users (status,dob,gender)
VALUES (1,'1997-03-01','m'),(1,'1997-03-02','f'),(1,'1997-03-03','f'),
(1,'1997-03-04','m'),(1,'1997-03-05','m');

-- Nomor 1i
INSERT INTO transactions (user_id,payment_method_id,status,total_qty,total_price)
VALUES (1,1,'sukses',3,80000),(1,1,'sukses',1,80000),(1,1,'sukses',1,80000),
(2,1,'sukses',1,80000),(2,1,'sukses',1,80000),(2,1,'sukses',1,80000),
(3,1,'sukses',1,80000),(3,1,'sukses',1,80000),(3,1,'sukses',1,80000),
(4,1,'sukses',1,80000),(4,1,'sukses',1,80000),(4,1,'sukses',1,80000),
(5,1,'sukses',1,80000),(5,1,'sukses',1,80000),(5,1,'sukses',1,80000);

-- Nomor 1j
INSERT INTO transaction_details(transaction_id,product_id,status,qty,price)
VALUES (1,3,'sukses',1,50000),(1,4,'sukses',1,20000),(1,5,'sukses',1,10000),
(2,3,'sukses',1,50000),(2,4,'sukses',1,20000),(2,5,'sukses',1,10000),
(3,3,'sukses',1,50000),(3,4,'sukses',1,20000),(3,5,'sukses',1,10000),
(4,3,'sukses',1,50000),(4,4,'sukses',1,20000),(4,5,'sukses',1,10000),
(5,3,'sukses',1,50000),(5,4,'sukses',1,20000),(5,5,'sukses',1,10000),
(6,3,'sukses',1,50000),(6,4,'sukses',1,20000),(6,5,'sukses',1,10000),
(7,3,'sukses',1,50000),(7,4,'sukses',1,20000),(7,5,'sukses',1,10000),
(8,3,'sukses',1,50000),(8,4,'sukses',1,20000),(8,5,'sukses',1,10000),
(9,3,'sukses',1,50000),(9,4,'sukses',1,20000),(9,5,'sukses',1,10000),
(10,3,'sukses',1,50000),(10,4,'sukses',1,20000),(10,5,'sukses',1,10000),
(11,3,'sukses',1,50000),(11,4,'sukses',1,20000),(11,5,'sukses',1,10000),
(12,3,'sukses',1,50000),(12,4,'sukses',1,20000),(12,5,'sukses',1,10000),
(13,3,'sukses',1,50000),(13,4,'sukses',1,20000),(13,5,'sukses',1,10000),
(14,3,'sukses',1,50000),(14,4,'sukses',1,20000),(14,5,'sukses',1,10000),
(15,3,'sukses',1,50000),(15,4,'sukses',1,20000),(15,5,'sukses',1,10000);

-- Nomor 2a
ALTER TABLE users
ADD COLUMN name VARCHAR(255);

UPDATE users 
SET name='Anto'
WHERE id =1;

UPDATE users 
SET name='Bento'
WHERE id =2;

UPDATE users 
SET name='Canto'
WHERE id =3;

UPDATE users 
SET name='Danto'
WHERE id =4;

UPDATE users 
SET name='Eanto'
WHERE id =5;

SELECT name
FROM users
WHERE gender = 'm';

-- Nomor 2b
SELECT name
FROM products
WHERE id = 3;

-- Nomor 2c
SELECT name
FROM users
WHERE created_at < round(now())-7;

-- Nomor 2d
SELECT COUNT(*)
FROM users
WHERE gender = 'f';

-- Nomor 2e
SELECT name
FROM users
ORDER BY name ASC;

-- Nomor 2f
SELECT *
FROM transaction_details
WHERE product_id=3
LIMIT 5;

-- Nomor 3a
UPDATE products
SET name = 'product dummy'
WHERE id = 1;

-- Nomor 3b
UPDATE transaction_details
SET qty = 3
WHERE product_id = 1;

-- Nomor 4a
DELETE FROM transaction_details
WHERE product_id = 1;

DELETE FROM product_descriptions
WHERE id = 1;

DELETE FROM products
WHERE id = 1;

-- Nomor 4b
SELECT *
FROM products; -- Melihat product where product_type_id = 1

DELETE FROM transaction_details
WHERE product_id = 2;

DELETE FROM product_descriptions
WHERE id = 2;

DELETE FROM products
WHERE product_type_id = 1;







