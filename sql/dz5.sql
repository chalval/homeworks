DROP DATABASE IF EXISTS dz5;
CREATE DATABASE IF NOT EXISTS dz5;
USE dz5;
CREATE TABLE cars (
	id INT NOT NULL PRIMARY KEY,
    name VARCHAR(45),
    cost INT);
INSERT cars
VALUES
	(1, "Audi", 52642),
    (2, "Mercedes", 57127 ),
    (3, "Skoda", 9000 ),
    (4, "Volvo", 29000),
	(5, "Bentley", 350000),
    (6, "Citroen ", 21000 ), 
    (7, "Hummer", 41400), 
    (8, "Volkswagen ", 21600);
SELECT * FROM cars;

-- Task1. Создайте представление, в которое попадут автомобили стоимостью до 25 000 долларов
CREATE OR REPLACE VIEW avto AS
SELECT name
FROM cars
WHERE cars.cost < 25000;

SELECT * FROM avto;

-- Task2. Изменить в существующем представлении порог для стоимости: 
-- пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW)

ALTER VIEW avto AS
SELECT name
FROM cars
WHERE cars.cost < 30000;

SELECT * FROM avto;

-- Task3. Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди”
CREATE OR REPLACE VIEW avto2 AS
SELECT name
FROM cars
WHERE cars.name IN ('Skoda', 'Audi');

SELECT * FROM avto2;