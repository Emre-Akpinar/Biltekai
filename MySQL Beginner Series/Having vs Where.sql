

SELECT gender,AVG(age)
FROM employee_demographics
WHERE AVG(age) >40        -- We got an error because group of genders have not created yet so AVG(age) of the genders are not assigned to any value
GROUP BY gender
;

SELECT gender,AVG(age)
FROM employee_demographics
GROUP BY gender
HAVING AVG(age)>40     -- Having help us here. Shows only groups having 40 or more avarage age.
;

SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE "%manager%"
GROUP BY occupation
HAVING occupation LIKE "%f%"
;

SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE "%manager%"
GROUP BY occupation
HAVING AVG(salary) > 60000
;





