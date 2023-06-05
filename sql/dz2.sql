-- Task1. Используя операторы языка SQL, создайте табличку “sales”. Заполните ее данными
DROP DATABASE IF EXISTS dz2;
CREATE DATABASE IF NOT EXISTS dz2;
USE dz2;
DROP TABLE IF EXISTS sales;
CREATE TABLE IF NOT EXISTS sales
(id INT PRIMARY KEY AUTO_INCREMENT,
order_date DATE NOT NULL,
count_product INT NOT NULL);
INSERT INTO sales (order_date, count_product)
VALUES
	('2022-01-01', 156),
	('2022-01-02', 180),
	('2022-01-03', 21),
	('2022-01-04', 124),
	('2022-01-05', 341);
SELECT * FROM sales;

-- Task2. Сгруппируйте значений количества в 3 сегмента — меньше 100, 100-300 и больше 300 (функция IF)
SELECT id AS "id заказа",
	IF (count_product < 100, "Маленький заказ",
		IF (count_product > 300, "Большой заказ", "Средний заказ"))
AS "Тип заказа" FROM sales;

-- Task3. Создайте таблицу “orders”, заполните ее значениями. Покажите “полный” статус заказа, используя оператор CASE
DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS orders
(id INT PRIMARY KEY AUTO_INCREMENT,
employee_id VARCHAR(20) NOT NULL,
amount DECIMAL(9, 2) NOT NULL,
order_status VARCHAR(20) NOT NULL);
INSERT INTO orders (employee_id, amount, order_status)
VALUES
	('e03', 15, 'OPEN'),
	('e01', 25.5, 'OPEN'),
	('e05', 100.7, 'CLOSED'),
	('e02', 22.18, 'OPEN'),
	('e04', 9.5, 'CANCELLED');
SELECT * FROM orders;
SELECT *,
	CASE 
		WHEN order_status = "OPEN" THEN "Order is in open state"
		WHEN order_status = "CLOSED" THEN "Order is closed"
		WHEN order_status = "CANCELLED" THEN "Order is cancelled"
	ELSE "Статус не определен"
	END AS full_order_status
	FROM orders;

-- Task4. Чем NULL отличается от 0?
-- NULL - это специальное значение, которое используется в SQL для обозначения отсутствия данных. 
-- Оно отличается от пустой строки или нулевого значения, так как NULL означает отсутствие какого-либо значения в ячейке таблицы.