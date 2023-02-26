
-- create
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO classmates VALUES (1, 'Василий', 25, 'Сочи ул. Ленина, 25');
INSERT INTO classmates VALUES (2, 'Анна', 52, 'Орел ул. Шевченко, 5');
INSERT INTO classmates VALUES (3, 'Сергей', 18, 'Москва ул. Пушкина, 44');
INSERT INTO classmates VALUES (4, 'Валерий', 49, 'Шахты ул. Майская, 16');
INSERT INTO classmates VALUES (5, 'Сергей', 33, 'Москва ул. Гагарина, 12');
INSERT INTO classmates VALUES (6, 'Вадим', 33, 'Воронеж ул. Антонова, 21');

-- fetch 
SELECT name FROM classmates WHERE id < 6 AND age < 50 AND name LIKE '%ва%';
