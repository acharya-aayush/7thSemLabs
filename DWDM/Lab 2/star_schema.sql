CREATE DATABASE SALES_STAR;

USE SALES_STAR;

CREATE TABLE sales_source (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    sale_date DATE,
    store_location VARCHAR(255),
    units_sold INT,
    revenue DECIMAL(10, 2)
);

INSERT INTO sales_source (product_name, category, sale_date, store_location, units_sold, revenue) VALUES
('Gaming Laptop', 'Electronics', '2026-04-01', 'San Francisco', 8, 12000.00),
('Smartwatch', 'Wearables', '2026-04-10', 'Seattle', 12, 6000.00),
('Wireless Earbuds', 'Audio', '2026-04-15', 'Austin', 20, 4000.00);

CREATE TABLE time_dim (
    t_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE
);

INSERT INTO time_dim (sale_date)
SELECT DISTINCT sale_date FROM sales_source;

CREATE TABLE product_dim (
    p_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255)
);

INSERT INTO product_dim (product_name, category)
SELECT DISTINCT product_name, category FROM sales_source;

CREATE TABLE location_dim (
    l_id INT AUTO_INCREMENT PRIMARY KEY,
    store_location VARCHAR(255)
);

INSERT INTO location_dim (store_location)
SELECT DISTINCT store_location FROM sales_source;

CREATE TABLE sales_fact (
    t_id INT,
    p_id INT,
    l_id INT,
    units_sold INT,
    revenue DECIMAL(10, 2),
    FOREIGN KEY (t_id) REFERENCES time_dim(t_id),
    FOREIGN KEY (p_id) REFERENCES product_dim(p_id),
    FOREIGN KEY (l_id) REFERENCES location_dim(l_id)
);

INSERT INTO sales_fact (t_id, p_id, l_id, units_sold, revenue)
SELECT t.t_id, p.p_id, l.l_id, s.units_sold, s.revenue
FROM sales_source s
LEFT JOIN time_dim t ON t.sale_date = s.sale_date
LEFT JOIN product_dim p ON p.product_name = s.product_name AND p.category = s.category
LEFT JOIN location_dim l ON l.store_location = s.store_location;

SELECT sf.*, t.sale_date
FROM sales_fact sf
LEFT JOIN time_dim t ON t.t_id = sf.t_id
WHERE YEAR(t.sale_date) = 2026;