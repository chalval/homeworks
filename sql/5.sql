
DROP DATABASE IF EXISTS l4;
CREATE DATABASE IF NOT EXISTS l4;
USE l4;

-- Создание таблицы
CREATE TABLE IF NOT EXISTS staff
(
id INT PRIMARY KEY,
first_name VARCHAR(30),
post VARCHAR(30),
discipline VARCHAR(30),
salary INT
);
-- Заполнение таблицы данными
INSERT staff (id, first_name, post, discipline, salary)
VALUES
(100,'Антон', 'Преподаватель', 'Программирование', 50),
(101,'Василий', 'Преподаватель', 'Программирование', 60),
(103,'Александр', 'Ассистент', 'Программирование', 25),
(104,'Владимир', 'Профессор', 'Математика', 120),
(105,'Иван', 'Профессор', 'Математика', 120),
(106,'Михаил', 'Доцент', 'Физика', 70),
(107, 'Анна', 'Доцент', 'Физика', 70),
(108, 'Вероника', 'Доцент', 'ИКТ', 30),
(109,'Григорий', 'Преподаватель', 'ИКТ', 25),
(110,'Георгий', 'Ассистент', 'Программирование', 30);

SELECT
DENSE_RANK() OVER W AS `rank`, -- W = OVER(ORDER BY salary DESC)
first_name, discipline,
salary
FROM staff
WINDOW w AS (ORDER BY salary DESC)
ORDER BY `rank`, id;

SELECT
DENSE_RANK() OVER W AS `rank`,
first_name, discipline,
salary
FROM staff
WINDOW w AS (ORDER BY salary ASC)
ORDER BY salary DESC;






