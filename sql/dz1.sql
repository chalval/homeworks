# Task 1. Создайте таблицу с мобильными телефонами, 
# используя графический интерфейс. Заполните БД данными

CREATE DATABASE dz1;
USE dz1;
CREATE TABLE mobil
(id INT PRIMARY KEY NOT NULL,
model VARCHAR(30) NOT NULL,
producer VARCHAR(30) NOT NULL,
price INT NOT NULL,
amount INT NOT NULL
);
INSERT mobil(id, model, producer, price, amount)
VALUES
(10, "Iphone 13 128GB Blue", "Apple", 59000, 3),
(20, "Galaxy S21 FE 8+ 256Gb", "Samsung", 47800, 5),
(30, "GT Master Edition 6/128Gb", "Realme", 24800, 1),
(40, "Samsung Galaxy A73 5G 256Gb", "Samsung", 37400, 2),
(50, "Redmi 9A 2/32GB blue", "Xiaomi", 4900, 2);

# Task 2. Выведите название, производителя и цену 
# для товаров, количество которых превышает 2
SELECT model, producer, price FROM mobil WHERE amount > 2;

# Task 3. Выведите весь ассортимент товаров марки “Samsung”
SELECT * FROM mobil WHERE producer LIKE "Samsung";

# Task 4. С помощью регулярных выражений найти:
# 4.1. Товары, в которых есть упоминание "Iphone"
SELECT * FROM mobil WHERE model LIKE "%Iphone%";

# 4.2. Товары, в которых есть упоминание "Samsung"
SELECT * FROM mobil WHERE model LIKE "%Samsung%";

# 4.3. Товары, в которых есть ЦИФРА "8"
SELECT * FROM mobil WHERE model LIKE "%8%";
