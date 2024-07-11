SELECT *
FROM  employee_demographics;




SELECT DISTINCT gender
FROM  employee_demographics
;
								-- Output looks the same but with group by all the values are rolled up. So we can use mean etc. easily

SELECT gender
FROM  employee_demographics
GROUP BY gender 
;

SELECT gender,AVG(age)
FROM  employee_demographics
GROUP BY gender
;

SELECT occupation
FROM  employee_salary
Group By occupation
;



SELECT occupation,AVG(salary)
FROM  employee_salary
Group By occupation
;


SELECT occupation,salary
FROM  employee_salary        -- if both occupation and salary is same they'd be one row
Group By occupation, salary
;


SELECT gender,AVG(age),MAX(age),MIN(age),COUNT(age)
FROM  employee_demographics
Group By gender
;


-- ORDER BY

SELECT *
FROM  employee_demographics
ORDER BY first_name DESC      -- ASC default
;

SELECT *
FROM  employee_demographics   -- first ordered by gender after by age
ORDER BY gender DESC, age DESC
;


SELECT *
FROM  employee_demographics  
ORDER BY 5,4					-- These numbers represent column numbers fifth is gender and fourth is age(this could be tricky when columns added or removed)
;
















