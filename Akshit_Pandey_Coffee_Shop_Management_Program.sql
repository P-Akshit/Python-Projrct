CREATE DATABASE coffee_shop;

USE coffee_shop;

CREATE TABLE  coffee_order(
    order_id int not null auto_increment,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    customer_name VARCHAR(20),
    robo_name VARCHAR (10),
    quantity_of_coffee int,
    coffee_type VARCHAR(20),
    cream_yes_or_no VARCHAR(5),
    payment_mode VARCHAR(10),
    total_amount int
);

SELECT * FROM coffee_order;