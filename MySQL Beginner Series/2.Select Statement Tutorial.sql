SELECT *
FROM parks_and_recreation.employee_demographics;

SELECT first_name 
FROM parks_and_recreation.employee_demographics;

SELECT first_name,last_name,birth_date
FROM parks_and_recreation.employee_demographics;

SELECT first_name,
last_name,
birth_date,
age,
(age+10)*10 as age_2
FROM parks_and_recreation.employee_demographics;

#Distinct
SELECT DISTINCT first_name
FROM parks_and_recreation.employee_demographics;

SELECT gender
FROM parks_and_recreation.employee_demographics;

SELECT DISTINCT gender
FROM parks_and_recreation.employee_demographics;

SELECT DISTINCT first_name,gender
FROM parks_and_recreation.employee_demographics;






