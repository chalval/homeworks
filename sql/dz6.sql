DROP DATABASE IF EXISTS dz6;
CREATE DATABASE IF NOT EXISTS dz6;
USE dz6;

-- Task1. Создайте процедуру, которая принимает кол-во сек и формат их в кол-во дней часов. 
-- Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '
DELIMITER //
CREATE PROCEDURE proc1(t INT)
	BEGIN
		DECLARE days1 INT DEFAULT 0;
		DECLARE hours1 INT DEFAULT 0;
		DECLARE minutes1 INT DEFAULT 0;
		DECLARE seconds1 INT DEFAULT 0;
		DECLARE result VARCHAR(70) DEFAULT CONCAT(t,' seconds = ');
		SET days1 = t DIV 86400;
		SET t = t - days1 * 86400;
		SET hours1 = t DIV 3600;
		SET t = t - hours1 * 3600;
		SET minutes1 = t DIV 60;
		SET seconds1 = t - minutes1 * 60;
		SET result = CONCAT(result, days1,' days ', hours1, ' hours ', minutes1, ' minutes ', seconds1, ' seconds.');
		SELECT result;
	END //
DELIMITER ;

CALL proc1(123456);

-- Task2. Создайте функцию, которая выводит только четные числа от 1 до 10. Пример: 2,4,6,8,10
DELIMITER //
CREATE FUNCTION even2(a INT, b INT)
RETURNS VARCHAR(45)
DETERMINISTIC
BEGIN
    DECLARE i INT DEFAULT a;
    DECLARE result VARCHAR(45) DEFAULT '';
    WHILE i <= b DO
		IF i % 2 = 0 THEN
			SET result = CONCAT(result,' ', i);
		END IF;
		SET i = i + 1;
     END WHILE;
     RETURN result;
END //
DELIMITER ;
     
SELECT even2(1, 10);