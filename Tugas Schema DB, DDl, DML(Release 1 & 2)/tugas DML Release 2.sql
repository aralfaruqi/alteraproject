USE ata_online_shop;

-- Nomor 1
SELECT *
FROM transactions
WHERE user_id = 1
UNION
SELECT *
FROM transactions
WHERE user_id = 2;

-- Nomor 2
SELECT SUM(total_price) AS 'jumlah harga transaksi user id 1'
FROM transactions
WHERE user_id = 1;

-- Nomor 3
SELECT COUNT(distinct transaction_id) AS 'total transaksi product type 2'
FROM transaction_details 
WHERE product_id IN (SELECT id FROM products WHERE product_type_id = 2);

-- Nomor 4
SELECT products.*,product_types.name AS 'tipe product' FROM products
INNER JOIN product_types
ON products.product_type_id = product_types.id;

-- Nomor 5
SELECT transactions.*,users.name,products.name
FROM transactions
LEFT JOIN transaction_details
ON transactions.id = transaction_details.transaction_id
LEFT JOIN products
ON transaction_details.product_id = products.id
LEFT JOIN users
ON transactions.user_id = users.id;

-- Nomor 6
DELIMITER $$
CREATE TRIGGER delete_all_data_transactions
BEFORE DELETE ON transactions FOR EACH ROW
BEGIN
-- declare variables 
DECLARE v_transactions_id INT;
SET v_transactions_id = OLD.id;
-- trigger code
DELETE FROM transaction_details WHERE transaction_id=v_transactions_id;
END $$
DELIMITER ;

-- Nomor 7
DELIMITER $$
CREATE TRIGGER update_all_data_total_qty
AFTER DELETE ON transaction_details FOR EACH ROW
BEGIN
-- declare variables 
DECLARE v_qty INT; 
DECLARE v_transaction_id INT;
SET v_qty = OLD.qty;
SET v_transaction_id = OLD.transaction_id;
-- trigger code
UPDATE transactions
SET total_qty = total_qty - v_qty
WHERE id = v_transaction_id; 
END $$
DELIMITER ;

-- Nomor 8
SELECT * 
FROM products 
WHERE id NOT IN (SELECT product_id FROM transaction_details GROUP BY product_id);