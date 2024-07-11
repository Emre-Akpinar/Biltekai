-- Like & Aliasing


-- limit
SELECT *
FROM employee_demographics
ORDER BY birth_date
LIMIT 3
;



SELECT *
FROM employee_demographics
ORDER BY birth_date
LIMIT 2,1                -- When second parameter added, first parameter is starting position and second parameter is how much row we gonna go after.
;

-- aliasing

SELECT gender,AVG(age)
FROM employee_demographics
GROUP BY gender
HAVING AVG(age) > 40
;


SELECT gender,AVG(age) as avg_age
FROM employee_demographics
GROUP BY gender
HAVING avg_age > 40
;


SELECT gender,AVG(age) avg_age
FROM employee_demographics
GROUP BY gender
HAVING avg_age > 40
;









