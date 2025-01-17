-- Nomor 1
CREATE DATABASE ata_online_shop;
USE ata_online_shop;

-- Nomor 2
CREATE TABLE users (
id INT(11) NOT NULL AUTO_INCREMENT,
status SMALLINT NOT NULL,
dob DATE NOT NULL,
gender CHAR(1) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

CREATE TABLE product_types (
id INT(11) NOT NULL AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

CREATE TABLE operators (
id INT(11) NOT NULL AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

CREATE TABLE products (
id INT(11) NOT NULL AUTO_INCREMENT,
product_type_id INT(11) NOT NULL,
operator_id INT(11) NOT NULL,
code VARCHAR(50) NOT NULL,
price NUMERIC(25,2) NOT NULL,
name VARCHAR(100) NOT NULL,
status SMALLINT NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (product_type_id) REFERENCES product_types(id),
FOREIGN KEY (operator_id) REFERENCES operators(id));

CREATE TABLE product_descriptions (
id INT(11) NOT NULL AUTO_INCREMENT,
description TEXT NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

CREATE TABLE payment_methods (
id INT(11) NOT NULL AUTO_INCREMENT,
name VARCHAR(255),
status SMALLINT NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

CREATE TABLE transactions (
id INT(11) NOT NULL AUTO_INCREMENT,
user_id INT(11) NOT NULL,
payment_method_id INT(11) NOT NULL,
status VARCHAR(10) NOT NULL,
total_qty INT(11) NOT NULL,
total_price NUMERIC(25,2) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id));

CREATE TABLE transaction_details (
transaction_id INT(11) NOT NULL,
product_id INT(11) NOT NULL,
status VARCHAR(10) NOT NULL,
qty INT(11) NOT NULL,
price NUMERIC(25,2) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (transaction_id,product_id),
FOREIGN KEY (transaction_id) REFERENCES transactions(id),
FOREIGN KEY (product_id) REFERENCES products(id));

-- Nomor 3
CREATE TABLE tabel_kurir (
id INT(11) NOT NULL AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

-- Nomor 4
ALTER TABLE tabel_kurir 
ADD ongkos_dasar INT(11);

-- Nomor 5
ALTER TABLE tabel_kurir
RENAME TO shipping;

-- Nomor 6
DROP TABLE shipping;

-- Nomor 7a.
CREATE TABLE payment_method_description (
id INT(11) NOT NULL AUTO_INCREMENT,
description TEXT NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id));

-- Nomor 7b
CREATE TABLE alamat (
id INT(11) NOT NULL AUTO_INCREMENT,
user_id INT(11) NOT NULL,
detail_alamat TEXT NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (user_id) REFERENCES users(id));

-- Nomor 7c
CREATE TABLE user_payment_method_detail (
user_id INT(11) NOT NULL,
payment_id INT(11) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (user_id,payment_id),
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (payment_id) REFERENCES payment_methods(id));





