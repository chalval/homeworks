-- IF EXISTS - проверка на наличие таблицы или любого другого объекта.
-- Таким образом можно запускать скрипт без ошибки о том, что объект уже создан.
-- IF NOT EXISTS - проверка на отсутсвие объекта
DROP DATABASE IF EXISTS dz2;
CREATE DATABASE IF NOT EXISTS dz2;
USE dz2;
CREATE TABLE IF NOT EXISTS tbl (id INT(8));
-- Создадим таблицу, если ранее такой же не существовало
INSERT INTO tbl VALUES (5);
SELECT * FROM tbl;
DROP TABLE IF EXISTS tbl; -- Удалить таблицу tbl, если она существует
CREATE TABLE tbl (id INT(3));
INSERT INTO tbl VALUES (55555);
INSERT INTO tbl VALUES (500000000);

DESCRIBE tbl; -- Получим информацию о столбцах
ALTER TABLE tbl ADD collect JSON; -- Добавили столбец "collect" с типом JSON
-- DESCRIBE tbl; -- Получим информацию о столбцах с нвоым столбцом "collect"

INSERT INTO tbl VALUES(1, '{"first": "Hello", "second": "World"}');
-- Пара ключ ключ:значение
SELECT * FROM tbl;
SELECT collect->>"$.first" FROM tbl; -- Получить значение по ключу "first" - "Hello"
SELECT collect->>"$.second" FROM tbl; -- Получить значение по ключу "second" - "World"

-- CURRENT_TIMESTAMP возвращает текущую дату и время
-- COMMENT - комментарий к объекту
DROP TABLE IF EXISTS products;
CREATE TABLE products (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255) COMMENT 'Название',
description TEXT COMMENT 'Описание',
price DECIMAL (11,2) COMMENT 'Цена',
catalog_id INT UNSIGNED,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Товарные позиции';
INSERT INTO products
(name, description, price, catalog_id)
VALUES
('Intel Core i3-8100', 'Процессор для настольных персональных компьютеров,
основанных на платформе Intel.', 7890.00, 1),
('Intel Core i5-7400', 'Процессор для настольных персональных компьютеров,
основанных на платформе Intel.', 12700.00, 1),
('AMD FX-8320E', 'Процессор для настольных персональных компьютеров,
основанных на платформе AMD.', 4780.00, 1),
('AMD FX-8320', 'Процессор для настольных персональных компьютеров, основанных
на платформе AMD.', 7120.00, 1),
('ASUS ROG MAXIMUS X HERO', 'Материнская плата ASUS ROG MAXIMUS X HERO, Z370,
Socket 1151-V2, DDR4, ATX', 19310.00, 2),
('Gigabyte H310M S2H', 'Материнская плата Gigabyte H310M S2H, H310, Socket
1151-V2, DDR4, mATX', 4790.00, 2),
('MSI B250M GAMING PRO', 'Материнская плата MSI B250M GAMING PRO, B250, Socket
1151, DDR4, mATX', 5060.00, 2);
CREATE TABLE users (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255) COMMENT 'Имя покупателя',
birthday_at DATE COMMENT 'Дата рождения',
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';
INSERT INTO users (name, birthday_at)
VALUES
('Геннадий', '1990-10-05'),
('Наталья', '1984-11-12'),
('Александр', '1985-05-20'),
('Сергей', '1988-02-14'),
('Иван', '2001-01-12'),
('Мария', '2002-08-29');

SELECT * FROM products, users;

SELECT * FROM products ORDER BY id; -- Запрос сортирует результат выборки по полю id
-- Чтобы отсортировать таблицу по каталогам,
-- в рамках каждого каталога, по цене, мы можем указать
-- после ключевого слова ORDER BY сначала поле catalog_id, а затем поле price:
SELECT id, catalog_id, price, name FROM products ORDER BY catalog_id, price;

SELECT id, catalog_id, price, name
FROM products
ORDER BY catalog_id DESC, price DESC;

SELECT * FROM products
ORDER BY name
-- LIMIT 2 OFFSET 2;
LIMIT 2, 2;

SELECT DISTINCT catalog_id FROM products ORDER BY catalog_id;
-- задача вывода уникальных значений из таблицы

/* SELECT столбцы
FROM таблица
[WHERE условие_фильтрации_строк]
[GROUP BY столбцы_для_группировки]
[HAVING условие_фильтрации_групп]
[ORDER BY столбцы_для_сортировки]  */
SELECT DISTINCT catalog_id FROM products ORDER BY catalog_id;
-- Группировка данных через GROUP BY
SELECT catalog_id FROM products GROUP BY catalog_id;

SELECT id, name, SUBSTRING(birthday_at, 1, 3) as 'm' FROM users;

SELECT
id, name,
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
ORDER BY decade;

SELECT COUNT(*),
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
GROUP BY decade;

SELECT
COUNT(*),
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
GROUP BY decade
ORDER BY decade DESC;

SELECT
COUNT(*) AS total,
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
GROUP BY decade
ORDER BY total DESC;

SELECT
GROUP_CONCAT(name),
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
GROUP BY decade;

SELECT
GROUP_CONCAT(name SEPARATOR ' '),
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
GROUP BY decade;

SELECT
GROUP_CONCAT(name ORDER BY name DESC SEPARATOR ' '),
SUBSTRING(birthday_at, 1, 3) AS decade
FROM users
GROUP BY decade;

SELECT
catalog_id,
COUNT(*) AS total
FROM products
GROUP BY catalog_id;

SELECT
MIN(price) AS min,
MAX(price) AS max
FROM products;

-- SUM(price) / COUNT(price)

SELECT
AVG(price) AS "Средняя цена через AVG",
SUM(price) AS "Сумма товаров через SUM",
COUNT(price) AS "Количество всех товаров через COUNT",
SUM(price) / COUNT(price) AS "Проверка ср. арифм"
FROM products;









