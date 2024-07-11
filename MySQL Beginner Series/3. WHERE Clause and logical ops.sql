-- WHERE Clause

SELECT *
FROM parks_and_recreation.employee_salary
WHERE first_name = "Leslie";


SELECT *
FROM parks_and_recreation.employee_salary
WHERE salary >= 50000;


SELECT *
FROM parks_and_recreation.employee_salary
WHERE salary < 50000;


SELECT *
FROM parks_and_recreation.employee_demographics
WHERE gender = "Female";

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE gender != "Female";


SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > "1985-01-01";


-- AND OR NOT -- Logical operaters

SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > "1985-01-01"
OR gender = "Female";


SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > "1985-01-01"
AND gender = "Female";


SELECT *
FROM parks_and_recreation.employee_demographics
WHERE birth_date > "1985-01-01"
AND NOT gender = "Male";


SELECT *
FROM parks_and_recreation.employee_demographics
WHERE (first_name = "Leslie" AND age = 44) OR age>55
;


-- LIKE Statement
-- % and _

SELECT *
FROM employee_demographics
WHERE first_name = "Jerry"
;
 
SELECT *
FROM employee_demographics
WHERE first_name LIKE "Jer" -- Directly Jer, looking for Name = Jer
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE "Jer%" -- Names starting with 'Jer'
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE "%r%"  -- Names that has r in it
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE "a%" -- Names starting with a
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE "a__" -- a and two just 2 characters after
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE "a___%"
;

SELECT *
FROM employee_demographics
WHERE birth_date LIKE "1988%"
;

SELECT *
FROM employee_demographics
WHERE gender LIKE "%male"
;

SELECT *
FROM employee_demographics
WHERE age LIKE "3%"
;

SELECT *
FROM employee_demographics
WHERE birth_date LIKE "_____03___"  -- Employees whose birthday is on march
;










