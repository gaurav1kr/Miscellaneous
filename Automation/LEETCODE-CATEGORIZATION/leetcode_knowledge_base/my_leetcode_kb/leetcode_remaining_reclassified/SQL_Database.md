# SQL Database

## 175. Combine Two Tables

**Problem:** https://leetcode.com/problems/combine-two-tables/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187214441  
**Language:** mysql

### Description

Table:  Person 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
```
 
 
   
 
 Table:  Address 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.
```
 
 
   
 
 Write a solution to report the first name, last name, city, and state of each person in the  Person  table. If the address of a  personId  is not present in the  Address  table, report  null  instead. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+

Output:
 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+

Explanation:
 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p LEFT JOIN Address a ON p.personId = a.personId;
```

---

## 176. Second Highest Salary

**Problem:** https://leetcode.com/problems/second-highest-salary/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187215433  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```
 
 
   
 
 Write a solution to find the second highest  distinct  salary from the  Employee  table. If there is no second highest salary, return  null (return None in Pandas) . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

Output:
 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```
 
 
 Example 2: 
 
```text
Input:
 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

Output:
 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary;
```

---

## 177. Nth Highest Salary

**Problem:** https://leetcode.com/problems/nth-highest-salary/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187215551  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```
 
 
   
 
 Write a solution to find the  n th  highest  distinct  salary from the  Employee  table. If there are less than  n  distinct salaries, return  null . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2

Output:
 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```
 
 
 Example 2: 
 
```text
Input:
 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2

Output:
 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N);
END;
```

---

## 178. Rank Scores

**Problem:** https://leetcode.com/problems/rank-scores/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222102  
**Language:** mysql

### Description

Table:  Scores 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
```
 
 
   
 
 Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules: 
 
 
 The scores should be ranked from the highest to the lowest. 
 
 If there is a tie between two scores, both should have the same ranking. 
 
 After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks. 
 
 
 Return the result table ordered by  score  in descending order. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

Output:
 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores ORDER BY score DESC;
```

---

## 180. Consecutive Numbers

**Problem:** https://leetcode.com/problems/consecutive-numbers/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187216839  
**Language:** mysql

### Description

Table:  Logs 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
```
 
 
   
 
 Find all numbers that appear at least three times consecutively. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Output:
 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

Explanation:
 1 is the only number that appears consecutively for at least three times.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DISTINCT a.num AS ConsecutiveNums FROM Logs a JOIN Logs b ON b.id = a.id + 1 JOIN Logs c ON c.id = a.id + 2 WHERE a.num = b.num AND b.num = c.num;
```

---

## 181. Employees Earning More Than Their Managers

**Problem:** https://leetcode.com/problems/employees-earning-more-than-their-managers/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187216968  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
```
 
 
   
 
 Write a solution to find the employees who earn more than their managers. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+

Output:
 
+----------+
| Employee |
+----------+
| Joe      |
+----------+

Explanation:
 Joe is the only employee who earns more than his manager.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT e.name AS Employee FROM Employee e JOIN Employee m ON e.managerId = m.id WHERE e.salary > m.salary;
```

---

## 182. Duplicate Emails

**Problem:** https://leetcode.com/problems/duplicate-emails/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187217066  
**Language:** mysql

### Description

Table:  Person 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
```
 
 
   
 
 Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

Output:
 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Explanation:
 a@b.com is repeated two times.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT email AS Email FROM Person GROUP BY email HAVING COUNT(*) > 1;
```

---

## 183. Customers Who Never Order

**Problem:** https://leetcode.com/problems/customers-who-never-order/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187217174  
**Language:** mysql

### Description

Table:  Customers 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
```
 
 
   
 
 Table:  Orders 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
```
 
 
   
 
 Write a solution to find all customers who never order anything. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output:
 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT c.name AS Customers FROM Customers c LEFT JOIN Orders o ON c.id = o.customerId WHERE o.id IS NULL;
```

---

## 184. Department Highest Salary

**Problem:** https://leetcode.com/problems/department-highest-salary/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187217302  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the 
Department 
table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
```
 
 
   
 
 Table:  Department 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not 
NULL.

Each row of this table indicates the ID of a department and its name.
```
 
 
   
 
 Write a solution to find employees who have the highest salary in each of the departments. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Output:
 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+

Explanation:
 Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary FROM Employee e JOIN Department d ON d.id=e.departmentId WHERE e.salary = (SELECT MAX(e2.salary) FROM Employee e2 WHERE e2.departmentId=e.departmentId);
```

---

## 185. Department Top Three Salaries

**Problem:** https://leetcode.com/problems/department-top-three-salaries/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187217430  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the 
Department 
table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
```
 
 
   
 
 Table:  Department 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
```
 
 
   
 
 A company's executives are interested in seeing who earns the most money in each of the company's departments. A  high earner  in a department is an employee who has a salary in the  top three unique  salaries for that department. 
 
 Write a solution to find the employees who are  high earners  in each of the departments. 
 
 Return the result table  in any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Output:
 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

Explanation:
 
In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees
```
 
 
   
 
 Constraints: 
 
 
 There are no employees with the  exact  same name, salary  and  department.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT e.*, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk FROM Employee e) SELECT d.name AS Department, r.name AS Employee, r.salary AS Salary FROM ranked r JOIN Department d ON d.id=r.departmentId WHERE r.rnk <= 3;
```

---

## 196. Delete Duplicate Emails

**Problem:** https://leetcode.com/problems/delete-duplicate-emails/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222204  
**Language:** mysql

### Description

Table:  Person 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
```
 
 
   
 
 Write a solution to  delete  all duplicate emails, keeping only one unique email with the smallest  id . 
 
 For SQL users, please note that you are supposed to write a  DELETE  statement and not a  SELECT  one. 
 
 For Pandas users, please note that you are supposed to modify  Person  in place. 
 
 After running your script, the answer shown is the  Person  table. The driver will first compile and run your piece of code and then show the  Person  table. The final order of the  Person  table  does not matter . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Output:
 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Explanation:
 john@example.com is repeated two times. We keep the row with the smallest Id = 1.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
DELETE p1 FROM Person p1 JOIN Person p2 ON p1.email=p2.email AND p1.id>p2.id;
```

---

## 197. Rising Temperature

**Problem:** https://leetcode.com/problems/rising-temperature/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187218738  
**Language:** mysql

### Description

Table:  Weather 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
```
 
 
   
 
 Write a solution to find all dates'  id  with higher temperatures compared to its previous calendar dates (yesterday). 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Output:
 
+----+
| id |
+----+
| 2  |
| 4  |
+----+

Explanation:
 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT w1.id FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w1.recordDate,w2.recordDate)=1 WHERE w1.temperature>w2.temperature;
```

---

## 262. Trips and Users

**Problem:** https://leetcode.com/problems/trips-and-users/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187218867  
**Language:** mysql

### Description

Table:  Trips 
 
```text
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | varchar  |     
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
```
 
 
   
 
 Table:  Users 
 
```text
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').
```
 
 
   
 
 The  cancellation rate  is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day. 
 
 Write a solution to find the  cancellation rate  of requests with unbanned users ( both client and driver must not be banned ) each day between  "2013-10-01"  and  "2013-10-03"  with  at least  one trip. Round  Cancellation Rate  to  two decimal  points. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+

Output:
 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+

Explanation:
 
On 2013-10-01:
  - There were 4 requests in total, 2 of which were canceled.
  - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
  - Hence there are 3 unbanned requests in total, 1 of which was canceled.
  - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
  - There were 3 requests in total, 0 of which were canceled.
  - The request with Id=6 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned requests in total, 0 of which were canceled.
  - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
  - There were 3 requests in total, 1 of which was canceled.
  - The request with Id=8 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned request in total, 1 of which were canceled.
  - The Cancellation Rate is (1 / 2) = 0.50
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT t.request_at AS Day, ROUND(AVG(t.status <> 'completed'),2) AS `Cancellation Rate` FROM Trips t JOIN Users c ON c.users_id=t.client_id AND c.banned='No' JOIN Users d ON d.users_id=t.driver_id AND d.banned='No' WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03' GROUP BY t.request_at;
```

---

## 511. Game Play Analysis I

**Problem:** https://leetcode.com/problems/game-play-analysis-i/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187218992  
**Language:** mysql

### Description

Table:  Activity 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
```
 
 
   
 
 Write a solution to find the  first login date  for each player. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Output:
 
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id;
```

---

## 512. Game Play Analysis II

**Problem:** https://leetcode.com/problems/game-play-analysis-ii/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187219107  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT a.player_id, a.device_id FROM Activity a JOIN (SELECT player_id, MIN(event_date) AS first_date FROM Activity GROUP BY player_id) f ON a.player_id=f.player_id AND a.event_date=f.first_date;
```

---

## 534. Game Play Analysis III

**Problem:** https://leetcode.com/problems/game-play-analysis-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187219219  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT player_id, event_date, SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS games_played_so_far FROM Activity;
```

---

## 550. Game Play Analysis IV

**Problem:** https://leetcode.com/problems/game-play-analysis-iv/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187219350  
**Language:** mysql

### Description

Table:  Activity 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
```
 
 
   
 
 Write a solution to report the  fraction  of players that logged in again on the day after the day they first logged in,  rounded to 2 decimal places . In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Output:
 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+

Explanation:
 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction FROM Activity a JOIN (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) f ON a.player_id=f.player_id AND a.event_date=DATE_ADD(f.first_login, INTERVAL 1 DAY);
```

---

## 569. Median Employee Salary

**Problem:** https://leetcode.com/problems/median-employee-salary/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187219449  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH r AS (SELECT id, company, salary, ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS rn, COUNT(*) OVER (PARTITION BY company) AS cnt FROM Employee) SELECT id, company, salary FROM r WHERE rn IN (FLOOR((cnt+1)/2), FLOOR((cnt+2)/2));
```

---

## 570. Managers with at Least 5 Direct Reports

**Problem:** https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187219576  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
```
 
 
   
 
 Write a solution to find managers with at least  five direct reports . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+

Output:
 
+------+
| name |
+------+
| John |
+------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT m.name FROM Employee m JOIN Employee e ON e.managerId=m.id GROUP BY m.id, m.name HAVING COUNT(*) >= 5;
```

---

## 571. Find Median Given Frequency of Numbers

**Problem:** https://leetcode.com/problems/find-median-given-frequency-of-numbers/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250242  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH freq AS (
 SELECT num, frequency,
        SUM(frequency) OVER (ORDER BY num) AS left_count,
        SUM(frequency) OVER (ORDER BY num DESC) AS right_count,
        SUM(frequency) OVER () AS total_count
 FROM Numbers
)
SELECT ROUND(AVG(num), 1) AS median
FROM freq
WHERE left_count >= total_count / 2
  AND right_count >= total_count / 2;
```

---

## 574. Winning Candidate

**Problem:** https://leetcode.com/problems/winning-candidate/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195458318  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT c.name FROM Candidate c JOIN Vote v ON c.id = v.candidateId GROUP BY c.id, c.name ORDER BY COUNT(*) DESC LIMIT 1;
```

---

## 577. Employee Bonus

**Problem:** https://leetcode.com/problems/employee-bonus/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187219798  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
```
 
 
   
 
 Table:  Bonus 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.
```
 
 
   
 
 Write a solution to report the name and bonus amount of each employee who satisfies either of the following: 
 
 
 The employee has a bonus  less than   1000 . 
 
 The employee did not get any bonus. 
 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+

Output:
 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

---

## 578. Get Highest Answer Rate Question

**Problem:** https://leetcode.com/problems/get-highest-answer-rate-question/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195458504  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT question_id AS survey_log FROM SurveyLog GROUP BY question_id ORDER BY SUM(action = 'answer') / NULLIF(SUM(action = 'show'), 0) DESC, question_id LIMIT 1;
```

---

## 579. Find Cumulative Salary of an Employee

**Problem:** https://leetcode.com/problems/find-cumulative-salary-of-an-employee/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195458676  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT e1.id, e1.month, SUM(e2.salary) AS Salary FROM Employee e1 JOIN Employee e2 ON e1.id = e2.id AND e2.month BETWEEN e1.month - 2 AND e1.month WHERE e1.month < (SELECT MAX(e3.month) FROM Employee e3 WHERE e3.id = e1.id) GROUP BY e1.id, e1.month ORDER BY e1.id, e1.month DESC;
```

---

## 580. Count Student Number in Departments

**Problem:** https://leetcode.com/problems/count-student-number-in-departments/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195458845  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT d.dept_name, COUNT(s.student_id) AS student_number FROM Department d LEFT JOIN Student s ON s.dept_id = d.dept_id GROUP BY d.dept_id, d.dept_name ORDER BY student_number DESC, d.dept_name;
```

---

## 584. Find Customer Referee

**Problem:** https://leetcode.com/problems/find-customer-referee/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222308  
**Language:** mysql

### Description

Table:  Customer 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
```
 
 
   
 
 Find the names of the customer that are either: 
 
 
 referred by  any customer with  id != 2 . 
 
 not referred by  any customer. 
 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+

Output:
 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

---

## 585. Investments in 2016

**Problem:** https://leetcode.com/problems/investments-in-2016/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222422  
**Language:** mysql

### Description

Table:  Insurance 
 
```text
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one policy where:
pid is the policyholder's policy ID.
tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.
```
 
 
   
 
 Write a solution to report the sum of all total investment values in 2016  tiv_2016 , for all policyholders who: 
 
 
 have the same  tiv_2015  value as one or more other policyholders, and 
 
 are not located in the same city as any other policyholder (i.e., the ( lat, lon ) attribute pairs must be unique). 
 
 
 Round  tiv_2016  to  two decimal places . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Insurance table:
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+

Output:
 
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+

Explanation:
 
The first record in the table, like the last record, meets both of the two criteria.
The tiv_2015 value 10 is the same as the third and fourth records, and its location is unique.

The second record does not meet any of the two criteria. Its tiv_2015 is not like any other policyholders and its location is the same as the third record, which makes the third record fail, too.
So, the result is the sum of tiv_2016 of the first and last record, which is 45.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance
    GROUP BY tiv_2015 HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon FROM Insurance
    GROUP BY lat, lon HAVING COUNT(*) = 1
);
```

---

## 586. Customer Placing the Largest Number of Orders

**Problem:** https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222544  
**Language:** mysql

### Description

Table:  Orders 
 
```text
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
```
 
 
   
 
 Write a solution to find the  customer_number  for the customer who has placed  the largest number of orders . 
 
 The test cases are generated so that  exactly one customer  will have placed more orders than any other customer. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+

Output:
 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+

Explanation:
 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.
```
 
 
   
 
 Follow up:  What if more than one customer has the largest number of orders, can you find all the  customer_number  in this case?

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```

---

## 595. Big Countries

**Problem:** https://leetcode.com/problems/big-countries/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222668  
**Language:** mysql

### Description

Table:  World 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
```
 
 
   
 
 A country is  big  if: 
 
 
 it has an area of at least three million (i.e.,  3000000 km 2 ), or 
 
 it has a population of at least twenty-five million (i.e.,  25000000 ). 
 
 
 Write a solution to find the name, population, and area of the  big countries . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+

Output:
 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
```

---

## 596. Classes With at Least 5 Students

**Problem:** https://leetcode.com/problems/classes-with-at-least-5-students/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222784  
**Language:** mysql

### Description

Table:  Courses 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
```
 
 
   
 
 Write a solution to find all the classes that have  at least five students . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+

Output:
 
+---------+
| class   |
+---------+
| Math    |
+---------+

Explanation:
 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

---

## 597. Friend Requests I: Overall Acceptance Rate

**Problem:** https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195459009  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(IFNULL((SELECT COUNT(DISTINCT requester_id, accepter_id) FROM RequestAccepted) / NULLIF((SELECT COUNT(DISTINCT sender_id, send_to_id) FROM FriendRequest), 0), 0), 2) AS accept_rate;
```

---

## 601. Human Traffic of Stadium

**Problem:** https://leetcode.com/problems/human-traffic-of-stadium/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187222897  
**Language:** mysql

### Description

Table:  Stadium 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the column with unique values for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
As the id increases, the date increases as well.
```
 
 
   
 
 Write a solution to display the records with three or more rows with  consecutive   id 's, and the number of people is greater than or equal to 100 for each. 
 
 Return the result table ordered by  visit_date  in  ascending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Stadium table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+

Output:
 
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+

Explanation:
 
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH qualified AS (
    SELECT id, visit_date, people,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
), runs AS (
    SELECT id, visit_date, people,
           COUNT(*) OVER (PARTITION BY grp) AS run_length
    FROM qualified
)
SELECT id, visit_date, people
FROM runs
WHERE run_length >= 3
ORDER BY visit_date;
```

---

## 602. Friend Requests II: Who Has the Most Friends

**Problem:** https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223036  
**Language:** mysql

### Description

Table:  RequestAccepted 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
```
 
 
   
 
 Write a solution to find the people who have the most friends and the most friends number. 
 
 The test cases are generated so that only one person has the most friends. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+

Output:
 
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+

Explanation:
 
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.
```
 
 
   
 
 Follow up:  In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH all_friends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
)
SELECT id, COUNT(*) AS num
FROM all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```

---

## 603. Consecutive Available Seats

**Problem:** https://leetcode.com/problems/consecutive-available-seats/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195459185  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DISTINCT a.seat_id FROM Cinema a JOIN Cinema b ON ABS(a.seat_id - b.seat_id) = 1 WHERE a.free = 1 AND b.free = 1 ORDER BY a.seat_id;
```

---

## 607. Sales Person

**Problem:** https://leetcode.com/problems/sales-person/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223161  
**Language:** mysql

### Description

Table:  SalesPerson 
 
```text
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
```
 
 
   
 
 Table:  Company 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.
```
 
 
   
 
 Table:  Orders 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key (column with unique values) for this table.
com_id is a foreign key (reference column) to com_id from the Company table.
sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
```
 
 
   
 
 Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name  "RED" . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
SalesPerson table:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+
Company table:
+--------+--------+----------+
| com_id | name   | city     |
+--------+--------+----------+
| 1      | RED    | Boston   |
| 2      | ORANGE | New York |
| 3      | YELLOW | Boston   |
| 4      | GREEN  | Austin   |
+--------+--------+----------+
Orders table:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+

Output:
 
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+

Explanation:
 
According to orders 3 and 4 in the Orders table, it is easy to tell that only salesperson John and Pam have sales to company RED, so we report all the other names in the table salesperson.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c ON c.com_id = o.com_id
    WHERE o.sales_id = s.sales_id AND c.name = 'RED'
);
```

---

## 608. Tree Node

**Problem:** https://leetcode.com/problems/tree-node/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223288  
**Language:** mysql

### Description

Table:  Tree 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the column with unique values for this table.
Each row of this table contains information about the id of a node and the id of its parent node in a tree.
The given structure is always a valid tree.
```
 
 
   
 
 Each node in the tree can be one of three types: 
 
 
 "Leaf" : if the node is a leaf node. 
 
 "Root" : if the node is the root of the tree. 
 
 "Inner" : If the node is neither a leaf node nor a root node. 
 
 
 Write a solution to report the type of each node in the tree. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
 
```text
Input:
 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

Output:
 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+

Explanation:
 
Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
Node 2 is an inner node because it has parent node 1 and child node 4 and 5.
Nodes 3, 4, and 5 are leaf nodes because they have parent nodes and they do not have child nodes.
```
 
 
 Example 2: 
 
 
```text
Input:
 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
+----+------+

Output:
 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
+----+-------+

Explanation:
 If there is only one node on the tree, you only need to output its root attributes.
```
 
 
   
 
 Note:  This question is the same as   3054: Binary Tree Nodes.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT t.id,
       CASE
           WHEN t.p_id IS NULL THEN 'Root'
           WHEN EXISTS (SELECT 1 FROM Tree c WHERE c.p_id = t.id) THEN 'Inner'
           ELSE 'Leaf'
       END AS type
FROM Tree t;
```

---

## 610. Triangle Judgement

**Problem:** https://leetcode.com/problems/triangle-judgement/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223387  
**Language:** mysql

### Description

Table:  Triangle 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
```
 
 
   
 
 Report for every three line segments whether they can form a triangle. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+

Output:
 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT x, y, z,
       CASE WHEN x + y > z AND x + z > y AND y + z > x
            THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle;
```

---

## 612. Shortest Distance in a Plane

**Problem:** https://leetcode.com/problems/shortest-distance-in-a-plane/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database, Nearest Pair of Points  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195459347  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(MIN(SQRT(POW(a.x - b.x, 2) + POW(a.y - b.y, 2))), 2) AS shortest FROM Point2D a JOIN Point2D b ON a.x < b.x OR (a.x = b.x AND a.y < b.y);
```

---

## 613. Shortest Distance in a Line

**Problem:** https://leetcode.com/problems/shortest-distance-in-a-line/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database, Nearest Pair of Points  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195459522  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT MIN(next_x - x) AS shortest FROM (SELECT x, LEAD(x) OVER (ORDER BY x) AS next_x FROM Point) t;
```

---

## 614. Second Degree Follower

**Problem:** https://leetcode.com/problems/second-degree-follower/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195459700  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT f.followee AS follower, COUNT(*) AS num FROM Follow f WHERE f.followee IN (SELECT follower FROM Follow) GROUP BY f.followee ORDER BY follower;
```

---

## 615. Average Salary: Departments VS Company

**Problem:** https://leetcode.com/problems/average-salary-departments-vs-company/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195459869  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH monthly AS (SELECT DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month, e.department_id, s.amount FROM Salary s JOIN Employee e ON e.employee_id = s.employee_id), dept AS (SELECT pay_month, department_id, AVG(amount) AS avg_salary FROM monthly GROUP BY pay_month, department_id), company AS (SELECT pay_month, AVG(amount) AS avg_salary FROM monthly GROUP BY pay_month) SELECT d.pay_month, d.department_id, CASE WHEN d.avg_salary > c.avg_salary THEN 'higher' WHEN d.avg_salary < c.avg_salary THEN 'lower' ELSE 'same' END AS comparison FROM dept d JOIN company c ON d.pay_month = c.pay_month;
```

---

## 618. Students Report By Geography

**Problem:** https://leetcode.com/problems/students-report-by-geography/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195460044  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH numbered AS (SELECT name, continent, ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS rn FROM Student) SELECT MAX(CASE WHEN continent = 'America' THEN name END) AS America, MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia, MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe FROM numbered GROUP BY rn ORDER BY rn;
```

---

## 619. Biggest Single Number

**Problem:** https://leetcode.com/problems/biggest-single-number/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223536  
**Language:** mysql

### Description

Table:  MyNumbers 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
```
 
 
   
 
 A  single number  is a number that appeared only once in the  MyNumbers  table. 
 
 Find the largest  single number . If there is no  single number , report  null . 
 
 The result format is in the following example. 
   
 
   
 
 Example 1: 
 
```text
Input:
 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+

Output:
 
+-----+
| num |
+-----+
| 6   |
+-----+

Explanation:
 The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.
```
 
 
 Example 2: 
 
```text
Input:
 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+

Output:
 
+------+
| num  |
+------+
| null |
+------+

Explanation:
 There are no single numbers in the input table so we return null.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS singles;
```

---

## 620. Not Boring Movies

**Problem:** https://leetcode.com/problems/not-boring-movies/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223656  
**Language:** mysql

### Description

Table:  Cinema 
 
```text
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
```
 
 
   
 
 Write a solution to report the movies with an odd-numbered ID and a description that is not  "boring" . 
 
 Return the result table ordered by  rating   in descending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+

Output:
 
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+

Explanation:
 
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT id, movie, description, rating
FROM Cinema
WHERE MOD(id, 2) = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

---

## 626. Exchange Seats

**Problem:** https://leetcode.com/problems/exchange-seats/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223780  
**Language:** mysql

### Description

Table:  Seat 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
```
 
 
   
 
 Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped. 
 
 Return the result table ordered by  id   in ascending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+

Output:
 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+

Explanation:
 
Note that if the number of students is odd, there is no need to change the last one's seat.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT CASE
           WHEN MOD(id, 2) = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
           WHEN MOD(id, 2) = 1 THEN id + 1
           ELSE id - 1
       END AS id,
       student
FROM Seat
ORDER BY id;
```

---

## 627. Swap Sex of Employees

**Problem:** https://leetcode.com/problems/swap-sex-of-employees/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187223893  
**Language:** mysql

### Description

Table:  Salary 
 
```text
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key (column with unique values) for this table.
The sex column is ENUM (category) value of type ('m', 'f').
The table contains information about an employee.
```
 
 
   
 
 Write a solution to swap all  'f'  and  'm'  values (i.e., change all  'f'  values to  'm'  and vice versa) with a  single update statement  and no intermediate temporary tables. 
 
 Note that you must write a single update statement,  do not  write any select statement for this problem. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+

Output:
 
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+

Explanation:
 
(1, A) and (3, C) were changed from 'm' to 'f'.
(2, B) and (4, D) were changed from 'f' to 'm'.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END;
```

---

## 1045. Customers Who Bought All Products

**Problem:** https://leetcode.com/problems/customers-who-bought-all-products/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224007  
**Language:** mysql

### Description

Table:  Customer 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows. 

customer_id
 is not NULL
.

product_key is a foreign key (reference column) to 
Product
 table.
```
 
 
   
 
 Table:  Product 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.
```
 
 
   
 
 Write a solution to report the customer ids from the  Customer  table that bought all the products in the  Product  table. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+

Output:
 
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+

Explanation:
 
The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) FROM Product
);
```

---

## 1050. Actors and Directors Who Cooperated At Least Three Times

**Problem:** https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224133  
**Language:** mysql

### Description

Table:  ActorDirector 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
```
 
 
   
 
 Write a solution to find all the pairs  (actor_id, director_id)  where the actor has cooperated with the director at least three times. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
ActorDirector table:
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+

Output:
 
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+

Explanation:
 The only pair is (1, 1) where they cooperated exactly 3 times.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
```

---

## 1068. Product Sales Analysis I

**Problem:** https://leetcode.com/problems/product-sales-analysis-i/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187246417  
**Language:** mysql

### Description

Table:  Sales 
 
```text
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to 
Product
 table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
```
 
 
   
 
 Table:  Product 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
```
 
 
   
 
 Write a solution to report the  product_name ,  year , and  price  for each  sale_id  in the  Sales  table. 
 
 Return the resulting table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Output:
 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+

Explanation:
 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.product_name, s.year, s.price
FROM Sales AS s
JOIN Product AS p ON p.product_id = s.product_id;
```

---

## 1069. Product Sales Analysis II

**Problem:** https://leetcode.com/problems/product-sales-analysis-ii/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195460249  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT product_id, SUM(quantity) AS total_quantity FROM Sales GROUP BY product_id;
```

---

## 1070. Product Sales Analysis III

**Problem:** https://leetcode.com/problems/product-sales-analysis-iii/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250314  
**Language:** mysql

### Description

Table:  Sales 
 
```text
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
Each row records a sale of a product in a given year.
A product may have multiple sales entries in the same year.
Note that the per-unit price.
```
 
 
 Write a solution to find all sales that occurred in the  first year  each product was sold. 
 
 
 
 
 For each  product_id , identify the earliest  year  it appears in the  Sales  table. 
 
 
 
 
 Return  all  sales entries for that product in that year. 
 
 
 
 Return a table with the following columns:  product_id ,  first_year ,  quantity,  and  price . 
Return the result in any order. 
 
   
 
 Example 1: 
 
```text
Input:
 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Output:
 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH first_year AS (
 SELECT product_id, MIN(year) AS first_year
 FROM Sales GROUP BY product_id
)
SELECT s.product_id, f.first_year, s.quantity, s.price
FROM Sales s
JOIN first_year f ON f.product_id=s.product_id AND f.first_year=s.year;
```

---

## 1075. Project Employees I

**Problem:** https://leetcode.com/problems/project-employees-i/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224415  
**Language:** mysql

### Description

Table:  Project 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to 
Employee
 table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
```
 
 
   
 
 Table:  Employee 
 
```text
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.
```
 
 
   
 
 Write an SQL query that reports the  average  experience years of all the employees for each project,  rounded to 2 digits . 
 
 Return the result table in  any order . 
 
 The query result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Output:
 
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+

Explanation:
 The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.project_id,
       ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project AS p
JOIN Employee AS e ON e.employee_id = p.employee_id
GROUP BY p.project_id;
```

---

## 1076. Project Employees II

**Problem:** https://leetcode.com/problems/project-employees-ii/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195460449  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH counts AS (SELECT project_id, COUNT(*) AS cnt FROM Project GROUP BY project_id) SELECT project_id FROM counts WHERE cnt = (SELECT MAX(cnt) FROM counts);
```

---

## 1077. Project Employees III

**Problem:** https://leetcode.com/problems/project-employees-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195460637  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT p.project_id, p.employee_id, DENSE_RANK() OVER (PARTITION BY p.project_id ORDER BY e.experience_years DESC) AS rnk FROM Project p JOIN Employee e ON p.employee_id = e.employee_id) SELECT project_id, employee_id FROM ranked WHERE rnk = 1;
```

---

## 1082. Sales Analysis I

**Problem:** https://leetcode.com/problems/sales-analysis-i/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195460795  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH totals AS (SELECT seller_id, SUM(price) AS total FROM Sales GROUP BY seller_id) SELECT seller_id FROM totals WHERE total = (SELECT MAX(total) FROM totals);
```

---

## 1083. Sales Analysis II

**Problem:** https://leetcode.com/problems/sales-analysis-ii/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195460971  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DISTINCT s.buyer_id FROM Sales s JOIN Product p ON p.product_id = s.product_id WHERE p.product_name = 'S8' AND NOT EXISTS (SELECT 1 FROM Sales s2 JOIN Product p2 ON p2.product_id = s2.product_id WHERE s2.buyer_id = s.buyer_id AND p2.product_name = 'iPhone');
```

---

## 1084. Sales Analysis III

**Problem:** https://leetcode.com/problems/sales-analysis-iii/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224534  
**Language:** mysql

### Description

Table:  Product 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
```
 
 
 Table:  Sales 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
```
 
 
   
 
 Write a solution to report the  products  that were  only  sold in the first quarter of  2019 . That is, between  2019-01-01  and  2019-03-31  inclusive. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+

Output:
 
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+

Explanation:
 
The product with id 1 was only sold in the spring of 2019.
The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
The product with id 3 was sold after spring 2019.
We return only product 1 as it is the product that was only sold in the spring of 2019.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.product_id, p.product_name
FROM Product AS p
JOIN Sales AS s ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01'
   AND MAX(s.sale_date) <= '2019-03-31';
```

---

## 1097. Game Play Analysis V

**Problem:** https://leetcode.com/problems/game-play-analysis-v/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195461137  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH installs AS (SELECT player_id, MIN(event_date) AS install_dt FROM Activity GROUP BY player_id) SELECT i.install_dt, COUNT(*) AS installs, ROUND(AVG(CASE WHEN a.player_id IS NOT NULL THEN 1 ELSE 0 END), 2) AS Day1_retention FROM installs i LEFT JOIN Activity a ON a.player_id = i.player_id AND a.event_date = DATE_ADD(i.install_dt, INTERVAL 1 DAY) GROUP BY i.install_dt;
```

---

## 1098. Unpopular Books

**Problem:** https://leetcode.com/problems/unpopular-books/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195461315  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT b.book_id, b.name FROM Books b LEFT JOIN Orders o ON o.book_id = b.book_id AND o.dispatch_date BETWEEN '2018-06-23' AND '2019-06-23' WHERE b.available_from < '2019-05-23' GROUP BY b.book_id, b.name HAVING COALESCE(SUM(o.quantity), 0) < 10;
```

---

## 1107. New Users Daily Count

**Problem:** https://leetcode.com/problems/new-users-daily-count/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195461503  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH first_login AS (SELECT user_id, MIN(activity_date) AS login_date FROM Traffic WHERE activity = 'login' GROUP BY user_id) SELECT login_date, COUNT(*) AS user_count FROM first_login WHERE login_date BETWEEN DATE_SUB('2019-06-30', INTERVAL 90 DAY) AND '2019-06-30' GROUP BY login_date;
```

---

## 1112. Highest Grade For Each Student

**Problem:** https://leetcode.com/problems/highest-grade-for-each-student/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195461679  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT student_id, course_id, grade, ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS rn FROM Enrollments) SELECT student_id, course_id, grade FROM ranked WHERE rn = 1 ORDER BY student_id;
```

---

## 1113. Reported Posts

**Problem:** https://leetcode.com/problems/reported-posts/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195463148  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count FROM Actions WHERE action = 'report' AND action_date = '2019-07-04' GROUP BY extra;
```

---

## 1126. Active Businesses

**Problem:** https://leetcode.com/problems/active-businesses/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195463352  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH compared AS (SELECT business_id, occurrences, AVG(occurrences) OVER (PARTITION BY event_type) AS avg_occurrences FROM Events) SELECT business_id FROM compared WHERE occurrences > avg_occurrences GROUP BY business_id HAVING COUNT(*) > 1;
```

---

## 1127. User Purchase Platform

**Problem:** https://leetcode.com/problems/user-purchase-platform/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195463535  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH per_user AS (SELECT spend_date, user_id, CASE WHEN COUNT(DISTINCT platform) = 2 THEN 'both' ELSE MAX(platform) END AS platform, SUM(amount) AS amount FROM Spending GROUP BY spend_date, user_id), dates AS (SELECT DISTINCT spend_date FROM Spending), platforms AS (SELECT 'mobile' AS platform UNION ALL SELECT 'desktop' UNION ALL SELECT 'both') SELECT d.spend_date, p.platform, COUNT(u.user_id) AS total_users, COALESCE(SUM(u.amount), 0) AS total_amount FROM dates d CROSS JOIN platforms p LEFT JOIN per_user u ON u.spend_date = d.spend_date AND u.platform = p.platform GROUP BY d.spend_date, p.platform;
```

---

## 1132. Reported Posts II

**Problem:** https://leetcode.com/problems/reported-posts-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195463721  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH reported AS (SELECT DISTINCT action_date, post_id FROM Actions WHERE action = 'report' AND extra = 'spam'), daily AS (SELECT r.action_date, COUNT(*) AS total, COUNT(m.post_id) AS removed FROM reported r LEFT JOIN Removals m ON r.post_id = m.post_id GROUP BY r.action_date) SELECT ROUND(AVG(100.0 * removed / total), 2) AS average_daily_percent FROM daily;
```

---

## 1141. User Activity for the Past 30 Days I

**Problem:** https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224694  
**Language:** mysql

### Description

Table:  Activity 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows.
The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.
```
 
 
   
 
 Write a solution to find the daily active user count for a period of  30  days ending  2019-07-27  inclusively. A user was active on someday if they made at least one activity on that day. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
 Note:  Any  activity from ( 'open_session' ,  'end_session' ,  'scroll_down' ,  'send_message' ) will be considered valid activity for a user to be considered active on a day. 
 
   
 
 Example 1: 
 
```text
Input:
 
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+

Output:
 
+------------+--------------+ 
| day        | active_users |
+------------+--------------+ 
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+ 

Explanation:
 Note that we do not care about days with zero active users.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;
```

---

## 1142. User Activity for the Past 30 Days II

**Problem:** https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195463909  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(IFNULL(COUNT(DISTINCT session_id) / NULLIF(COUNT(DISTINCT user_id), 0), 0), 2) AS average_sessions_per_user FROM Activity WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27';
```

---

## 1148. Article Views I

**Problem:** https://leetcode.com/problems/article-views-i/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224814  
**Language:** mysql

### Description

Table:  Views 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
```
 
 
   
 
 Write a solution to find all the authors that viewed at least one of their own articles. 
 
 Return the result table sorted by  id  in ascending order. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

Output:
 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
```

---

## 1149. Article Views II

**Problem:** https://leetcode.com/problems/article-views-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195464101  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DISTINCT viewer_id AS id FROM Views GROUP BY viewer_id, view_date HAVING COUNT(DISTINCT article_id) > 1 ORDER BY id;
```

---

## 1158. Market Analysis I

**Problem:** https://leetcode.com/problems/market-analysis-i/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187224945  
**Language:** mysql

### Description

Table:  Users 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
```
 
 
   
 
 Table:  Orders 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key (column with unique values) of this table.
item_id is a foreign key (reference column) to the Items table.
buyer_id and seller_id are foreign keys to the Users table.
```
 
 
   
 
 Table:  Items 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key (column with unique values) of this table.
```
 
 
   
 
 Write a solution to find for each user, the join date and the number of orders they made as a buyer in  2019 . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+
Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+

Output:
 
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT u.user_id AS buyer_id, u.join_date, COUNT(o.order_id) AS orders_in_2019
FROM Users AS u
LEFT JOIN Orders AS o
  ON o.buyer_id = u.user_id
 AND o.order_date >= '2019-01-01'
 AND o.order_date < '2020-01-01'
GROUP BY u.user_id, u.join_date;
```

---

## 1159. Market Analysis II

**Problem:** https://leetcode.com/problems/market-analysis-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195464269  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT o.seller_id, i.item_brand, ROW_NUMBER() OVER (PARTITION BY o.seller_id ORDER BY o.order_date, o.order_id) AS rn FROM Orders o JOIN Items i ON i.item_id = o.item_id) SELECT u.user_id AS seller_id, CASE WHEN r.item_brand = u.favorite_brand THEN 'yes' ELSE 'no' END AS `2nd_item_fav_brand` FROM Users u LEFT JOIN ranked r ON r.seller_id = u.user_id AND r.rn = 2;
```

---

## 1164. Product Price at a Given Date

**Problem:** https://leetcode.com/problems/product-price-at-a-given-date/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225082  
**Language:** mysql

### Description

Table:  Products 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
```
 
 
 Initially, all products have price 10. 
 
 Write a solution to find the prices of all products on the date  2019-08-16 . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+

Output:
 
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH latest AS (
    SELECT product_id, new_price,
           ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT p.product_id, COALESCE(l.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS p
LEFT JOIN latest AS l ON l.product_id = p.product_id AND l.rn = 1;
```

---

## 1173. Immediate Food Delivery I

**Problem:** https://leetcode.com/problems/immediate-food-delivery-i/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195464471  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(100.0 * AVG(order_date = customer_pref_delivery_date), 2) AS immediate_percentage FROM Delivery;
```

---

## 1174. Immediate Food Delivery II

**Problem:** https://leetcode.com/problems/immediate-food-delivery-ii/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225186  
**Language:** mysql

### Description

Table:  Delivery 
 
```text
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
```
 
 
   
 
 If the customer's preferred delivery date is the same as the order date, then the order is called  immediate;  otherwise, it is called  scheduled . 
 
 The  first order  of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order. 
 
 Write a solution to find the percentage of immediate orders in the first orders of all customers,  rounded to 2 decimal places . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+

Output:
 
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+

Explanation:
 
The customer id 1 has a first order with delivery id 1 and it is scheduled.
The customer id 2 has a first order with delivery id 2 and it is immediate.
The customer id 3 has a first order with delivery id 5 and it is scheduled.
The customer id 4 has a first order with delivery id 7 and it is immediate.
Hence, half the customers have immediate first orders.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH first_orders AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
)
SELECT ROUND(100.0 * AVG(order_date = customer_pref_delivery_date), 2) AS immediate_percentage
FROM first_orders
WHERE rn = 1;
```

---

## 1179. Reformat Department Table

**Problem:** https://leetcode.com/problems/reformat-department-table/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225310  
**Language:** mysql

### Description

Table:  Department 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
```
 
 
   
 
 Reformat the table such that there is a department id column and a revenue column  for each month . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Output:
 
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Explanation:
 The revenue from Apr to Dec is null.
Note that the result table has 13 columns (1 for the department id + 12 for the months).
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT id,
       MAX(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
       MAX(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
       MAX(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,
       MAX(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,
       MAX(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,
       MAX(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,
       MAX(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,
       MAX(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,
       MAX(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,
       MAX(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,
       MAX(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,
       MAX(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue
FROM Department
GROUP BY id;
```

---

## 1193. Monthly Transactions I

**Problem:** https://leetcode.com/problems/monthly-transactions-i/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225431  
**Language:** mysql

### Description

Table:  Transactions 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
```
 
 
   
 
 Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount. 
 
 Return the result table in  any order . 
 
 The query result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+

Output:
 
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country,
       COUNT(*) AS trans_count,
       SUM(state = 'approved') AS approved_count,
       SUM(amount) AS trans_total_amount,
       SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country;
```

---

## 1194. Tournament Winners

**Problem:** https://leetcode.com/problems/tournament-winners/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195464669  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH points AS (SELECT first_player AS player_id, first_score AS score FROM Matches UNION ALL SELECT second_player, second_score FROM Matches), totals AS (SELECT p.group_id, p.player_id, SUM(s.score) AS score FROM Players p JOIN points s ON s.player_id = p.player_id GROUP BY p.group_id, p.player_id), ranked AS (SELECT group_id, player_id, ROW_NUMBER() OVER (PARTITION BY group_id ORDER BY score DESC, player_id) AS rn FROM totals) SELECT group_id, player_id FROM ranked WHERE rn = 1;
```

---

## 1204. Last Person to Fit in the Bus

**Problem:** https://leetcode.com/problems/last-person-to-fit-in-the-bus/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225554  
**Language:** mysql

### Description

Table:  Queue 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id column contains unique values.
This table has the information about all people waiting for a bus.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
weight is the weight of the person in kilograms.
```
 
 
   
 
 There is a queue of people waiting to board a bus. However, the bus has a weight limit of  1000  kilograms , so there may be some people who cannot board. 
 
 Write a solution to find the  person_name  of the  last person  that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit. 
 
 Note  that  only one  person can board the bus at any given turn. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Queue table:
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
+-----------+-------------+--------+------+

Output:
 
+-------------+
| person_name |
+-------------+
| John Cena   |
+-------------+

Explanation:
 The folowing table is ordered by the turn for simplicity.
+------+----+-----------+--------+--------------+
| Turn | ID | Name      | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1    | 5  | Alice     | 250    | 250          |
| 2    | 3  | Alex      | 350    | 600          |
| 3    | 6  | John Cena | 400    | 1000         | (last person to board)
| 4    | 2  | Marie     | 200    | 1200         | (cannot board)
| 5    | 4  | Bob       | 175    | ___          |
| 6    | 1  | Winston   | 500    | ___          |
+------+----+-----------+--------+--------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH weights AS (
    SELECT person_name, turn,
           SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight
    FROM Queue
)
SELECT person_name
FROM weights
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
```

---

## 1205. Monthly Transactions II

**Problem:** https://leetcode.com/problems/monthly-transactions-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195464845  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH approved AS (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, COUNT(*) AS approved_count, SUM(amount) AS approved_amount FROM Transactions WHERE state = 'approved' GROUP BY month, country), charged AS (SELECT DATE_FORMAT(c.trans_date, '%Y-%m') AS month, t.country, COUNT(*) AS chargeback_count, SUM(t.amount) AS chargeback_amount FROM Chargebacks c JOIN Transactions t ON t.id = c.trans_id GROUP BY month, t.country), keys_all AS (SELECT month, country FROM approved UNION SELECT month, country FROM charged) SELECT k.month, k.country, COALESCE(a.approved_count, 0) AS approved_count, COALESCE(a.approved_amount, 0) AS approved_amount, COALESCE(c.chargeback_count, 0) AS chargeback_count, COALESCE(c.chargeback_amount, 0) AS chargeback_amount FROM keys_all k LEFT JOIN approved a ON a.month = k.month AND a.country <=> k.country LEFT JOIN charged c ON c.month = k.month AND c.country <=> k.country;
```

---

## 1211. Queries Quality and Percentage

**Problem:** https://leetcode.com/problems/queries-quality-and-percentage/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225702  
**Language:** mysql

### Description

Table:  Queries 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The 
position
 column has a value from 
1
 to 
500
.
The 
rating
 column has a value from 
1
 to 
5
. Query with 
rating
 less than 3 is a poor query.
```
 
 
   
 
 We define query  quality  as: 
 
 
 The average of the ratio between query rating and its position. 
 
 
 We also define  poor query percentage  as: 
 
 
 The percentage of all queries with rating less than 3. 
 
 
 Write a solution to find each  query_name , the  quality  and  poor_query_percentage . 
 
 Both  quality  and  poor_query_percentage  should be  rounded to 2 decimal places . 
 
 When rounding to two decimal places, values exactly halfway between two possible results are rounded away from zero. For example, 0.125 is rounded to 0.13. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+

Output:
 
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+

Explanation:
 
Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT query_name,
       ROUND(AVG(rating * 1.0 / position), 2) AS quality,
       ROUND(100.0 * AVG(rating < 3), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;
```

---

## 1212. Team Scores in Football Tournament

**Problem:** https://leetcode.com/problems/team-scores-in-football-tournament/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195465018  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH pts AS (SELECT host_team AS team_id, CASE WHEN host_goals > guest_goals THEN 3 WHEN host_goals = guest_goals THEN 1 ELSE 0 END AS pts FROM Matches UNION ALL SELECT guest_team, CASE WHEN guest_goals > host_goals THEN 3 WHEN guest_goals = host_goals THEN 1 ELSE 0 END FROM Matches) SELECT t.team_id, t.team_name, COALESCE(SUM(p.pts), 0) AS num_points FROM Teams t LEFT JOIN pts p ON p.team_id = t.team_id GROUP BY t.team_id, t.team_name ORDER BY num_points DESC, t.team_id;
```

---

## 1225. Report Contiguous Dates

**Problem:** https://leetcode.com/problems/report-contiguous-dates/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195465225  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH dates AS (SELECT fail_date AS dt, 'failed' AS period_state FROM Failed WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31' UNION ALL SELECT success_date, 'succeeded' FROM Succeeded WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'), numbered AS (SELECT dt, period_state, ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY dt) AS rn FROM dates) SELECT period_state, MIN(dt) AS start_date, MAX(dt) AS end_date FROM numbered GROUP BY period_state, DATE_SUB(dt, INTERVAL rn DAY) ORDER BY start_date;
```

---

## 1241. Number of Comments per Post

**Problem:** https://leetcode.com/problems/number-of-comments-per-post/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195465430  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.sub_id AS post_id, COUNT(DISTINCT c.sub_id) AS number_of_comments FROM (SELECT DISTINCT sub_id FROM Submissions WHERE parent_id IS NULL) p LEFT JOIN Submissions c ON c.parent_id = p.sub_id GROUP BY p.sub_id ORDER BY post_id;
```

---

## 1251. Average Selling Price

**Problem:** https://leetcode.com/problems/average-selling-price/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225809  
**Language:** mysql

### Description

Table:  Prices 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
```
 
 
   
 
 Table:  UnitsSold 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold.
```
 
 
   
 
 Write a solution to find the average selling price for each product.  average_price  should be  rounded to 2 decimal places . If a product does not have any sold units, its average selling price is assumed to be 0. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+

Output:
 
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+

Explanation:
 
Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.product_id,
       ROUND(COALESCE(SUM(p.price * u.units) / NULLIF(SUM(u.units), 0), 0), 2) AS average_price
FROM Prices AS p
LEFT JOIN UnitsSold AS u
  ON u.product_id = p.product_id
 AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
```

---

## 1264. Page Recommendations

**Problem:** https://leetcode.com/problems/page-recommendations/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195465634  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH friends AS (SELECT user2_id AS user_id FROM Friendship WHERE user1_id = 1 UNION SELECT user1_id FROM Friendship WHERE user2_id = 1) SELECT DISTINCT l.page_id AS recommended_page FROM Likes l JOIN friends f ON l.user_id = f.user_id WHERE NOT EXISTS (SELECT 1 FROM Likes own WHERE own.user_id = 1 AND own.page_id = l.page_id);
```

---

## 1270. All People Report to the Given Manager

**Problem:** https://leetcode.com/problems/all-people-report-to-the-given-manager/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195465810  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE reports AS (SELECT employee_id FROM Employees WHERE manager_id = 1 AND employee_id <> 1 UNION DISTINCT SELECT e.employee_id FROM Employees e JOIN reports r ON e.manager_id = r.employee_id WHERE e.employee_id <> 1) SELECT employee_id FROM reports;
```

---

## 1280. Students and Examinations

**Problem:** https://leetcode.com/problems/students-and-examinations/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187225945  
**Language:** mysql

### Description

Table:  Students 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
```
 
 
   
 
 Table:  Subjects 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
```
 
 
   
 
 Table:  Examinations 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
```
 
 
   
 
 Write a solution to find the number of times each student attended each exam. 
 
 Return the result table ordered by  student_id  and  subject_name . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+

Output:
 
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+

Explanation:
 
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.student_id, s.student_name, sub.subject_name,
       COUNT(e.student_id) AS attended_exams
FROM Students AS s
CROSS JOIN Subjects AS sub
LEFT JOIN Examinations AS e
  ON e.student_id = s.student_id
 AND e.subject_name = sub.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
```

---

## 1285. Find the Start and End Number of Continuous Ranges

**Problem:** https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195465974  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH numbered AS (SELECT log_id, log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp FROM Logs) SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id FROM numbered GROUP BY grp ORDER BY start_id;
```

---

## 1294. Weather Type in Each Country

**Problem:** https://leetcode.com/problems/weather-type-in-each-country/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195466159  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT c.country_name, CASE WHEN AVG(w.weather_state) <= 15 THEN 'Cold' WHEN AVG(w.weather_state) >= 25 THEN 'Hot' ELSE 'Warm' END AS weather_type FROM Countries c JOIN Weather w ON w.country_id = c.country_id WHERE w.day >= '2019-11-01' AND w.day < '2019-12-01' GROUP BY c.country_id, c.country_name;
```

---

## 1303. Find the Team Size

**Problem:** https://leetcode.com/problems/find-the-team-size/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195466334  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size FROM Employee;
```

---

## 1308. Running Total for Different Genders

**Problem:** https://leetcode.com/problems/running-total-for-different-genders/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195466494  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT gender, day, SUM(score_points) OVER (PARTITION BY gender ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total FROM Scores ORDER BY gender, day;
```

---

## 1321. Restaurant Growth

**Problem:** https://leetcode.com/problems/restaurant-growth/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226086  
**Language:** mysql

### Description

Table:  Customer 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
In SQL,(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
amount is the total paid by a customer.
```
 
 
   
 
 You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day). 
 
 Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before).  average_amount  should be  rounded to two decimal places . 
 
 Return the result table ordered by  visited_on   in ascending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         | 
| 6           | Elvis        | 2019-01-06   | 140         | 
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         | 
| 1           | Jhon         | 2019-01-10   | 130         | 
| 3           | Jade         | 2019-01-10   | 150         | 
+-------------+--------------+--------------+-------------+

Output:
 
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+

Explanation:
 
1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH daily AS (
    SELECT visited_on, SUM(amount) AS day_amount
    FROM Customer
    GROUP BY visited_on
), rolling AS (
    SELECT visited_on,
           SUM(day_amount) OVER (
               ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           ) AS amount,
           COUNT(*) OVER (
               ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           ) AS days_in_window
    FROM daily
)
SELECT visited_on, amount,
       ROUND(amount / 7, 2) AS average_amount
FROM rolling
WHERE days_in_window = 7
ORDER BY visited_on;
```

---

## 1322. Ads Performance

**Problem:** https://leetcode.com/problems/ads-performance/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195466653  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ad_id, ROUND(IFNULL(100.0 * SUM(action = 'Clicked') / NULLIF(SUM(action IN ('Clicked', 'Viewed')), 0), 0), 2) AS ctr FROM Ads GROUP BY ad_id ORDER BY ctr DESC, ad_id;
```

---

## 1327. List the Products Ordered in a Period

**Problem:** https://leetcode.com/problems/list-the-products-ordered-in-a-period/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226203  
**Language:** mysql

### Description

Table:  Products 
 
```text
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.
```
 
 
   
 
 Table:  Orders 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.
```
 
 
   
 
 Write a solution to get the names of products that have at least  100  units ordered in  February 2020  and their amount. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Products table:
+-------------+-----------------------+------------------+
| product_id  | product_name          | product_category |
+-------------+-----------------------+------------------+
| 1           | Leetcode Solutions    | Book             |
| 2           | Jewels of Stringology | Book             |
| 3           | HP                    | Laptop           |
| 4           | Lenovo                | Laptop           |
| 5           | Leetcode Kit          | T-shirt          |
+-------------+-----------------------+------------------+
Orders table:
+--------------+--------------+----------+
| product_id   | order_date   | unit     |
+--------------+--------------+----------+
| 1            | 2020-02-05   | 60       |
| 1            | 2020-02-10   | 70       |
| 2            | 2020-01-18   | 30       |
| 2            | 2020-02-11   | 80       |
| 3            | 2020-02-17   | 2        |
| 3            | 2020-02-24   | 3        |
| 4            | 2020-03-01   | 20       |
| 4            | 2020-03-04   | 30       |
| 4            | 2020-03-04   | 60       |
| 5            | 2020-02-25   | 50       |
| 5            | 2020-02-27   | 50       |
| 5            | 2020-03-01   | 50       |
+--------------+--------------+----------+

Output:
 
+--------------------+---------+
| product_name       | unit    |
+--------------------+---------+
| Leetcode Solutions | 130     |
| Leetcode Kit       | 100     |
+--------------------+---------+

Explanation:
 
Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
Products with product_id = 2 is ordered in February a total of 80.
Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
Products with product_id = 4 was not ordered in February 2020.
Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products AS p
JOIN Orders AS o ON o.product_id = p.product_id
WHERE o.order_date >= '2020-02-01'
  AND o.order_date < '2020-03-01'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;
```

---

## 1336. Number of Transactions per Visit

**Problem:** https://leetcode.com/problems/number-of-transactions-per-visit/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195466810  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE per_visit AS (SELECT v.user_id, v.visit_date, COUNT(t.transaction_date) AS n FROM Visits v LEFT JOIN Transactions t ON t.user_id=v.user_id AND t.transaction_date=v.visit_date GROUP BY v.user_id,v.visit_date), nums AS (SELECT 0 AS n UNION ALL SELECT n+1 FROM nums WHERE n < (SELECT MAX(n) FROM per_visit)) SELECT nums.n AS transactions_count, COUNT(p.n) AS visits_count FROM nums LEFT JOIN per_visit p ON p.n=nums.n GROUP BY nums.n ORDER BY nums.n;
```

---

## 1341. Movie Rating

**Problem:** https://leetcode.com/problems/movie-rating/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226342  
**Language:** mysql

### Description

Table:  Movies 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
Each movie has a unique title.
```
 
 
 Table:  Users 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.
```
 
 
 Table:  MovieRating 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.
```
 
 
   
 
 Write a solution to: 
 
 
 Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name. 
 
 Find the movie name with the  highest average  rating in  February 2020 . In case of a tie, return the lexicographically smaller movie name. 
 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+

Output:
 
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+

Explanation:
 
Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
(SELECT u.name AS results
 FROM Users AS u
 JOIN MovieRating AS r ON r.user_id = u.user_id
 GROUP BY u.user_id, u.name
 ORDER BY COUNT(*) DESC, u.name ASC
 LIMIT 1)
UNION ALL
(SELECT m.title AS results
 FROM Movies AS m
 JOIN MovieRating AS r ON r.movie_id = m.movie_id
 WHERE r.created_at >= '2020-02-01'
   AND r.created_at < '2020-03-01'
 GROUP BY m.movie_id, m.title
 ORDER BY AVG(r.rating) DESC, m.title ASC
 LIMIT 1);
```

---

## 1350. Students With Invalid Departments

**Problem:** https://leetcode.com/problems/students-with-invalid-departments/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195467013  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.id, s.name FROM Students s LEFT JOIN Departments d ON d.id=s.department_id WHERE d.id IS NULL;
```

---

## 1355. Activity Participants

**Problem:** https://leetcode.com/problems/activity-participants/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195467194  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH counts AS (SELECT activity, COUNT(*) AS cnt FROM Friends GROUP BY activity) SELECT activity FROM counts WHERE cnt > (SELECT MIN(cnt) FROM counts) AND cnt < (SELECT MAX(cnt) FROM counts);
```

---

## 1364. Number of Trusted Contacts of a Customer

**Problem:** https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195467374  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT i.invoice_id, c.customer_name, i.price, COUNT(ct.contact_email) AS contacts_cnt, COUNT(c2.customer_id) AS trusted_contacts_cnt FROM Invoices i JOIN Customers c ON c.customer_id=i.user_id LEFT JOIN Contacts ct ON ct.user_id=c.customer_id LEFT JOIN Customers c2 ON c2.email=ct.contact_email GROUP BY i.invoice_id,c.customer_name,i.price ORDER BY i.invoice_id;
```

---

## 1369. Get the Second Most Recent Activity

**Problem:** https://leetcode.com/problems/get-the-second-most-recent-activity/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195467571  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT username,activity,startDate,endDate, ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) AS rn, COUNT(*) OVER (PARTITION BY username) AS cnt FROM UserActivity) SELECT username,activity,startDate,endDate FROM ranked WHERE rn=2 OR (cnt=1 AND rn=1);
```

---

## 1378. Replace Employee ID With The Unique Identifier

**Problem:** https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226466  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
```
 
 
   
 
 Table:  EmployeeUNI 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
```
 
 
   
 
 Write a solution to show the  unique ID  of each user, If a user does not have a unique ID replace just show  null . 
 
 Return the result table in  any  order. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+

Output:
 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+

Explanation:
 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT u.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS u ON e.id = u.id;
```

---

## 1384. Total Sales Amount by Year

**Problem:** https://leetcode.com/problems/total-sales-amount-by-year/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195467738  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH years AS (SELECT 2018 AS y UNION ALL SELECT 2019 UNION ALL SELECT 2020) SELECT s.product_id,p.product_name,CAST(y.y AS CHAR) AS report_year, (DATEDIFF(LEAST(s.period_end,MAKEDATE(y.y,1)+INTERVAL 1 YEAR-INTERVAL 1 DAY), GREATEST(s.period_start,MAKEDATE(y.y,1)))+1)*s.average_daily_sales AS total_amount FROM Sales s JOIN Product p ON p.product_id=s.product_id JOIN years y ON s.period_start <= MAKEDATE(y.y,1)+INTERVAL 1 YEAR-INTERVAL 1 DAY AND s.period_end >= MAKEDATE(y.y,1) ORDER BY s.product_id,report_year;
```

---

## 1393. Capital Gain/Loss

**Problem:** https://leetcode.com/problems/capital-gainloss/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226608  
**Language:** mysql

### Description

Table:  Stocks 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
The operation column is an ENUM (category) of type ('Sell', 'Buy')
Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day. It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.
```
 
 
   
 
 Write a solution to report the  Capital gain/loss  for each stock. 
 
 The  Capital gain/loss  of a stock is the total gain or loss after buying and selling the stock one or many times. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Stocks table:
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+

Output:
 
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
+---------------+-------------------+

Explanation:
 
Leetcode stock was bought at day 1 for 1000$ and was sold at day 5 for 9000$. Capital gain = 9000 - 1000 = 8000$.
Handbags stock was bought at day 17 for 30000$ and was sold at day 29 for 7000$. Capital loss = 7000 - 30000 = -23000$.
Corona Masks stock was bought at day 1 for 10$ and was sold at day 3 for 1010$. It was bought again at day 4 for 1000$ and was sold at day 5 for 500$. At last, it was bought at day 6 for 1000$ and was sold at day 10 for 10000$. Capital gain/loss is the sum of capital gains/losses for each ('Buy' --> 'Sell') operation = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 1000 - 500 + 9000 = 9500$.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT stock_name,
       SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
```

---

## 1398. Customers Who Bought Products A and B but Not C

**Problem:** https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195467948  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT c.customer_id,c.customer_name FROM Customers c JOIN Orders o ON o.customer_id=c.customer_id GROUP BY c.customer_id,c.customer_name HAVING SUM(o.product_name='A')>0 AND SUM(o.product_name='B')>0 AND SUM(o.product_name='C')=0 ORDER BY c.customer_id;
```

---

## 1407. Top Travellers

**Problem:** https://leetcode.com/problems/top-travellers/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226740  
**Language:** mysql

### Description

Table:  Users 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the column with unique values for this table.
name is the name of the user.
```
 
 
   
 
 Table:  Rides 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id is the column with unique values for this table.
user_id is the id of the user who traveled the distance "distance".
```
 
 
   
 
 Write a solution to report the distance traveled by each user. 
 
 Return the result table ordered by  travelled_distance  in  descending order , if two or more users traveled the same distance, order them by their  name  in  ascending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Users table:
+------+-----------+
| id   | name      |
+------+-----------+
| 1    | Alice     |
| 2    | Bob       |
| 3    | Alex      |
| 4    | Donald    |
| 7    | Lee       |
| 13   | Jonathan  |
| 19   | Elvis     |
+------+-----------+
Rides table:
+------+----------+----------+
| id   | user_id  | distance |
+------+----------+----------+
| 1    | 1        | 120      |
| 2    | 2        | 317      |
| 3    | 3        | 222      |
| 4    | 7        | 100      |
| 5    | 13       | 312      |
| 6    | 19       | 50       |
| 7    | 7        | 120      |
| 8    | 19       | 400      |
| 9    | 7        | 230      |
+------+----------+----------+

Output:
 
+----------+--------------------+
| name     | travelled_distance |
+----------+--------------------+
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
+----------+--------------------+

Explanation:
 
Elvis and Lee traveled 450 miles, Elvis is the top traveler as his name is alphabetically smaller than Lee.
Bob, Jonathan, Alex, and Alice have only one ride and we just order them by the total distances of the ride.
Donald did not have any rides, the distance traveled by him is 0.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users AS u
LEFT JOIN Rides AS r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
```

---

## 1412. Find the Quiet Students in All Exams

**Problem:** https://leetcode.com/problems/find-the-quiet-students-in-all-exams/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195468156  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH scored AS (SELECT student_id,score,MIN(score) OVER (PARTITION BY exam_id) AS lo,MAX(score) OVER (PARTITION BY exam_id) AS hi FROM Exam) SELECT s.student_id,s.student_name FROM Student s JOIN scored e ON e.student_id=s.student_id GROUP BY s.student_id,s.student_name HAVING SUM(e.score=e.lo OR e.score=e.hi)=0 ORDER BY s.student_id;
```

---

## 1421. NPV Queries

**Problem:** https://leetcode.com/problems/npv-queries/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195468348  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT q.id,q.year,COALESCE(n.npv,0) AS npv FROM Queries q LEFT JOIN NPV n ON n.id=q.id AND n.year=q.year;
```

---

## 1435. Create a Session Bar Chart

**Problem:** https://leetcode.com/problems/create-a-session-bar-chart/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195468523  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT b.bin,COUNT(s.session_id) AS total FROM (SELECT '[0-5>' AS bin,0 AS lo,5 AS hi UNION ALL SELECT '[5-10>',5,10 UNION ALL SELECT '[10-15>',10,15 UNION ALL SELECT '15 or more',15,99999999) b LEFT JOIN Sessions s ON s.duration/60 >= b.lo AND s.duration/60 < b.hi GROUP BY b.bin,b.lo ORDER BY b.lo;
```

---

## 1440. Evaluate Boolean Expression

**Problem:** https://leetcode.com/problems/evaluate-boolean-expression/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195468721  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT e.left_operand,e.operator,e.right_operand,CASE WHEN (e.operator='>' AND v1.value>v2.value) OR (e.operator='<' AND v1.value<v2.value) OR (e.operator='=' AND v1.value=v2.value) THEN 'true' ELSE 'false' END AS value FROM Expressions e JOIN Variables v1 ON v1.name=e.left_operand JOIN Variables v2 ON v2.name=e.right_operand;
```

---

## 1445. Apples & Oranges

**Problem:** https://leetcode.com/problems/apples-oranges/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195468898  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT sale_date,SUM(CASE WHEN fruit='apples' THEN sold_num ELSE -sold_num END) AS diff FROM Sales GROUP BY sale_date ORDER BY sale_date;
```

---

## 1454. Active Users

**Problem:** https://leetcode.com/problems/active-users/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195469047  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH days AS (SELECT DISTINCT id,login_date FROM Logins), ranked AS (SELECT id,login_date,DATE_SUB(login_date,INTERVAL ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date) DAY) AS grp FROM days) SELECT DISTINCT a.id,a.name FROM Accounts a JOIN ranked r ON r.id=a.id GROUP BY a.id,a.name,r.grp HAVING COUNT(*)>=5 ORDER BY a.id;
```

---

## 1459. Rectangles Area

**Problem:** https://leetcode.com/problems/rectangles-area/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195469256  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT a.id AS p1,b.id AS p2,ABS(a.x_value-b.x_value)*ABS(a.y_value-b.y_value) AS area FROM Points a JOIN Points b ON a.id<b.id WHERE a.x_value<>b.x_value AND a.y_value<>b.y_value ORDER BY area DESC,p1,p2;
```

---

## 1468. Calculate Salaries

**Problem:** https://leetcode.com/problems/calculate-salaries/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195469429  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT company_id,employee_id,employee_name,ROUND(salary * CASE WHEN MAX(salary) OVER(PARTITION BY company_id)<1000 THEN 1 WHEN MAX(salary) OVER(PARTITION BY company_id)<=10000 THEN 0.76 ELSE 0.51 END) AS salary FROM Salaries;
```

---

## 1479. Sales by Day of the Week

**Problem:** https://leetcode.com/problems/sales-by-day-of-the-week/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195469581  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT i.item_category AS CATEGORY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=2 THEN o.quantity ELSE 0 END) AS MONDAY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=3 THEN o.quantity ELSE 0 END) AS TUESDAY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=4 THEN o.quantity ELSE 0 END) AS WEDNESDAY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=5 THEN o.quantity ELSE 0 END) AS THURSDAY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=6 THEN o.quantity ELSE 0 END) AS FRIDAY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=7 THEN o.quantity ELSE 0 END) AS SATURDAY, SUM(CASE WHEN DAYOFWEEK(o.order_date)=1 THEN o.quantity ELSE 0 END) AS SUNDAY FROM Items i LEFT JOIN Orders o ON o.item_id=i.item_id GROUP BY i.item_category ORDER BY i.item_category;
```

---

## 1484. Group Sold Products By The Date

**Problem:** https://leetcode.com/problems/group-sold-products-by-the-date/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226858  
**Language:** mysql

### Description

Table  Activities : 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
```
 
 
   
 
 Write a solution to find for each date the number of different products sold and their names. 
 
 The sold products names for each date should be sorted lexicographically. 
 
 Return the result table ordered by  sell_date . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+

Output:
 
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+

Explanation:
 
For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
For 2020-06-02, the Sold item is (Mask), we just return it.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT sell_date,
       COUNT(DISTINCT product) AS num_sold,
       GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
```

---

## 1495. Friendly Movies Streamed Last Month

**Problem:** https://leetcode.com/problems/friendly-movies-streamed-last-month/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195469747  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DISTINCT c.title FROM Content c JOIN TVProgram t ON t.content_id=c.content_id WHERE c.Kids_content='Y' AND c.content_type='Movies' AND t.program_date >= '2020-06-01' AND t.program_date < '2020-07-01';
```

---

## 1501. Countries You Can Safely Invest In

**Problem:** https://leetcode.com/problems/countries-you-can-safely-invest-in/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195469933  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH calls AS (SELECT caller_id AS person_id,duration FROM Calls UNION ALL SELECT callee_id,duration FROM Calls) SELECT c.name AS country FROM calls ca JOIN Person p ON p.id=ca.person_id JOIN Country c ON c.country_code=LEFT(p.phone_number,3) GROUP BY c.name HAVING AVG(ca.duration)>(SELECT AVG(duration) FROM Calls);
```

---

## 1511. Customer Order Frequency

**Problem:** https://leetcode.com/problems/customer-order-frequency/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195470091  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT c.customer_id,c.name FROM Customers c JOIN Orders o ON o.customer_id=c.customer_id JOIN Product p ON p.product_id=o.product_id WHERE o.order_date >= '2020-06-01' AND o.order_date < '2020-08-01' GROUP BY c.customer_id,c.name HAVING SUM(CASE WHEN MONTH(o.order_date)=6 THEN o.quantity*p.price ELSE 0 END)>=100 AND SUM(CASE WHEN MONTH(o.order_date)=7 THEN o.quantity*p.price ELSE 0 END)>=100;
```

---

## 1517. Find Users With Valid E-Mails

**Problem:** https://leetcode.com/problems/find-users-with-valid-e-mails/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187226990  
**Language:** mysql

### Description

Table:  Users 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
```
 
 
   
 
 Write a solution to find the users who have  valid emails . 
 
 A valid e-mail has a prefix name and a domain where: 
 
 
 The prefix name  is a string that may contain letters (upper or lower case), digits, underscore  '_' , period  '.' , and/or dash  '-' . The prefix name  must  start with a letter. 
 
 The domain  must be exactly  '@leetcode.com'  in lowercase. 
 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Users table:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+

Output:
 
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+

Explanation:
 
The mail of user 2 does not have a domain.
The mail of user 5 has the # sign which is not allowed.
The mail of user 6 does not have the leetcode domain.
The mail of user 7 starts with a period.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT user_id, name, mail
FROM Users
WHERE REGEXP_LIKE(mail, '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$', 'c');
```

---

## 1527. Patients With a Condition

**Problem:** https://leetcode.com/problems/patients-with-a-condition/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227099  
**Language:** mysql

### Description

Table:  Patients 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
```
 
 
   
 
 Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with  DIAB1  prefix. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+

Output:
 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+

Explanation:
 Bob and George both have a condition that starts with DIAB1.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';
```

---

## 1532. The Most Recent Three Orders

**Problem:** https://leetcode.com/problems/the-most-recent-three-orders/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195470267  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH r AS (SELECT c.name AS customer_name,c.customer_id,o.order_id,o.order_date,ROW_NUMBER() OVER(PARTITION BY c.customer_id ORDER BY o.order_date DESC,o.order_id DESC) AS rn FROM Customers c JOIN Orders o ON o.customer_id=c.customer_id) SELECT customer_name,customer_id,order_id,order_date FROM r WHERE rn<=3 ORDER BY customer_name,customer_id,order_date DESC;
```

---

## 1543. Fix Product Name Format

**Problem:** https://leetcode.com/problems/fix-product-name-format/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195470480  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT LOWER(TRIM(product_name)) AS product_name,DATE_FORMAT(sale_date,'%Y-%m') AS sale_date,COUNT(*) AS total FROM Sales GROUP BY LOWER(TRIM(product_name)),DATE_FORMAT(sale_date,'%Y-%m') ORDER BY product_name,sale_date;
```

---

## 1549. The Most Recent Orders for Each Product

**Problem:** https://leetcode.com/problems/the-most-recent-orders-for-each-product/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195470657  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH r AS (SELECT p.product_name,p.product_id,o.order_id,o.order_date, RANK() OVER(PARTITION BY p.product_id ORDER BY o.order_date DESC) AS rk FROM Products p JOIN Orders o ON o.product_id=p.product_id) SELECT product_name,product_id,order_id,order_date FROM r WHERE rk=1 ORDER BY product_name,product_id,order_id;
```

---

## 1555. Bank Account Summary

**Problem:** https://leetcode.com/problems/bank-account-summary/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195470827  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH balances AS (SELECT u.user_id,u.user_name,u.credit+COALESCE(SUM(CASE WHEN t.paid_by=u.user_id THEN -t.amount WHEN t.paid_to=u.user_id THEN t.amount ELSE 0 END),0) AS credit FROM Users u LEFT JOIN Transactions t ON t.paid_by=u.user_id OR t.paid_to=u.user_id GROUP BY u.user_id,u.user_name,u.credit) SELECT user_id,user_name,credit,IF(credit<0,'Yes','No') AS credit_limit_breached FROM balances;
```

---

## 1565. Unique Orders and Customers Per Month

**Problem:** https://leetcode.com/problems/unique-orders-and-customers-per-month/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195470995  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DATE_FORMAT(order_date,'%Y-%m') AS month,COUNT(DISTINCT order_id) AS order_count,COUNT(DISTINCT customer_id) AS customer_count FROM Orders WHERE invoice>20 GROUP BY DATE_FORMAT(order_date,'%Y-%m');
```

---

## 1571. Warehouse Manager

**Problem:** https://leetcode.com/problems/warehouse-manager/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195471172  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT w.name AS warehouse_name,SUM(w.units*p.Width*p.Length*p.Height) AS volume FROM Warehouse w JOIN Products p ON p.product_id=w.product_id GROUP BY w.name;
```

---

## 1581. Customer Who Visited but Did Not Make Any Transactions

**Problem:** https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227190  
**Language:** mysql

### Description

Table:  Visits 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.
```
 
 
   
 
 Table:  Transactions 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.
```
 
 
   
 
 Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits. 
 
 Return the result table sorted in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+

Output:
 
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+

Explanation:
 
Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
```

---

## 1587. Bank Account Summary II

**Problem:** https://leetcode.com/problems/bank-account-summary-ii/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227343  
**Language:** mysql

### Description

Table:  Users 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account is the primary key (column with unique values) for this table.
Each row of this table contains the account number of each user in the bank.
There will be no two users having the same name in the table.
```
 
 
   
 
 Table:  Transactions 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id is the primary key (column with unique values) for this table.
Each row of this table contains all changes made to all accounts.
amount is positive if the user received money and negative if they transferred money.
All accounts start with a balance of 0.
```
 
 
   
 
 Write a solution to report the name and balance of users with a balance higher than  10000 . The balance of an account is equal to the sum of the amounts of all transactions involving that account. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Users table:
+------------+--------------+
| account    | name         |
+------------+--------------+
| 900001     | Alice        |
| 900002     | Bob          |
| 900003     | Charlie      |
+------------+--------------+
Transactions table:
+------------+------------+------------+---------------+
| trans_id   | account    | amount     | transacted_on |
+------------+------------+------------+---------------+
| 1          | 900001     | 7000       |  2020-08-01   |
| 2          | 900001     | 7000       |  2020-09-01   |
| 3          | 900001     | -3000      |  2020-09-02   |
| 4          | 900002     | 1000       |  2020-09-12   |
| 5          | 900003     | 6000       |  2020-08-07   |
| 6          | 900003     | 6000       |  2020-09-07   |
| 7          | 900003     | -4000      |  2020-09-11   |
+------------+------------+------------+---------------+

Output:
 
+------------+------------+
| name       | balance    |
+------------+------------+
| Alice      | 11000      |
+------------+------------+

Explanation:
 
Alice's balance is (7000 + 7000 - 3000) = 11000.
Bob's balance is 1000.
Charlie's balance is (6000 + 6000 - 4000) = 8000.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT u.name, SUM(t.amount) AS balance
FROM Users AS u
JOIN Transactions AS t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
```

---

## 1596. The Most Frequently Ordered Products for Each Customer

**Problem:** https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195471336  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH counts AS (SELECT customer_id,product_id,COUNT(*) AS n FROM Orders GROUP BY customer_id,product_id), r AS (SELECT customer_id,product_id,DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY n DESC) AS rk FROM counts) SELECT r.customer_id,r.product_id,p.product_name FROM r JOIN Products p ON p.product_id=r.product_id WHERE rk=1;
```

---

## 1607. Sellers With No Sales

**Problem:** https://leetcode.com/problems/sellers-with-no-sales/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195471531  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.seller_name FROM Seller s WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.seller_id=s.seller_id AND o.sale_date >= '2020-01-01' AND o.sale_date < '2021-01-01') ORDER BY s.seller_name;
```

---

## 1613. Find the Missing IDs

**Problem:** https://leetcode.com/problems/find-the-missing-ids/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195471693  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE nums AS (SELECT 1 AS customer_id UNION ALL SELECT customer_id+1 FROM nums WHERE customer_id<(SELECT MAX(customer_id) FROM Customers)) SELECT n.customer_id AS ids FROM nums n LEFT JOIN Customers c ON c.customer_id=n.customer_id WHERE c.customer_id IS NULL ORDER BY ids;
```

---

## 1623. All Valid Triplets That Can Represent a Country

**Problem:** https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195471870  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT a.student_name AS member_A,b.student_name AS member_B,c.student_name AS member_C FROM SchoolA a JOIN SchoolB b ON a.student_id<>b.student_id AND a.student_name<>b.student_name JOIN SchoolC c ON c.student_id<>a.student_id AND c.student_id<>b.student_id AND c.student_name<>a.student_name AND c.student_name<>b.student_name;
```

---

## 1633. Percentage of Users Attended a Contest

**Problem:** https://leetcode.com/problems/percentage-of-users-attended-a-contest/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227487  
**Language:** mysql

### Description

Table:  Users 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.
```
 
 
   
 
 Table:  Register 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.
```
 
 
   
 
 Write a solution to find the percentage of the users registered in each contest rounded to  two decimals . 
 
 Return the result table ordered by  percentage  in  descending order . In case of a tie, order it by  contest_id  in  ascending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+
Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+

Output:
 
+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208        | 100.0      |
| 209        | 100.0      |
| 210        | 100.0      |
| 215        | 66.67      |
| 207        | 33.33      |
+------------+------------+

Explanation:
 
All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT r.contest_id,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register AS r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
```

---

## 1635. Hopper Company Queries I

**Problem:** https://leetcode.com/problems/hopper-company-queries-i/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195608299  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 12
)
SELECT
    m.month,
    (
        SELECT COUNT(*)
        FROM Drivers d
        WHERE d.join_date <= LAST_DAY(
            DATE_ADD('2020-01-01', INTERVAL (m.month - 1) MONTH)
        )
    ) AS active_drivers,
    (
        SELECT COUNT(*)
        FROM Rides r
        JOIN AcceptedRides a
            ON r.ride_id = a.ride_id
        WHERE r.requested_at >= DATE_ADD(
                  '2020-01-01', INTERVAL (m.month - 1) MONTH
              )
          AND r.requested_at < DATE_ADD(
                  '2020-01-01', INTERVAL m.month MONTH
              )
    ) AS accepted_rides
FROM Months m
ORDER BY m.month;
```

---

## 1645. Hopper Company Queries II

**Problem:** https://leetcode.com/problems/hopper-company-queries-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195608453  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH RECURSIVE Months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM Months
    WHERE month < 12
)
SELECT
    m.month,
    IFNULL(
        ROUND(
            (
                SELECT COUNT(DISTINCT a.driver_id)
                FROM Rides r
                JOIN AcceptedRides a
                    ON r.ride_id = a.ride_id
                WHERE YEAR(r.requested_at) = 2020
                  AND MONTH(r.requested_at) = m.month
            ) * 100.0 /
            NULLIF(
                (
                    SELECT COUNT(*)
                    FROM Drivers d
                    WHERE d.join_date <= LAST_DAY(
                        DATE_ADD('2020-01-01',
                            INTERVAL (m.month - 1) MONTH)
                    )
                ), 0
            ),
            2
        ),
        0
    ) AS working_percentage
FROM Months m
ORDER BY m.month;
```

---

## 1651. Hopper Company Queries III

**Problem:** https://leetcode.com/problems/hopper-company-queries-iii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195474550  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE months AS (SELECT 1 AS month UNION ALL SELECT month+1 FROM months WHERE month<12), monthly AS (SELECT MONTH(r.requested_at) AS month,SUM(a.ride_distance) AS distance,SUM(a.ride_duration) AS duration FROM Rides r JOIN AcceptedRides a ON a.ride_id=r.ride_id WHERE YEAR(r.requested_at)=2020 GROUP BY MONTH(r.requested_at)), totals AS (SELECT m.month,COALESCE(x.distance,0) AS distance,COALESCE(x.duration,0) AS duration FROM months m LEFT JOIN monthly x ON x.month=m.month) SELECT a.month,ROUND(AVG(b.distance),2) AS average_ride_distance,ROUND(AVG(b.duration),2) AS average_ride_duration FROM totals a JOIN totals b ON b.month BETWEEN a.month AND a.month+2 WHERE a.month<=10 GROUP BY a.month ORDER BY a.month;
```

---

## 1661. Average Time of Process per Machine

**Problem:** https://leetcode.com/problems/average-time-of-process-per-machine/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227625  
**Language:** mysql

### Description

Table:  Activity 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The `start` timestamp will always be less than or equal to the `end` timestamp for every `(machine_id, process_id)` pair.
It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.
```
 
 
   
 
 There is a factory website that has several machines, each running one or more processes. Write a solution to find the  average time  each machine takes to complete a process. 
 
 The time to complete a process is the  'end' timestamp  minus the  'start' timestamp . The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run on that machine. 
 
 The resulting table should have the  machine_id  along with the  average time  as  processing_time , which should be  rounded to 3 decimal places . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+

Output:
 
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+

Explanation:
 
There are 3 machines running 2 processes each.
Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.machine_id,
       ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM Activity AS s
JOIN Activity AS e
  ON s.machine_id = e.machine_id
 AND s.process_id = e.process_id
 AND s.activity_type = 'start'
 AND e.activity_type = 'end'
GROUP BY s.machine_id;
```

---

## 1667. Fix Names in a Table

**Problem:** https://leetcode.com/problems/fix-names-in-a-table/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227765  
**Language:** mysql

### Description

Table:  Users 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
```
 
 
   
 
 Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase. 
 
 Return the result table ordered by  user_id . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+

Output:
 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT user_id,
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
```

---

## 1677. Product's Worth Over Invoices

**Problem:** https://leetcode.com/problems/products-worth-over-invoices/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195608630  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    p.name,
    IFNULL(SUM(i.rest), 0) AS rest,
    IFNULL(SUM(i.paid), 0) AS paid,
    IFNULL(SUM(i.canceled), 0) AS canceled,
    IFNULL(SUM(i.refunded), 0) AS refunded
FROM Product p
LEFT JOIN Invoice i
    ON p.product_id = i.product_id
GROUP BY p.product_id, p.name
ORDER BY p.name;
```

---

## 1683. Invalid Tweets

**Problem:** https://leetcode.com/problems/invalid-tweets/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195475900  
**Language:** mysql

### Description

Table:  Tweets 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.
```
 
 
   
 
 Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is  strictly greater  than  15 . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+

Output:
 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+

Explanation:
 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content)>15;
```

---

## 1693. Daily Leads and Partners

**Problem:** https://leetcode.com/problems/daily-leads-and-partners/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227889  
**Language:** mysql

### Description

Table:  DailySales 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.
```
 
 
   
 
 For each  date_id  and  make_name , find the number of  distinct   lead_id 's and  distinct   partner_id 's. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+

Output:
 
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+

Explanation:
 
For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS unique_leads,
       COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
```

---

## 1699. Number of Calls Between Two Persons

**Problem:** https://leetcode.com/problems/number-of-calls-between-two-persons/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195476068  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT LEAST(from_id,to_id) AS person1,GREATEST(from_id,to_id) AS person2,COUNT(*) AS call_count,SUM(duration) AS total_duration FROM Calls GROUP BY LEAST(from_id,to_id),GREATEST(from_id,to_id);
```

---

## 1709. Biggest Window Between Visits

**Problem:** https://leetcode.com/problems/biggest-window-between-visits/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195476227  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH visits AS (SELECT DISTINCT user_id,visit_date FROM UserVisits), next_visits AS (SELECT user_id,visit_date,LEAD(visit_date,1,'2021-01-01') OVER(PARTITION BY user_id ORDER BY visit_date) AS next_date FROM visits) SELECT user_id,MAX(DATEDIFF(next_date,visit_date)) AS biggest_window FROM next_visits GROUP BY user_id ORDER BY user_id;
```

---

## 1715. Count Apples and Oranges

**Problem:** https://leetcode.com/problems/count-apples-and-oranges/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195476401  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT SUM(b.apple_count+COALESCE(c.apple_count,0)) AS apple_count,SUM(b.orange_count+COALESCE(c.orange_count,0)) AS orange_count FROM Boxes b LEFT JOIN Chests c ON c.chest_id=b.chest_id;
```

---

## 1729. Find Followers Count

**Problem:** https://leetcode.com/problems/find-followers-count/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187227998  
**Language:** mysql

### Description

Table:  Followers 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.
```
 
 
   
 
 Write a solution that will, for each user, return the number of followers. 
 
 Return the result table ordered by  user_id  in ascending order. 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+

Output:
 
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+

Explanation:
 
The followers of 0 are {1}
The followers of 1 are {0}
The followers of 2 are {0,1}
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```

---

## 1731. The Number of Employees Which Report to Each Employee

**Problem:** https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187228107  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).
```
 
 
   
 
 For this problem, we will consider a  manager  an employee who has at least 1 other employee reporting to them. 
 
 Write a solution to report the ids and the names of all  managers , the number of employees who report  directly  to them, and the average age of the reports rounded to the nearest integer. 
 
 Return the result table ordered by  employee_id . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+

Output:
 
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+

Explanation:
 Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
```
 
 
 Example 2: 
 
```text
Input:
 
Employees table:
+-------------+---------+------------+-----+ 
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+ 

Output:
 
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT m.employee_id, m.name,
       COUNT(*) AS reports_count,
       ROUND(AVG(e.age)) AS average_age
FROM Employees AS m
JOIN Employees AS e ON e.reports_to = m.employee_id
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;
```

---

## 1741. Find Total Time Spent by Each Employee

**Problem:** https://leetcode.com/problems/find-total-time-spent-by-each-employee/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187228221  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
(emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
The table shows the employees' entries and exits in an office.
event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
in_time and out_time are between 1 and 1440.
It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
```
 
 
   
 
 Write a solution to calculate the total time  in minutes  spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is  out_time - in_time . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employees table:
+--------+------------+---------+----------+
| emp_id | event_day  | in_time | out_time |
+--------+------------+---------+----------+
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-03 | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-09 | 47      | 74       |
+--------+------------+---------+----------+

Output:
 
+------------+--------+------------+
| day        | emp_id | total_time |
+------------+--------+------------+
| 2020-11-28 | 1      | 173        |
| 2020-11-28 | 2      | 30         |
| 2020-12-03 | 1      | 41         |
| 2020-12-09 | 2      | 27         |
+------------+--------+------------+

Explanation:
 
Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT event_day AS day, emp_id,
       SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
```

---

## 1747. Leetflex Banned Accounts

**Problem:** https://leetcode.com/problems/leetflex-banned-accounts/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195608817  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT DISTINCT a.account_id
FROM LogInfo a
JOIN LogInfo b
    ON a.account_id = b.account_id
WHERE a.ip_address != b.ip_address
  AND a.login <= b.logout
  AND b.login <= a.logout;
```

---

## 1757. Recyclable and Low Fat Products

**Problem:** https://leetcode.com/problems/recyclable-and-low-fat-products/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187246534  
**Language:** mysql

### Description

Table:  Products 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
```
 
 
   
 
 Write a solution to find the ids of products that are both low fat and recyclable. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+

Output:
 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+

Explanation:
 Only products 1 and 3 are both low fat and recyclable.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

---

## 1767. Find the Subtasks That Did Not Execute

**Problem:** https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195477843  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE nums AS (SELECT 1 AS subtask_id UNION ALL SELECT subtask_id+1 FROM nums WHERE subtask_id<20) SELECT t.task_id,n.subtask_id FROM Tasks t JOIN nums n ON n.subtask_id<=t.subtasks_count LEFT JOIN Executed e ON e.task_id=t.task_id AND e.subtask_id=n.subtask_id WHERE e.task_id IS NULL;
```

---

## 1777. Product's Price for Each Store

**Problem:** https://leetcode.com/problems/products-price-for-each-store/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195478020  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT product_id,MAX(CASE WHEN store='store1' THEN price END) AS store1,MAX(CASE WHEN store='store2' THEN price END) AS store2,MAX(CASE WHEN store='store3' THEN price END) AS store3 FROM Products GROUP BY product_id;
```

---

## 1783. Grand Slam Titles

**Problem:** https://leetcode.com/problems/grand-slam-titles/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195478174  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.player_id, p.player_name, COUNT(*) AS grand_slams_count
FROM Players p JOIN (
 SELECT Wimbledon AS id FROM Championships UNION ALL
 SELECT Fr_open FROM Championships UNION ALL
 SELECT US_open FROM Championships UNION ALL
 SELECT Au_open FROM Championships
) w ON w.id=p.player_id
GROUP BY p.player_id,p.player_name;
```

---

## 1789. Primary Department for Each Employee

**Problem:** https://leetcode.com/problems/primary-department-for-each-employee/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187229480  
**Language:** mysql

### Description

Table:  Employee 
 
```text
+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.
```
 
 
   
 
 Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is  'N' . 
 
 Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+

Output:
 
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+

Explanation:
 
- The Primary department for employee 1 is 1.
- The Primary department for employee 2 is 1.
- The Primary department for employee 3 is 3.
- The Primary department for employee 4 is 3.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
       SELECT employee_id
       FROM Employee
       GROUP BY employee_id
       HAVING COUNT(*) = 1
   );
```

---

## 1795. Rearrange Products Table

**Problem:** https://leetcode.com/problems/rearrange-products-table/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187229602  
**Language:** mysql

### Description

Table:  Products 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.
```
 
 
   
 
 Write a solution to rearrange the  Products  table so that each row has  (product_id, store, price) . If a product is not available in a store, do  not  include a row with that  product_id  and  store  combination in the result table. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+

Output:
 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+

Explanation:
 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products WHERE store3 IS NOT NULL;
```

---

## 1809. Ad-Free Sessions

**Problem:** https://leetcode.com/problems/ad-free-sessions/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195478348  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.session_id FROM Playback p
WHERE NOT EXISTS (SELECT 1 FROM Ads a WHERE a.customer_id=p.customer_id
 AND a.timestamp BETWEEN p.start_time AND p.end_time);
```

---

## 1811. Find Interview Candidates

**Problem:** https://leetcode.com/problems/find-interview-candidates/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195478509  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH medals AS (
 SELECT contest_id, gold_medal AS user_id, 1 AS gold FROM Contests UNION ALL
 SELECT contest_id, silver_medal, 0 FROM Contests UNION ALL
 SELECT contest_id, bronze_medal, 0 FROM Contests
), runs AS (
 SELECT user_id, contest_id, ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY contest_id) AS rn
 FROM medals
), eligible AS (
 SELECT user_id FROM medals WHERE gold=1 GROUP BY user_id HAVING COUNT(*)>=3
 UNION
 SELECT user_id FROM runs GROUP BY user_id,contest_id-rn HAVING COUNT(*)>=3
)
SELECT u.name,u.mail FROM Users u JOIN eligible e ON e.user_id=u.user_id;
```

---

## 1821. Find Customers With Positive Revenue this Year

**Problem:** https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195478675  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT customer_id FROM Customers WHERE year=2021 AND revenue>0;
```

---

## 1831. Maximum Transaction Each Day

**Problem:** https://leetcode.com/problems/maximum-transaction-each-day/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195478838  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT transaction_id, amount, MAX(amount) OVER(PARTITION BY DATE(day)) AS day_max
 FROM Transactions
)
SELECT transaction_id FROM ranked WHERE amount=day_max ORDER BY transaction_id;
```

---

## 1841. League Statistics

**Problem:** https://leetcode.com/problems/league-statistics/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195608996  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH AllMatches AS (
    SELECT
        home_team_id AS team_id,
        home_team_goals AS goal_for,
        away_team_goals AS goal_against,
        CASE
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals = away_team_goals THEN 1
            ELSE 0
        END AS points
    FROM Matches

    UNION ALL

    SELECT
        away_team_id AS team_id,
        away_team_goals AS goal_for,
        home_team_goals AS goal_against,
        CASE
            WHEN away_team_goals > home_team_goals THEN 3
            WHEN away_team_goals = home_team_goals THEN 1
            ELSE 0
        END AS points
    FROM Matches
)
SELECT
    t.team_name,
    COUNT(*) AS matches_played,
    SUM(a.points) AS points,
    SUM(a.goal_for) AS goal_for,
    SUM(a.goal_against) AS goal_against,
    SUM(a.goal_for) - SUM(a.goal_against) AS goal_diff
FROM Teams t
JOIN AllMatches a
    ON t.team_id = a.team_id
GROUP BY t.team_id, t.team_name
ORDER BY points DESC, goal_diff DESC, team_name ASC;
```

---

## 1843. Suspicious Bank Accounts

**Problem:** https://leetcode.com/problems/suspicious-bank-accounts/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195480202  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH monthly AS (
 SELECT t.account_id,DATE_FORMAT(t.day,'%Y-%m-01') AS month_start,SUM(t.amount) AS income
 FROM Transactions t WHERE t.type='Creditor' GROUP BY t.account_id,DATE_FORMAT(t.day,'%Y-%m-01')
), high AS (
 SELECT m.account_id,STR_TO_DATE(m.month_start,'%Y-%m-%d') AS month_start
 FROM monthly m JOIN Accounts a ON a.account_id=m.account_id WHERE m.income>a.max_income
)
SELECT DISTINCT a.account_id FROM high a JOIN high b ON a.account_id=b.account_id
 AND b.month_start=DATE_ADD(a.month_start,INTERVAL 1 MONTH);
```

---

## 1853. Convert Date Format

**Problem:** https://leetcode.com/problems/convert-date-format/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195480403  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT DATE_FORMAT(day,'%W, %M %e, %Y') AS day FROM Days;
```

---

## 1867. Orders With Maximum Quantity Above Average

**Problem:** https://leetcode.com/problems/orders-with-maximum-quantity-above-average/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195480565  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH stats AS (
 SELECT order_id,MAX(quantity) AS mx,AVG(quantity) AS av FROM OrdersDetails GROUP BY order_id
)
SELECT order_id FROM stats WHERE mx>(SELECT MAX(av) FROM stats);
```

---

## 1873. Calculate Special Bonus

**Problem:** https://leetcode.com/problems/calculate-special-bonus/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187229710  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
```
 
 
   
 
 Write a solution to calculate the bonus of each employee. The bonus of an employee is  100%  of their salary if the ID of the employee is  an odd number  and  the employee's name does not start with the character  'M' . The bonus of an employee is  0  otherwise. 
 
 Return the result table ordered by  employee_id . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+

Output:
 
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+

Explanation:
 
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT employee_id,
       CASE WHEN MOD(employee_id, 2) = 1 AND name NOT LIKE 'M%'
            THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id;
```

---

## 1875. Group Employees of the Same Salary

**Problem:** https://leetcode.com/problems/group-employees-of-the-same-salary/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195480764  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH eligible AS (
 SELECT salary FROM Employees GROUP BY salary HAVING COUNT(*)>1
), numbered AS (
 SELECT salary,DENSE_RANK() OVER(ORDER BY salary) AS team_id FROM eligible
)
SELECT e.employee_id,e.name,e.salary,n.team_id FROM Employees e
JOIN numbered n ON n.salary=e.salary ORDER BY n.team_id,e.employee_id;
```

---

## 1890. The Latest Login in 2020

**Problem:** https://leetcode.com/problems/the-latest-login-in-2020/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187229826  
**Language:** mysql

### Description

Table:  Logins 
 
```text
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
Each row contains information about the login time for the user with ID user_id.
```
 
 
   
 
 Write a solution to report the  latest  login for all users in the year  2020 . Do  not  include the users who did not login in  2020 . 
 
 Return the result table  in any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Logins table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |
+---------+---------------------+

Output:
 
+---------+---------------------+
| user_id | last_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
+---------+---------------------+

Explanation:
 
User 6 logged into their account 3 times but only once in 2020, so we include this login in the result table.
User 8 logged into their account 2 times in 2020, once in February and once in December. We include only the latest one (December) in the result table.
User 2 logged into their account 2 times but only once in 2020, so we include this login in the result table.
User 14 did not login in 2020, so we do not include them in the result table.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp >= '2020-01-01'
  AND time_stamp < '2021-01-01'
GROUP BY user_id;
```

---

## 1892. Page Recommendations II

**Problem:** https://leetcode.com/problems/page-recommendations-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195480944  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH friends AS (
 SELECT user1_id AS user_id,user2_id AS friend_id FROM Friendship
 UNION ALL SELECT user2_id,user1_id FROM Friendship
)
SELECT f.user_id,l.page_id,COUNT(DISTINCT f.friend_id) AS friends_likes
FROM friends f JOIN Likes l ON l.user_id=f.friend_id
WHERE NOT EXISTS (SELECT 1 FROM Likes own WHERE own.user_id=f.user_id AND own.page_id=l.page_id)
GROUP BY f.user_id,l.page_id;
```

---

## 1907. Count Salary Categories

**Problem:** https://leetcode.com/problems/count-salary-categories/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187229940  
**Language:** mysql

### Description

Table:  Accounts 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
```
 
 
   
 
 Write a solution to calculate the number of bank accounts for each salary category. The salary categories are: 
 
 
 "Low Salary" : All the salaries  strictly less  than  $20000 . 
 
 "Average Salary" : All the salaries in the  inclusive  range  [$20000, $50000] . 
 
 "High Salary" : All the salaries  strictly greater  than  $50000 . 
 
 
 The result table  must  contain all three categories. If there are no accounts in a category, return  0 . 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+

Output:
 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+

Explanation:
 
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT 'Low Salary' AS category,
       COUNT(CASE WHEN income < 20000 THEN 1 END) AS accounts_count
FROM Accounts
UNION ALL
SELECT 'Average Salary',
       COUNT(CASE WHEN income BETWEEN 20000 AND 50000 THEN 1 END)
FROM Accounts
UNION ALL
SELECT 'High Salary',
       COUNT(CASE WHEN income > 50000 THEN 1 END)
FROM Accounts;
```

---

## 1917. Leetcodify Friends Recommendations

**Problem:** https://leetcode.com/problems/leetcodify-friends-recommendations/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195609140  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH CommonSongs AS (
    SELECT
        a.user_id,
        b.user_id AS recommended_id,
        a.day
    FROM Listens a
    JOIN Listens b
        ON a.song_id = b.song_id
        AND a.day = b.day
        AND a.user_id != b.user_id
    GROUP BY
        a.user_id,
        b.user_id,
        a.day
    HAVING COUNT(DISTINCT a.song_id) >= 3
)
SELECT DISTINCT
    c.user_id,
    c.recommended_id
FROM CommonSongs c
WHERE NOT EXISTS (
    SELECT 1
    FROM Friendship f
    WHERE
        (f.user1_id = c.user_id
         AND f.user2_id = c.recommended_id)
        OR
        (f.user1_id = c.recommended_id
         AND f.user2_id = c.user_id)
);
```

---

## 1919. Leetcodify Similar Friends

**Problem:** https://leetcode.com/problems/leetcodify-similar-friends/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195482314  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH listens AS (SELECT DISTINCT user_id,song_id,day FROM Listens)
SELECT DISTINCT f.user1_id,f.user2_id
FROM Friendship f JOIN listens a ON a.user_id=f.user1_id
JOIN listens b ON b.user_id=f.user2_id AND b.day=a.day AND b.song_id=a.song_id
GROUP BY f.user1_id,f.user2_id,a.day HAVING COUNT(*)>=3;
```

---

## 1934. Confirmation Rate

**Problem:** https://leetcode.com/problems/confirmation-rate/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230165  
**Language:** mysql

### Description

Table:  Signups 
 
```text
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.
```
 
 
   
 
 Table:  Confirmations 
 
```text
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').
```
 
 
   
 
 The  confirmation rate  of a user is the number of  'confirmed'  messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is  0 . Round the confirmation rate to  two decimal  places. 
 
 Write a solution to find the  confirmation rate  of each user. 
 
 Return the result table in  any order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+

Output:
 
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+

Explanation:
 
User 6 did not request any confirmation messages. The confirmation rate is 0.
User 3 made 2 requests and both timed out. The confirmation rate is 0.
User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.user_id,
       ROUND(COALESCE(AVG(c.action = 'confirmed'), 0), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c ON c.user_id = s.user_id
GROUP BY s.user_id;
```

---

## 1939. Users That Actively Request Confirmation Messages

**Problem:** https://leetcode.com/problems/users-that-actively-request-confirmation-messages/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195482516  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ordered AS (
 SELECT user_id,time_stamp,LAG(time_stamp) OVER(PARTITION BY user_id ORDER BY time_stamp) AS prev_time
 FROM Confirmations
)
SELECT DISTINCT user_id FROM ordered
WHERE TIMESTAMPDIFF(SECOND,prev_time,time_stamp)<=86400;
```

---

## 1949. Strong Friendship

**Problem:** https://leetcode.com/problems/strong-friendship/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195482681  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH edges AS (
 SELECT user1_id AS u,user2_id AS v FROM Friendship UNION ALL
 SELECT user2_id,user1_id FROM Friendship
)
SELECT f.user1_id,f.user2_id,COUNT(*) AS common_friend
FROM Friendship f JOIN edges a ON a.u=f.user1_id
JOIN edges b ON b.u=f.user2_id AND b.v=a.v
GROUP BY f.user1_id,f.user2_id HAVING COUNT(*)>=3;
```

---

## 1951. All the Pairs With the Maximum Number of Common Followers

**Problem:** https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195482835  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH common AS (
 SELECT a.user_id AS user1_id,b.user_id AS user2_id,COUNT(*) AS cnt
 FROM Relations a JOIN Relations b ON a.follower_id=b.follower_id AND a.user_id<b.user_id
 GROUP BY a.user_id,b.user_id
)
SELECT user1_id,user2_id FROM common WHERE cnt=(SELECT MAX(cnt) FROM common);
```

---

## 1965. Employees With Missing Information

**Problem:** https://leetcode.com/problems/employees-with-missing-information/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230269  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.
```
 
 
   
 
 Table:  Salaries 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.
```
 
 
   
 
 Write a solution to report the IDs of all the employees with  missing information . The information of an employee is missing if: 
 
 
 The employee's  name  is missing, or 
 
 The employee's  salary  is missing. 
 
 
 Return the result table ordered by  employee_id   in ascending order . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
+-------------+--------+

Output:
 
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+

Explanation:
 
Employees 1, 2, 4, and 5 are working at this company.
The name of employee 1 is missing.
The salary of employee 2 is missing.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT employee_id
FROM (
    SELECT employee_id FROM Employees
    UNION ALL
    SELECT employee_id FROM Salaries
) AS combined
GROUP BY employee_id
HAVING COUNT(*) = 1
ORDER BY employee_id;
```

---

## 1972. First and Last Call On the Same Day

**Problem:** https://leetcode.com/problems/first-and-last-call-on-the-same-day/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195482991  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH calls AS (
 SELECT caller_id AS user_id,recipient_id AS other_id,call_time FROM Calls UNION ALL
 SELECT recipient_id,caller_id,call_time FROM Calls
), ranked AS (
 SELECT user_id,other_id,DATE(call_time) AS dt,
 FIRST_VALUE(other_id) OVER(PARTITION BY user_id,DATE(call_time) ORDER BY call_time) AS first_other,
 FIRST_VALUE(other_id) OVER(PARTITION BY user_id,DATE(call_time) ORDER BY call_time DESC) AS last_other
 FROM calls
)
SELECT DISTINCT user_id FROM ranked WHERE first_other=last_other;
```

---

## 1978. Employees Whose Manager Left the Company

**Problem:** https://leetcode.com/problems/employees-whose-manager-left-the-company/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230377  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null).
```
 
 
   
 
 Find the IDs of the employees whose salary is strictly less than  $30000  and whose manager left the company. When a manager leaves the company, their information is deleted from the  Employees  table, but the reports still have their  manager_id  set to the manager that left. 
 
 Return the result table ordered by  employee_id . 
 
 The result format is in the following example. 
 
   
 
 Example 1: 
 
```text
Input: 
 
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+

Output:
 
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

Explanation:
 
The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
Kalel's manager is employee 11, who is still in the company (Joziah).
Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT e.employee_id
FROM Employees AS e
LEFT JOIN Employees AS m ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;
```

---

## 1988. Find Cutoff Score for Each School

**Problem:** https://leetcode.com/problems/find-cutoff-score-for-each-school/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195483154  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.school_id,COALESCE(MIN(e.score),-1) AS score
FROM Schools s LEFT JOIN Exam e ON e.student_count<=s.capacity
GROUP BY s.school_id;
```

---

## 1990. Count the Number of Experiments

**Problem:** https://leetcode.com/problems/count-the-number-of-experiments/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195483319  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH platforms AS (SELECT 'Android' AS platform UNION ALL SELECT 'IOS' UNION ALL SELECT 'Web'),
 names AS (SELECT 'Reading' AS experiment_name UNION ALL SELECT 'Sports' UNION ALL SELECT 'Programming')
SELECT p.platform,n.experiment_name,COUNT(e.experiment_id) AS num_experiments
FROM platforms p CROSS JOIN names n LEFT JOIN Experiments e
 ON e.platform=p.platform AND e.experiment_name=n.experiment_name
GROUP BY p.platform,n.experiment_name;
```

---

## 2004. The Number of Seniors and Juniors to Join the Company

**Problem:** https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195483490  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT employee_id,experience,salary,
 SUM(salary) OVER(PARTITION BY experience ORDER BY salary,employee_id) AS running_cost
 FROM Candidates
), seniors AS (
 SELECT COUNT(*) AS cnt,COALESCE(MAX(running_cost),0) AS spent
 FROM ranked WHERE experience='Senior' AND running_cost<=70000
)
SELECT 'Senior' AS experience,cnt AS accepted_candidates FROM seniors
UNION ALL
SELECT 'Junior',COUNT(*) FROM ranked CROSS JOIN seniors
WHERE experience='Junior' AND running_cost<=70000-seniors.spent;
```

---

## 2010. The Number of Seniors and Juniors to Join the Company II

**Problem:** https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195483671  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT employee_id,experience,salary,
 SUM(salary) OVER(PARTITION BY experience ORDER BY salary,employee_id) AS running_cost
 FROM Candidates
), seniors AS (
 SELECT COALESCE(MAX(running_cost),0) AS spent FROM ranked
 WHERE experience='Senior' AND running_cost<=70000
)
SELECT r.employee_id FROM ranked r CROSS JOIN seniors s
WHERE (r.experience='Senior' AND r.running_cost<=70000)
 OR (r.experience='Junior' AND r.running_cost<=70000-s.spent);
```

---

## 2020. Number of Accounts That Did Not Stream

**Problem:** https://leetcode.com/problems/number-of-accounts-that-did-not-stream/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230479  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT COUNT(*) AS accounts_count
FROM Subscriptions s
WHERE s.start_date <= '2021-12-31'
  AND s.end_date >= '2021-01-01'
  AND NOT EXISTS (
      SELECT 1 FROM Streams t
      WHERE t.account_id = s.account_id
        AND t.stream_date BETWEEN '2021-01-01' AND '2021-12-31'
  );
```

---

## 2026. Low-Quality Problems

**Problem:** https://leetcode.com/problems/low-quality-problems/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230603  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT problem_id
FROM Problems
WHERE 5 * likes < 3 * (likes + dislikes)
ORDER BY problem_id;
```

---

## 2041. Accepted Candidates From the Interviews

**Problem:** https://leetcode.com/problems/accepted-candidates-from-the-interviews/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230726  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT c.candidate_id
FROM Candidates c
JOIN Rounds r ON c.interview_id = r.interview_id
WHERE c.years_of_exp >= 2
GROUP BY c.candidate_id
HAVING SUM(r.score) > 15;
```

---

## 2051. The Category of Each Member in the Store

**Problem:** https://leetcode.com/problems/the-category-of-each-member-in-the-store/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230839  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT m.member_id, m.name,
       CASE WHEN COUNT(v.visit_id) = 0 THEN 'Bronze'
            WHEN 100 * COUNT(p.visit_id) >= 80 * COUNT(v.visit_id) THEN 'Diamond'
            WHEN 100 * COUNT(p.visit_id) >= 50 * COUNT(v.visit_id) THEN 'Gold'
            ELSE 'Silver' END AS category
FROM Members m
LEFT JOIN Visits v ON v.member_id = m.member_id
LEFT JOIN Purchases p ON p.visit_id = v.visit_id
GROUP BY m.member_id, m.name;
```

---

## 2066. Account Balance

**Problem:** https://leetcode.com/problems/account-balance/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187230956  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT account_id, day,
       SUM(CASE WHEN type = 'Deposit' THEN amount ELSE -amount END)
           OVER (PARTITION BY account_id ORDER BY day) AS balance
FROM Transactions
ORDER BY account_id, day;
```

---

## 2072. The Winner University

**Problem:** https://leetcode.com/problems/the-winner-university/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231055  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT CASE WHEN ny.cnt > ca.cnt THEN 'New York University'
            WHEN ny.cnt < ca.cnt THEN 'California University'
            ELSE 'No Winner' END AS winner
FROM (SELECT COUNT(*) AS cnt FROM NewYork WHERE score >= 90) ny
CROSS JOIN (SELECT COUNT(*) AS cnt FROM California WHERE score >= 90) ca;
```

---

## 2082. The Number of Rich Customers

**Problem:** https://leetcode.com/problems/the-number-of-rich-customers/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231199  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500;
```

---

## 2084. Drop Type 1 Orders for Customers With Type 0 Orders

**Problem:** https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231313  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT o.order_id, o.customer_id, o.order_type
FROM Orders o
WHERE o.order_type = 0
   OR NOT EXISTS (SELECT 1 FROM Orders x
                  WHERE x.customer_id = o.customer_id
                    AND x.order_type = 0);
```

---

## 2112. The Airport With the Most Traffic

**Problem:** https://leetcode.com/problems/the-airport-with-the-most-traffic/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231438  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH Traffic AS (
    SELECT departure_airport AS airport_id, flights_count FROM Flights
    UNION ALL
    SELECT arrival_airport AS airport_id, flights_count FROM Flights
), Totals AS (
    SELECT airport_id, SUM(flights_count) AS total
    FROM Traffic GROUP BY airport_id
)
SELECT airport_id
FROM Totals
WHERE total = (SELECT MAX(total) FROM Totals);
```

---

## 2118. Build the Equation

**Problem:** https://leetcode.com/problems/build-the-equation/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231552  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT CONCAT(
         GROUP_CONCAT(
           CONCAT(IF(factor > 0, '+', ''), factor,
                  CASE WHEN power = 0 THEN ''
                       WHEN power = 1 THEN 'X'
                       ELSE CONCAT('X^', power) END)
           ORDER BY power DESC SEPARATOR ''), '=0') AS equation
FROM Terms;
```

---

## 2142. The Number of Passengers in Each Bus I

**Problem:** https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187246649  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH Counts AS (
    SELECT b.bus_id, b.arrival_time,
           COUNT(p.passenger_id) AS arrived
    FROM Buses b
    LEFT JOIN Passengers p ON p.arrival_time <= b.arrival_time
    GROUP BY b.bus_id, b.arrival_time
)
SELECT bus_id,
       arrived - LAG(arrived, 1, 0) OVER (ORDER BY arrival_time) AS passengers_cnt
FROM Counts
ORDER BY bus_id;
```

---

## 2153. The Number of Passengers in Each Bus II

**Problem:** https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231714  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE
BusTimes AS (
  SELECT bus_id, arrival_time, capacity,
         COALESCE(LAG(arrival_time) OVER (ORDER BY arrival_time), -1) AS prev_time,
         ROW_NUMBER() OVER (ORDER BY arrival_time) AS rn
  FROM Buses
),
Waiting AS (
  SELECT b.bus_id, b.capacity, b.rn,
         COUNT(p.passenger_id) AS new_waiting
  FROM BusTimes b
  LEFT JOIN Passengers p
    ON p.arrival_time > b.prev_time AND p.arrival_time <= b.arrival_time
  GROUP BY b.bus_id, b.capacity, b.rn
),
Boarding AS (
  SELECT rn, bus_id,
         LEAST(capacity, new_waiting) AS passengers_cnt,
         GREATEST(0, new_waiting - capacity) AS leftover
  FROM Waiting WHERE rn = 1
  UNION ALL
  SELECT w.rn, w.bus_id,
         LEAST(w.capacity, w.new_waiting + b.leftover),
         GREATEST(0, w.new_waiting + b.leftover - w.capacity)
  FROM Boarding b JOIN Waiting w ON w.rn = b.rn + 1
)
SELECT bus_id, passengers_cnt
FROM Boarding
ORDER BY bus_id;
```

---

## 2159. Order Two Columns Independently

**Problem:** https://leetcode.com/problems/order-two-columns-independently/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231877  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH A AS (
    SELECT first_col, ROW_NUMBER() OVER (ORDER BY first_col) AS rn FROM Data
), B AS (
    SELECT second_col, ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rn FROM Data
)
SELECT A.first_col, B.second_col
FROM A JOIN B USING (rn);
```

---

## 2173. Longest Winning Streak

**Problem:** https://leetcode.com/problems/longest-winning-streak/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187231984  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH Marked AS (
    SELECT player_id, match_day, result,
           SUM(CASE WHEN result = 'Win' THEN 0 ELSE 1 END)
             OVER (PARTITION BY player_id ORDER BY match_day) AS grp
    FROM Matches
), Runs AS (
    SELECT player_id, grp, COUNT(*) AS streak
    FROM Marked WHERE result = 'Win'
    GROUP BY player_id, grp
)
SELECT p.player_id, COALESCE(MAX(r.streak), 0) AS longest_streak
FROM (SELECT DISTINCT player_id FROM Matches) p
LEFT JOIN Runs r ON r.player_id = p.player_id
GROUP BY p.player_id;
```

---

## 2175. The Change in Global Rankings

**Problem:** https://leetcode.com/problems/the-change-in-global-rankings/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232105  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH Rankings AS (
    SELECT t.team_id, t.name,
           ROW_NUMBER() OVER (ORDER BY t.points DESC, t.name) AS old_rank,
           ROW_NUMBER() OVER (ORDER BY (t.points + p.points_change) DESC, t.name) AS new_rank
    FROM TeamPoints t JOIN PointsChange p USING (team_id)
)
SELECT team_id, name, CAST(old_rank AS SIGNED) - CAST(new_rank AS SIGNED) AS rank_diff
FROM Rankings;
```

---

## 2199. Finding the Topic of Each Post

**Problem:** https://leetcode.com/problems/finding-the-topic-of-each-post/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232226  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.post_id,
       COALESCE(GROUP_CONCAT(DISTINCT k.topic_id ORDER BY k.topic_id SEPARATOR ','),
                'Ambiguous!') AS topic
FROM Posts p
LEFT JOIN Keywords k
  ON INSTR(CONCAT(' ', LOWER(p.content), ' '),
           CONCAT(' ', LOWER(k.word), ' ')) > 0
GROUP BY p.post_id;
```

---

## 2205. The Number of Users That Are Eligible for Discount

**Problem:** https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232369  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT)
RETURNS INT
READS SQL DATA
BEGIN
    RETURN (
        SELECT COUNT(DISTINCT user_id)
        FROM Purchases
        WHERE time_stamp BETWEEN startDate AND endDate
          AND amount >= minAmount
    );
END;
```

---

## 2228. Users With Two Purchases Within Seven Days

**Problem:** https://leetcode.com/problems/users-with-two-purchases-within-seven-days/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232476  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH Ordered AS (
    SELECT user_id, purchase_date,
           LAG(purchase_date) OVER (
               PARTITION BY user_id ORDER BY purchase_date, purchase_id
           ) AS previous_date
    FROM Purchases
)
SELECT DISTINCT user_id
FROM Ordered
WHERE DATEDIFF(purchase_date, previous_date) <= 7
ORDER BY user_id;
```

---

## 2230. The Users That Are Eligible for Discount

**Problem:** https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232570  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
CREATE PROCEDURE getUserIDs(IN startDate DATE, IN endDate DATE, IN minAmount INT)
BEGIN
    SELECT DISTINCT user_id
    FROM Purchases
    WHERE time_stamp BETWEEN startDate AND endDate
      AND amount >= minAmount
    ORDER BY user_id;
END;
```

---

## 2238. Number of Times a Driver Was a Passenger

**Problem:** https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232670  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH Drivers AS (SELECT DISTINCT driver_id FROM Rides)
SELECT d.driver_id, COUNT(r.ride_id) AS cnt
FROM Drivers d
LEFT JOIN Rides r ON r.passenger_id = d.driver_id
GROUP BY d.driver_id;
```

---

## 2252. Dynamic Pivoting of a Table

**Problem:** https://leetcode.com/problems/dynamic-pivoting-of-a-table/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232769  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
CREATE PROCEDURE PivotProducts()
BEGIN
  SET SESSION group_concat_max_len = 1000000;
  SELECT GROUP_CONCAT(DISTINCT CONCAT('MAX(CASE WHEN store = ', QUOTE(store), ' THEN price END) AS `', REPLACE(store, '`', '``'), '`') ORDER BY store SEPARATOR ', ') INTO @cols FROM Products;
  SET @sql = CONCAT('SELECT product_id, ', @cols, ' FROM Products GROUP BY product_id');
  PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
END
```

---

## 2253. Dynamic Unpivoting of a Table

**Problem:** https://leetcode.com/problems/dynamic-unpivoting-of-a-table/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232869  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
CREATE PROCEDURE UnpivotProducts()
BEGIN
  SET SESSION group_concat_max_len = 1000000;
  SELECT GROUP_CONCAT(CONCAT('SELECT product_id, ', QUOTE(column_name), ' AS store, `', REPLACE(column_name, '`', '``'), '` AS price FROM Products WHERE `', REPLACE(column_name, '`', '``'), '` IS NOT NULL') SEPARATOR ' UNION ALL ') INTO @sql
  FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'Products' AND column_name <> 'product_id';
  PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
END
```

---

## 2292. Products With Three or More Orders in Two Consecutive Years

**Problem:** https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187232976  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH yearly AS (SELECT product_id, YEAR(purchase_date) AS yr, COUNT(*) AS cnt FROM Orders GROUP BY product_id, YEAR(purchase_date))
SELECT DISTINCT a.product_id FROM yearly a JOIN yearly b ON a.product_id=b.product_id AND b.yr=a.yr+1 WHERE a.cnt>=3 AND b.cnt>=3;
```

---

## 2298. Tasks Count in the Weekend

**Problem:** https://leetcode.com/problems/tasks-count-in-the-weekend/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187233064  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT SUM(DAYOFWEEK(submit_date) IN (1,7)) AS weekend_cnt, SUM(DAYOFWEEK(submit_date) NOT IN (1,7)) AS working_cnt FROM Tasks;
```

---

## 2308. Arrange Table by Gender

**Problem:** https://leetcode.com/problems/arrange-table-by-gender/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187233151  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT user_id, gender, ROW_NUMBER() OVER (PARTITION BY gender ORDER BY user_id) AS rn FROM Genders)
SELECT user_id, gender FROM ranked ORDER BY rn, FIELD(gender,'female','other','male');
```

---

## 2314. The First Day of the Maximum Recorded Degree in Each City

**Problem:** https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187233247  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT city_id, day, degree, ROW_NUMBER() OVER (PARTITION BY city_id ORDER BY degree DESC, day) AS rn FROM Weather) SELECT city_id, day, degree FROM ranked WHERE rn=1 ORDER BY city_id;
```

---

## 2324. Product Sales Analysis IV

**Problem:** https://leetcode.com/problems/product-sales-analysis-iv/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250389  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH spending AS (
 SELECT s.user_id, s.product_id, SUM(s.quantity*p.price) AS spent
 FROM Sales s JOIN Product p ON p.product_id=s.product_id
 GROUP BY s.user_id, s.product_id
), ranked AS (
 SELECT *, RANK() OVER (PARTITION BY user_id ORDER BY spent DESC) AS rk
 FROM spending
)
SELECT user_id, product_id FROM ranked WHERE rk=1;
```

---

## 2329. Product Sales Analysis V

**Problem:** https://leetcode.com/problems/product-sales-analysis-v/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187233443  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT s.user_id, SUM(s.quantity*p.price) AS spending FROM Sales s JOIN Product p USING (product_id) GROUP BY s.user_id ORDER BY spending DESC, s.user_id;
```

---

## 2339. All the Matches of the League

**Problem:** https://leetcode.com/problems/all-the-matches-of-the-league/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187233540  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT a.team_name AS home_team, b.team_name AS away_team FROM Teams a CROSS JOIN Teams b WHERE a.team_name<>b.team_name;
```

---

## 2346. Compute the Rank as a Percentage

**Problem:** https://leetcode.com/problems/compute-the-rank-as-a-percentage/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250480  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT student_id, department_id,
 COALESCE(ROUND(100.0*(RANK() OVER (PARTITION BY department_id ORDER BY mark DESC)-1)
 / NULLIF(COUNT(*) OVER (PARTITION BY department_id)-1,0),2),0) AS percentage
FROM Students;
```

---

## 2356. Number of Unique Subjects Taught by Each Teacher

**Problem:** https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187234519  
**Language:** mysql

### Description

Table:  Teacher 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
```
 
 
   
 
 Write a solution to calculate the number of unique subjects each teacher teaches in the university. 
 
 Return the result table in  any order . 
 
 The result format is shown in the following example. 
 
   
 
 Example 1: 
 
```text
Input:
 
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+

Output:
  
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+

Explanation:
 
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt FROM Teacher GROUP BY teacher_id;
```

---

## 2362. Generate the Invoice

**Problem:** https://leetcode.com/problems/generate-the-invoice/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187234609  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH totals AS (SELECT pu.invoice_id, SUM(pu.quantity*pr.price) AS total FROM Purchases pu JOIN Products pr USING(product_id) GROUP BY pu.invoice_id), chosen AS (SELECT invoice_id FROM totals ORDER BY total DESC, invoice_id LIMIT 1) SELECT pu.product_id, pu.quantity, pu.quantity*pr.price AS price FROM Purchases pu JOIN Products pr USING(product_id) JOIN chosen c USING(invoice_id);
```

---

## 2372. Calculate the Influence of Each Salesperson

**Problem:** https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250562  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT sp.salesperson_id, sp.name, COALESCE(SUM(sa.price),0) AS total
FROM Salesperson sp
LEFT JOIN Customer c ON c.salesperson_id=sp.salesperson_id
LEFT JOIN Sales sa ON sa.customer_id=c.customer_id
GROUP BY sp.salesperson_id, sp.name;
```

---

## 2377. Sort the Olympic Table

**Problem:** https://leetcode.com/problems/sort-the-olympic-table/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187246840  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT * FROM Olympic ORDER BY gold_medals DESC, silver_medals DESC, bronze_medals DESC, country;
```

---

## 2388. Change Null Values in a Table to the Previous Value

**Problem:** https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195483840  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH numbered AS (
 SELECT id,drink,ROW_NUMBER() OVER() AS rn FROM CoffeeShop
), grouped AS (
 SELECT id,drink,rn,COUNT(drink) OVER(ORDER BY rn) AS grp FROM numbered
)
SELECT id,MAX(drink) OVER(PARTITION BY grp) AS drink FROM grouped ORDER BY rn;
```

---

## 2394. Employees With Deductions

**Problem:** https://leetcode.com/problems/employees-with-deductions/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187235852  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH worked AS (SELECT employee_id, SUM(CEIL(TIMESTAMPDIFF(SECOND,in_time,out_time)/60)) AS mins FROM Logs GROUP BY employee_id) SELECT e.employee_id FROM Employees e LEFT JOIN worked w USING(employee_id) WHERE COALESCE(w.mins,0)<e.needed_hours*60;
```

---

## 2474. Customers With Strictly Increasing Purchases

**Problem:** https://leetcode.com/problems/customers-with-strictly-increasing-purchases/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250725  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH annual AS (
 SELECT customer_id, YEAR(order_date) AS yr, SUM(price) AS amount
 FROM Orders GROUP BY customer_id, YEAR(order_date)
), bounds AS (
 SELECT customer_id, MIN(yr) AS first_yr, MAX(yr) AS last_yr,
 COUNT(*) AS active_years
 FROM annual GROUP BY customer_id
), ranked AS (
 SELECT customer_id, yr, amount,
 ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY yr) AS year_rank,
 RANK() OVER (PARTITION BY customer_id ORDER BY amount) AS amount_rank
 FROM annual
)
SELECT b.customer_id
FROM bounds b JOIN ranked r ON r.customer_id=b.customer_id
GROUP BY b.customer_id, b.first_yr, b.last_yr, b.active_years
HAVING b.active_years=b.last_yr-b.first_yr+1
   AND COUNT(*)=COUNT(DISTINCT r.amount)
   AND SUM(r.year_rank<>r.amount_rank)=0;
```

---

## 2480. Form a Chemical Bond

**Problem:** https://leetcode.com/problems/form-a-chemical-bond/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195484013  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT m.symbol AS metal,n.symbol AS nonmetal
FROM Elements m CROSS JOIN Elements n
WHERE m.type='Metal' AND n.type='Nonmetal';
```

---

## 2494. Merge Overlapping Events in the Same Hall

**Problem:** https://leetcode.com/problems/merge-overlapping-events-in-the-same-hall/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236138  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ordered AS (SELECT hall_id,start_day,end_day, MAX(end_day) OVER (PARTITION BY hall_id ORDER BY start_day,end_day ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS previous_end FROM HallEvents), starts AS (SELECT *, CASE WHEN previous_end IS NULL OR start_day>previous_end THEN 1 ELSE 0 END AS new_group FROM ordered), grouped AS (SELECT *, SUM(new_group) OVER (PARTITION BY hall_id ORDER BY start_day,end_day) AS grp FROM starts) SELECT hall_id, MIN(start_day) AS start_day, MAX(end_day) AS end_day FROM grouped GROUP BY hall_id,grp;
```

---

## 2504. Concatenate the Name and the Profession

**Problem:** https://leetcode.com/problems/concatenate-the-name-and-the-profession/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187250974  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT person_id, CONCAT(name,'(',LEFT(profession,1),')') AS name
FROM Person ORDER BY person_id DESC;
```

---

## 2668. Find Latest Salaries

**Problem:** https://leetcode.com/problems/find-latest-salaries/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236328  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT emp_id, firstname, lastname, salary, department_id,
 ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY CAST(salary AS UNSIGNED) DESC) rn
 FROM Salary
)
SELECT emp_id, firstname, lastname, salary, department_id
FROM ranked WHERE rn=1 ORDER BY emp_id;
```

---

## 2669. Count Artist Occurrences On Spotify Ranking List

**Problem:** https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236449  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT artist, COUNT(*) AS occurrences FROM Spotify
GROUP BY artist ORDER BY occurrences DESC, artist;
```

---

## 2686. Immediate Food Delivery III

**Problem:** https://leetcode.com/problems/immediate-food-delivery-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236538  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT order_date,
 ROUND(100 * AVG(order_date = customer_pref_delivery_date), 2) AS immediate_percentage
FROM Delivery GROUP BY order_date ORDER BY order_date;
```

---

## 2687. Bikes Last Time Used 

**Problem:** https://leetcode.com/problems/bikes-last-time-used/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236626  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT bike_number, MAX(end_time) AS end_time
FROM Bikes GROUP BY bike_number ORDER BY end_time DESC;
```

---

## 2688. Find Active Users

**Problem:** https://leetcode.com/problems/find-active-users/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236720  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH x AS (
 SELECT user_id, created_at,
 LAG(created_at) OVER (PARTITION BY user_id ORDER BY created_at) AS previous_date
 FROM Users
)
SELECT DISTINCT user_id FROM x
WHERE DATEDIFF(created_at, previous_date) BETWEEN 0 AND 7;
```

---

## 2701. Consecutive Transactions with Increasing Amounts

**Problem:** https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236825  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH prev AS (
 SELECT customer_id, transaction_date, amount,
 LAG(transaction_date) OVER (PARTITION BY customer_id ORDER BY transaction_date) AS pd,
 LAG(amount) OVER (PARTITION BY customer_id ORDER BY transaction_date) AS pa
 FROM Transactions
), marks AS (
 SELECT *, SUM(CASE WHEN DATEDIFF(transaction_date,pd)=1 AND amount>pa THEN 0 ELSE 1 END)
 OVER (PARTITION BY customer_id ORDER BY transaction_date) AS grp FROM prev
)
SELECT customer_id, MIN(transaction_date) AS consecutive_start,
 MAX(transaction_date) AS consecutive_end FROM marks
GROUP BY customer_id, grp HAVING COUNT(*)>=3
ORDER BY customer_id, consecutive_start, consecutive_end;
```

---

## 2720. Popularity Percentage

**Problem:** https://leetcode.com/problems/popularity-percentage/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187236911  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH edges AS (
 SELECT user1 AS uid, user2 AS friend FROM Friends
 UNION ALL SELECT user2, user1 FROM Friends
), totals AS (SELECT COUNT(DISTINCT uid) AS n FROM edges)
SELECT uid AS user1, ROUND(100.0*COUNT(DISTINCT friend)/MAX(t.n),2) AS percentage_popularity
FROM edges CROSS JOIN totals t GROUP BY uid ORDER BY user1;
```

---

## 2738. Count Occurrences in Text

**Problem:** https://leetcode.com/problems/count-occurrences-in-text/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195494167  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT 'bull' AS word, COUNT(*) AS count FROM Files WHERE content LIKE '% bull %'
UNION ALL
SELECT 'bear' AS word, COUNT(*) AS count FROM Files WHERE content LIKE '% bear %';
```

---

## 2752. Customers with Maximum Number of Transactions on Consecutive Days

**Problem:** https://leetcode.com/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237102  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH days AS (
 SELECT DISTINCT customer_id, transaction_date FROM Transactions
), tagged AS (
 SELECT customer_id, DATE_SUB(transaction_date, INTERVAL
 ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date) DAY) AS grp
 FROM days
), runs AS (
 SELECT customer_id, COUNT(*) AS len FROM tagged GROUP BY customer_id,grp
)
SELECT DISTINCT customer_id FROM runs
WHERE len=(SELECT MAX(len) FROM runs) ORDER BY customer_id;
```

---

## 2783. Flight Occupancy and Waitlist Analysis

**Problem:** https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237184  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT f.flight_id,
 LEAST(f.capacity,COUNT(p.passenger_id)) AS booked_cnt,
 GREATEST(COUNT(p.passenger_id)-f.capacity,0) AS waitlist_cnt
FROM Flights f LEFT JOIN Passengers p ON p.flight_id=f.flight_id
GROUP BY f.flight_id,f.capacity ORDER BY f.flight_id;
```

---

## 2793. Status of Flight Tickets

**Problem:** https://leetcode.com/problems/status-of-flight-tickets/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195497010  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
    SELECT p.passenger_id, p.flight_id,
           ROW_NUMBER() OVER (
               PARTITION BY p.flight_id ORDER BY p.booking_time, p.passenger_id
           ) AS booking_rank
    FROM Passengers p
)
SELECT r.passenger_id,
       CASE WHEN r.booking_rank <= f.capacity THEN 'Confirmed'
            ELSE 'Waitlist' END AS Status
FROM ranked r JOIN Flights f ON f.flight_id = r.flight_id
ORDER BY r.passenger_id;
```

---

## 2820. Election Results

**Problem:** https://leetcode.com/problems/election-results/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195611085  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH VoteWeights AS (
    SELECT
        candidate,
        1.0 / COUNT(*) OVER (
            PARTITION BY voter
        ) AS vote
    FROM Votes
    WHERE candidate IS NOT NULL
),
CandidateVotes AS (
    SELECT
        candidate,
        SUM(vote) AS total_votes
    FROM VoteWeights
    GROUP BY candidate
),
RankedCandidates AS (
    SELECT
        candidate,
        RANK() OVER (
            ORDER BY total_votes DESC
        ) AS rnk
    FROM CandidateVotes
)
SELECT candidate
FROM RankedCandidates
WHERE rnk = 1
ORDER BY candidate;
```

---

## 2837. Total Traveled Distance

**Problem:** https://leetcode.com/problems/total-traveled-distance/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237286  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT u.user_id,u.name,COALESCE(SUM(r.distance),0) AS `traveled distance`
FROM Users u LEFT JOIN Rides r ON u.user_id=r.user_id
GROUP BY u.user_id,u.name ORDER BY u.user_id;
```

---

## 2853. Highest Salaries Difference

**Problem:** https://leetcode.com/problems/highest-salaries-difference/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187251136  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ABS(
 (SELECT MAX(salary) FROM Salaries WHERE department='Engineering') -
 (SELECT MAX(salary) FROM Salaries WHERE department='Marketing')
) AS salary_difference;
```

---

## 2854. Rolling Average Steps

**Problem:** https://leetcode.com/problems/rolling-average-steps/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237481  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH x AS (
 SELECT user_id,steps_date,
 ROUND(AVG(steps_count) OVER (PARTITION BY user_id ORDER BY steps_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW),2) AS rolling_average,
 LAG(steps_date,2) OVER (PARTITION BY user_id ORDER BY steps_date) AS date_two_before
 FROM Steps
)
SELECT user_id,steps_date,rolling_average FROM x
WHERE DATEDIFF(steps_date,date_two_before)=2
ORDER BY user_id,steps_date;
```

---

## 2893. Calculate Orders Within Each Interval

**Problem:** https://leetcode.com/problems/calculate-orders-within-each-interval/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237578  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT (minute+5) DIV 6 AS interval_no, SUM(order_count) AS total_orders
FROM Orders GROUP BY interval_no ORDER BY interval_no;
```

---

## 2922. Market Analysis III

**Problem:** https://leetcode.com/problems/market-analysis-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237680  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH counts AS (
 SELECT o.seller_id, COUNT(DISTINCT o.item_id) AS num_items
 FROM Orders o JOIN Users u ON o.seller_id=u.seller_id
 JOIN Items i ON o.item_id=i.item_id
 WHERE i.item_brand<>u.favorite_brand GROUP BY o.seller_id
)
SELECT seller_id,num_items FROM counts
WHERE num_items=(SELECT MAX(num_items) FROM counts) ORDER BY seller_id;
```

---

## 2978. Symmetric Coordinates

**Problem:** https://leetcode.com/problems/symmetric-coordinates/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237756  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH c AS (
 SELECT X,Y,ROW_NUMBER() OVER () AS rid FROM Coordinates
)
SELECT DISTINCT a.X AS x,a.Y AS y FROM c a JOIN c b
 ON a.X=b.Y AND a.Y=b.X AND a.rid<>b.rid
WHERE a.X<=a.Y ORDER BY x,y;
```

---

## 2984. Find Peak Calling Hours for Each City

**Problem:** https://leetcode.com/problems/find-peak-calling-hours-for-each-city/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237881  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH hourly AS (
 SELECT city,HOUR(call_time) AS peak_calling_hour,COUNT(*) AS number_of_calls
 FROM Calls GROUP BY city,HOUR(call_time)
), ranked AS (
 SELECT *,RANK() OVER (PARTITION BY city ORDER BY number_of_calls DESC) AS rk FROM hourly
)
SELECT city,peak_calling_hour,number_of_calls FROM ranked
WHERE rk=1 ORDER BY peak_calling_hour DESC,city DESC;
```

---

## 2985. Calculate Compressed Mean

**Problem:** https://leetcode.com/problems/calculate-compressed-mean/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187237981  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ROUND(SUM(item_count*order_occurrences)/SUM(order_occurrences),2)
 AS average_items_per_order FROM Orders;
```

---

## 2986. Find Third Transaction

**Problem:** https://leetcode.com/problems/find-third-transaction/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187238052  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH x AS (
 SELECT user_id,spend,transaction_date,
 ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) AS rn,
 LAG(spend) OVER (PARTITION BY user_id ORDER BY transaction_date) AS p1,
 LAG(spend,2) OVER (PARTITION BY user_id ORDER BY transaction_date) AS p2
 FROM Transactions
)
SELECT user_id,spend AS third_transaction_spend,transaction_date AS third_transaction_date
FROM x WHERE rn=3 AND spend>p1 AND spend>p2 ORDER BY user_id;
```

---

## 2987. Find Expensive Cities

**Problem:** https://leetcode.com/problems/find-expensive-cities/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187246923  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT city FROM Listings GROUP BY city
HAVING AVG(price)>(SELECT AVG(price) FROM Listings) ORDER BY city;
```

---

## 2988. Manager of the Largest Department

**Problem:** https://leetcode.com/problems/manager-of-the-largest-department/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187238980  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH counts AS (SELECT dep_id, COUNT(*) cnt FROM Employees GROUP BY dep_id)
SELECT e.emp_name AS manager_name, e.dep_id
FROM Employees e JOIN counts c ON e.dep_id=c.dep_id
WHERE e.position='Manager' AND c.cnt=(SELECT MAX(cnt) FROM counts)
ORDER BY e.dep_id;
```

---

## 2989. Class Performance

**Problem:** https://leetcode.com/problems/class-performance/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239060  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT MAX(assignment1+assignment2+assignment3)-MIN(assignment1+assignment2+assignment3) AS difference_in_score FROM Scores;
```

---

## 2990. Loan Types

**Problem:** https://leetcode.com/problems/loan-types/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239148  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT user_id FROM Loans GROUP BY user_id
HAVING SUM(loan_type='Mortgage')>0 AND SUM(loan_type='Refinance')>0 ORDER BY user_id;
```

---

## 2991. Top Three Wineries 

**Problem:** https://leetcode.com/problems/top-three-wineries/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239257  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH totals AS (SELECT country,winery,SUM(points) pts FROM Wineries GROUP BY country,winery),
ranked AS (SELECT country, CONCAT(winery,' (',pts,')') label,
ROW_NUMBER() OVER (PARTITION BY country ORDER BY pts DESC, winery ASC) rn FROM totals)
SELECT country,
MAX(CASE WHEN rn=1 THEN label END) AS top_winery,
COALESCE(MAX(CASE WHEN rn=2 THEN label END),'No second winery') AS second_winery,
COALESCE(MAX(CASE WHEN rn=3 THEN label END),'No third winery') AS third_winery
FROM ranked GROUP BY country ORDER BY country;
```

---

## 2993. Friday Purchases I

**Problem:** https://leetcode.com/problems/friday-purchases-i/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239345  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT CEIL(DAYOFMONTH(purchase_date)/7) AS week_of_month, purchase_date,
SUM(amount_spend) AS total_amount FROM Purchases
WHERE purchase_date BETWEEN '2023-11-01' AND '2023-11-30'
AND DAYOFWEEK(purchase_date)=6 GROUP BY purchase_date ORDER BY week_of_month;
```

---

## 2994. Friday Purchases II 

**Problem:** https://leetcode.com/problems/friday-purchases-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239444  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE fridays AS (
SELECT DATE('2023-11-03') AS purchase_date
UNION ALL SELECT DATE_ADD(purchase_date,INTERVAL 7 DAY) FROM fridays
WHERE purchase_date<'2023-11-24')
SELECT CEIL(DAYOFMONTH(f.purchase_date)/7) AS week_of_month, f.purchase_date,
COALESCE(SUM(p.amount_spend),0) AS total_amount
FROM fridays f LEFT JOIN Purchases p ON p.purchase_date=f.purchase_date
GROUP BY f.purchase_date ORDER BY week_of_month;
```

---

## 2995. Viewers Turned Streamers

**Problem:** https://leetcode.com/problems/viewers-turned-streamers/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239550  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (SELECT user_id,session_type,session_start,session_id,
ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY session_start,session_id) rn FROM Sessions),
first_viewers AS (SELECT user_id FROM ranked WHERE rn=1 AND session_type='Viewer')
SELECT s.user_id,COUNT(*) AS sessions_count FROM Sessions s
JOIN first_viewers f ON s.user_id=f.user_id WHERE s.session_type='Streamer'
GROUP BY s.user_id ORDER BY sessions_count DESC,s.user_id DESC;
```

---

## 3050. Pizza Toppings Cost Analysis

**Problem:** https://leetcode.com/problems/pizza-toppings-cost-analysis/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239652  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT CONCAT(a.topping_name,',',b.topping_name,',',c.topping_name) AS pizza,
ROUND(a.cost+b.cost+c.cost,2) AS total_cost
FROM Toppings a JOIN Toppings b ON a.topping_name<b.topping_name
JOIN Toppings c ON b.topping_name<c.topping_name
ORDER BY total_cost DESC,pizza ASC;
```

---

## 3051. Find Candidates for Data Scientist Position

**Problem:** https://leetcode.com/problems/find-candidates-for-data-scientist-position/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239751  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT candidate_id FROM Candidates
WHERE skill IN ('Python','Tableau','PostgreSQL')
GROUP BY candidate_id HAVING COUNT(DISTINCT skill)=3 ORDER BY candidate_id;
```

---

## 3052. Maximize Items

**Problem:** https://leetcode.com/problems/maximize-items/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239853  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH x AS (SELECT
SUM(CASE WHEN item_type='prime_eligible' THEN square_footage ELSE 0 END) p_area,
SUM(CASE WHEN item_type='prime_eligible' THEN 1 ELSE 0 END) p_count,
SUM(CASE WHEN item_type='not_prime' THEN square_footage ELSE 0 END) n_area,
SUM(CASE WHEN item_type='not_prime' THEN 1 ELSE 0 END) n_count FROM Inventory),
y AS (SELECT *,IF(p_area>0,FLOOR(500000/p_area),0) AS p_sets FROM x)
SELECT 'prime_eligible' AS item_type,p_count*p_sets AS item_count FROM y
UNION ALL
SELECT 'not_prime',n_count*IF(n_area>0,FLOOR((500000-p_area*p_sets)/n_area),0) FROM y
ORDER BY item_count DESC,item_type DESC;
```

---

## 3053. Classifying Triangles by Lengths

**Problem:** https://leetcode.com/problems/classifying-triangles-by-lengths/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database, Polygons  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187239937  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT CASE WHEN A+B<=C OR A+C<=B OR B+C<=A THEN 'Not A Triangle'
WHEN A=B AND B=C THEN 'Equilateral'
WHEN A=B OR B=C OR A=C THEN 'Isosceles' ELSE 'Scalene' END AS triangle_type
FROM Triangles;
```

---

## 3054. Binary Tree Nodes

**Problem:** https://leetcode.com/problems/binary-tree-nodes/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240036  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT t.N, CASE WHEN t.P IS NULL THEN 'Root'
WHEN EXISTS(SELECT 1 FROM Tree c WHERE c.P=t.N) THEN 'Inner'
ELSE 'Leaf' END AS Type FROM Tree t ORDER BY t.N;
```

---

## 3055. Top Percentile Fraud

**Problem:** https://leetcode.com/problems/top-percentile-fraud/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187251235  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT policy_id, state, fraud_score,
 RANK() OVER (PARTITION BY state ORDER BY fraud_score DESC) AS rk
 FROM Fraud
)
SELECT policy_id, state, fraud_score
FROM ranked WHERE rk=1
ORDER BY state, fraud_score DESC, policy_id;
```

---

## 3056. Snaps Analysis

**Problem:** https://leetcode.com/problems/snaps-analysis/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240209  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT g.age_bucket,
ROUND(100*SUM(CASE WHEN a.activity_type='send' THEN a.time_spent ELSE 0 END)/SUM(a.time_spent),2) AS send_perc,
ROUND(100*SUM(CASE WHEN a.activity_type='open' THEN a.time_spent ELSE 0 END)/SUM(a.time_spent),2) AS open_perc
FROM Activities a JOIN Age g ON a.user_id=g.user_id GROUP BY g.age_bucket;
```

---

## 3057. Employees Project Allocation

**Problem:** https://leetcode.com/problems/employees-project-allocation/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240293  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH team_avg AS (SELECT e.team,AVG(p.workload) avg_workload
FROM Project p JOIN Employees e ON e.employee_id=p.employee_id GROUP BY e.team)
SELECT p.employee_id,p.project_id,e.name AS employee_name,p.workload AS project_workload
FROM Project p JOIN Employees e ON p.employee_id=e.employee_id
JOIN team_avg a ON e.team=a.team WHERE p.workload>a.avg_workload
ORDER BY p.employee_id,p.project_id;
```

---

## 3058. Friends With No Mutual Friends

**Problem:** https://leetcode.com/problems/friends-with-no-mutual-friends/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240407  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH edges AS (SELECT user_id1 a,user_id2 b FROM Friends
UNION ALL SELECT user_id2,user_id1 FROM Friends)
SELECT f.user_id1,f.user_id2 FROM Friends f
WHERE NOT EXISTS (SELECT 1 FROM edges x JOIN edges y ON x.b=y.b
WHERE x.a=f.user_id1 AND y.a=f.user_id2)
ORDER BY f.user_id1,f.user_id2;
```

---

## 3059. Find All Unique Email Domains

**Problem:** https://leetcode.com/problems/find-all-unique-email-domains/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240559  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT SUBSTRING_INDEX(email,'@',-1) AS email_domain,COUNT(*) AS count
FROM Emails WHERE email LIKE '%.com'
GROUP BY email_domain ORDER BY email_domain;
```

---

## 3060. User Activities within Time Bounds

**Problem:** https://leetcode.com/problems/user-activities-within-time-bounds/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187251305  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH sessions_with_previous AS (
 SELECT user_id, session_type, session_start,
 LAG(session_end) OVER (
 PARTITION BY user_id, session_type ORDER BY session_end
 ) AS prev_end
 FROM Sessions
)
SELECT DISTINCT user_id
FROM sessions_with_previous
WHERE prev_end IS NOT NULL
  AND session_start <= DATE_ADD(prev_end, INTERVAL 12 HOUR)
ORDER BY user_id;
```

---

## 3061. Calculate Trapping Rain Water

**Problem:** https://leetcode.com/problems/calculate-trapping-rain-water/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240729  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH x AS (SELECT id,height,
MAX(height) OVER(ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) left_max,
MAX(height) OVER(ORDER BY id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) right_max
FROM Heights)
SELECT COALESCE(SUM(LEAST(left_max,right_max)-height),0) AS total_trapped_water FROM x;
```

---

## 3087. Find Trending Hashtags

**Problem:** https://leetcode.com/problems/find-trending-hashtags/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240807  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT REGEXP_SUBSTR(tweet,'#[A-Za-z0-9_]+') AS hashtag,
COUNT(*) AS hashtag_count FROM Tweets
WHERE tweet_date>='2024-02-01' AND tweet_date<'2024-03-01'
GROUP BY hashtag ORDER BY hashtag_count DESC,hashtag DESC LIMIT 3;
```

---

## 3089. Find Bursty Behavior

**Problem:** https://leetcode.com/problems/find-bursty-behavior/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240890  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH feb AS (SELECT * FROM Posts WHERE post_date BETWEEN '2024-02-01' AND '2024-02-28'), weekly AS (SELECT user_id,COUNT(*)/4 AS avg_weekly_posts FROM feb GROUP BY user_id), windows AS (SELECT a.user_id,a.post_id,COUNT(*) AS n FROM feb a JOIN feb b ON a.user_id=b.user_id AND b.post_date BETWEEN a.post_date AND DATE_ADD(a.post_date,INTERVAL 6 DAY) GROUP BY a.user_id,a.post_id) SELECT w.user_id,MAX(w.n) AS max_7day_posts, a.avg_weekly_posts FROM windows w JOIN weekly a USING(user_id) GROUP BY w.user_id,a.avg_weekly_posts HAVING MAX(w.n)>=2*a.avg_weekly_posts ORDER BY w.user_id;
```

---

## 3103. Find Trending Hashtags II 

**Problem:** https://leetcode.com/problems/find-trending-hashtags-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195507614  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE tags AS (
    SELECT tweet_id, tweet,
           REGEXP_SUBSTR(tweet, '#[[:alnum:]_]+', 1, 1) AS hashtag,
           1 AS occurrence
    FROM Tweets
    WHERE tweet_date >= '2024-02-01' AND tweet_date < '2024-03-01'
    UNION ALL
    SELECT tweet_id, tweet,
           REGEXP_SUBSTR(tweet, '#[[:alnum:]_]+', 1, occurrence + 1),
           occurrence + 1
    FROM tags WHERE hashtag IS NOT NULL
)
SELECT hashtag, COUNT(*) AS count
FROM tags WHERE hashtag IS NOT NULL
GROUP BY hashtag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
```

---

## 3118. Friday Purchase III 

**Problem:** https://leetcode.com/problems/friday-purchase-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195508017  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE fridays AS (
    SELECT DATE('2023-11-03') AS friday, 1 AS week_of_month
    UNION ALL
    SELECT DATE_ADD(friday, INTERVAL 7 DAY), week_of_month + 1
    FROM fridays WHERE friday < '2023-11-24'
), memberships AS (
    SELECT 'Premium' AS membership UNION ALL SELECT 'VIP'
)
SELECT f.week_of_month, m.membership,
       COALESCE(SUM(p.amount_spend), 0) AS total_amount
FROM fridays f CROSS JOIN memberships m
LEFT JOIN Users u ON u.membership = m.membership
LEFT JOIN Purchases p ON p.user_id = u.user_id AND p.purchase_date = f.friday
GROUP BY f.week_of_month, m.membership
ORDER BY f.week_of_month, m.membership;
```

---

## 3124. Find Longest Calls

**Problem:** https://leetcode.com/problems/find-longest-calls/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195611898  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below


WITH RankedCalls AS (
    SELECT
        c.first_name,
        ca.type,
        ca.duration,
        ROW_NUMBER() OVER (
            PARTITION BY ca.type
            ORDER BY ca.duration DESC, c.first_name DESC
        ) AS rn
    FROM Calls ca
    JOIN Contacts c
        ON ca.contact_id = c.id
)
SELECT
    first_name,
    type,
    CAST(SEC_TO_TIME(duration) AS CHAR) AS duration_formatted
FROM RankedCalls
WHERE rn <= 3
ORDER BY
    type DESC,
    duration DESC,
    first_name DESC;
```

---

## 3126. Server Utilization Time

**Problem:** https://leetcode.com/problems/server-utilization-time/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195509558  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH sessions AS (
    SELECT server_id, status_time, session_status,
           LEAD(status_time) OVER (
               PARTITION BY server_id ORDER BY status_time
           ) AS next_time
    FROM Servers
)
SELECT FLOOR(SUM(TIMESTAMPDIFF(SECOND, status_time, next_time)) / 86400)
       AS total_uptime_days
FROM sessions WHERE session_status = 'start';
```

---

## 3140. Consecutive Available Seats II

**Problem:** https://leetcode.com/problems/consecutive-available-seats-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187240986  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH t AS (SELECT seat_id, seat_id-ROW_NUMBER() OVER(ORDER BY seat_id) AS grp FROM Cinema WHERE free=1), g AS (SELECT MIN(seat_id) AS first_seat_id,MAX(seat_id) AS last_seat_id,COUNT(*) AS consecutive_seats_len FROM t GROUP BY grp) SELECT first_seat_id,last_seat_id,consecutive_seats_len FROM g WHERE consecutive_seats_len=(SELECT MAX(consecutive_seats_len) FROM g) ORDER BY first_seat_id;
```

---

## 3150. Invalid Tweets II

**Problem:** https://leetcode.com/problems/invalid-tweets-ii/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187247041  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content) > 140 OR LENGTH(content)-LENGTH(REPLACE(content,'@','')) > 3 OR LENGTH(content)-LENGTH(REPLACE(content,'#','')) > 3 ORDER BY tweet_id;
```

---

## 3156. Employee Task Duration and Concurrent Tasks

**Problem:** https://leetcode.com/problems/employee-task-duration-and-concurrent-tasks/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195509696  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ordered AS (
    SELECT employee_id, start_time, end_time,
           MAX(end_time) OVER (PARTITION BY employee_id ORDER BY start_time, end_time
               ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS prev_end
    FROM Tasks
), islands AS (
    SELECT *, SUM(CASE WHEN prev_end IS NULL OR start_time > prev_end THEN 1 ELSE 0 END)
      OVER (PARTITION BY employee_id ORDER BY start_time, end_time) AS grp
    FROM ordered
), merged AS (
    SELECT employee_id, grp, MIN(start_time) AS st, MAX(end_time) AS en
    FROM islands GROUP BY employee_id, grp
), hours AS (
    SELECT employee_id, FLOOR(SUM(TIMESTAMPDIFF(SECOND, st, en)) / 3600) AS total_task_hours
    FROM merged GROUP BY employee_id
), events AS (
    SELECT employee_id, start_time AS tm, 1 AS delta FROM Tasks
    UNION ALL
    SELECT employee_id, end_time AS tm, -1 AS delta FROM Tasks
), counts AS (
    SELECT employee_id, SUM(delta) OVER (
        PARTITION BY employee_id ORDER BY tm, delta
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS active
    FROM events
)
SELECT h.employee_id, h.total_task_hours, MAX(c.active) AS max_concurrent_tasks
FROM hours h JOIN counts c USING (employee_id)
GROUP BY h.employee_id, h.total_task_hours
ORDER BY h.employee_id;
```

---

## 3166. Calculate Parking Fees and Duration

**Problem:** https://leetcode.com/problems/calculate-parking-fees-and-duration/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612032  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH CarStats AS (
    SELECT
        car_id,
        SUM(fee_paid) AS total_fee_paid,
        SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time))
            AS total_seconds
    FROM ParkingTransactions
    GROUP BY car_id
),
LotStats AS (
    SELECT
        car_id,
        lot_id,
        SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time))
            AS total_seconds
    FROM ParkingTransactions
    GROUP BY car_id, lot_id
),
RankedLots AS (
    SELECT
        car_id,
        lot_id,
        ROW_NUMBER() OVER (
            PARTITION BY car_id
            ORDER BY total_seconds DESC, lot_id ASC
        ) AS rn
    FROM LotStats
)
SELECT
    c.car_id,
    c.total_fee_paid,
    ROUND(c.total_fee_paid * 3600.0 / c.total_seconds, 2)
        AS avg_hourly_fee,
    r.lot_id AS most_time_lot
FROM CarStats c
JOIN RankedLots r
    ON c.car_id = r.car_id
WHERE r.rn = 1
ORDER BY c.car_id;
```

---

## 3172. Second Day Verification

**Problem:** https://leetcode.com/problems/second-day-verification/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187241894  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT e.user_id FROM Emails e JOIN texts t ON e.email_id=t.email_id WHERE DATEDIFF(t.action_date,e.signup_date)=1 AND t.signup_action='Verified' ORDER BY e.user_id;
```

---

## 3182. Find Top Scoring Students

**Problem:** https://leetcode.com/problems/find-top-scoring-students/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187247117  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT student_id FROM students JOIN courses USING (major) LEFT JOIN enrollments USING (student_id,course_id) GROUP BY student_id HAVING SUM(grade='A')=COUNT(major) ORDER BY student_id;
```

---

## 3188. Find Top Scoring Students II

**Problem:** https://leetcode.com/problems/find-top-scoring-students-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612153  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH GPAStats AS (
    SELECT
        student_id,
        AVG(GPA) AS avg_gpa
    FROM enrollments
    GROUP BY student_id
    HAVING AVG(GPA) >= 2.5
)
SELECT
    s.student_id
FROM students s
JOIN GPAStats g
    ON s.student_id = g.student_id
JOIN courses c
    ON s.major = c.major
LEFT JOIN enrollments e
    ON s.student_id = e.student_id
    AND c.course_id = e.course_id
GROUP BY s.student_id
HAVING
    COUNT(DISTINCT CASE
        WHEN c.mandatory = 'Yes'
             AND e.grade = 'A'
        THEN c.course_id
    END) =
    COUNT(DISTINCT CASE
        WHEN c.mandatory = 'Yes'
        THEN c.course_id
    END)
    AND
    COUNT(DISTINCT CASE
        WHEN c.mandatory = 'No'
             AND e.grade IN ('A', 'B')
        THEN c.course_id
    END) >= 2
ORDER BY s.student_id;
```

---

## 3198. Find Cities in Each State

**Problem:** https://leetcode.com/problems/find-cities-in-each-state/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242041  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT state, GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') AS cities FROM cities GROUP BY state ORDER BY state;
```

---

## 3204. Bitwise User Permissions Analysis

**Problem:** https://leetcode.com/problems/bitwise-user-permissions-analysis/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242107  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT BIT_AND(permissions) AS common_perms, BIT_OR(permissions) AS any_perms FROM user_permissions;
```

---

## 3214. Year on Year Growth Rate

**Problem:** https://leetcode.com/problems/year-on-year-growth-rate/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195511584  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH yearly AS (
    SELECT YEAR(transaction_date) AS year, product_id,
           SUM(spend) AS curr_year_spend
    FROM user_transactions GROUP BY YEAR(transaction_date), product_id
), previous AS (
    SELECT *, LAG(curr_year_spend) OVER (
        PARTITION BY product_id ORDER BY year
    ) AS prev_year_spend
    FROM yearly
)
SELECT year, product_id, curr_year_spend, prev_year_spend,
       ROUND(100 * (curr_year_spend - prev_year_spend) /
             NULLIF(prev_year_spend, 0), 2) AS yoy_rate
FROM previous ORDER BY product_id, year;
```

---

## 3220. Odd and Even Transactions

**Problem:** https://leetcode.com/problems/odd-and-even-transactions/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242196  
**Language:** mysql

### Description

Table:  transactions 
 
```text
+------------------+------+
| Column Name      | Type | 
+------------------+------+
| transaction_id   | int  |
| amount           | int  |
| transaction_date | date |
+------------------+------+
The transactions_id column uniquely identifies each row in this table.
Each row of this table contains the transaction id, amount and transaction date.
```
 
 
 Write a solution to find the  sum of amounts  for  odd  and  even  transactions for each day. If there are no odd or even transactions for a specific date, display as  0 . 
 
 Return  the result table ordered by   transaction_date   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 transactions  table: 
 
```text
+----------------+--------+------------------+
| transaction_id | amount | transaction_date |
+----------------+--------+------------------+
| 1              | 150    | 2024-07-01       |
| 2              | 200    | 2024-07-01       |
| 3              | 75     | 2024-07-01       |
| 4              | 300    | 2024-07-02       |
| 5              | 50     | 2024-07-02       |
| 6              | 120    | 2024-07-03       |
+----------------+--------+------------------+
```
 
 
 Output: 
 
```text
+------------------+---------+----------+
| transaction_date | odd_sum | even_sum |
+------------------+---------+----------+
| 2024-07-01       | 75      | 350      |
| 2024-07-02       | 0       | 350      |
| 2024-07-03       | 0       | 120      |
+------------------+---------+----------+
```
 
 
 Explanation: 
 
 
 For transaction dates:
	 
 
 2024-07-01:
		 
 
 Sum of amounts for odd transactions: 75 
 
 Sum of amounts for even transactions: 150 + 200 = 350 
 
 
 
 2024-07-02:
		 
 
 Sum of amounts for odd transactions: 0 
 
 Sum of amounts for even transactions: 300 + 50 = 350 
 
 
 
 2024-07-03:
		 
 
 Sum of amounts for odd transactions: 0 
 
 Sum of amounts for even transactions: 120 
 
 
 
 
 
 
 Note:  The output table is ordered by  transaction_date  in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT transaction_date, SUM(IF(amount%2=1,amount,0)) AS odd_sum, SUM(IF(amount%2=0,amount,0)) AS even_sum FROM transactions GROUP BY transaction_date ORDER BY transaction_date;
```

---

## 3230. Customer Purchasing Behavior Analysis

**Problem:** https://leetcode.com/problems/customer-purchasing-behavior-analysis/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195511713  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH joined AS (
    SELECT t.*, p.category FROM Transactions t
    JOIN Products p ON p.product_id = t.product_id
), summary AS (
    SELECT customer_id, SUM(amount) AS spent, COUNT(*) AS transactions,
           COUNT(DISTINCT category) AS unique_categories, AVG(amount) AS avg_amount
    FROM joined GROUP BY customer_id
), categories AS (
    SELECT customer_id, category, COUNT(*) AS frequency,
           MAX(transaction_date) AS latest_date
    FROM joined GROUP BY customer_id, category
), ranked AS (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY customer_id ORDER BY frequency DESC, latest_date DESC, category
    ) AS rn FROM categories
)
SELECT s.customer_id, ROUND(s.spent, 2) AS total_amount,
       s.transactions AS transaction_count, s.unique_categories,
       ROUND(s.avg_amount, 2) AS avg_transaction_amount,
       r.category AS top_category,
       ROUND(s.transactions * 10 + s.spent / 100, 2) AS loyalty_score
FROM summary s JOIN ranked r ON r.customer_id = s.customer_id AND r.rn = 1
ORDER BY loyalty_score DESC, s.customer_id;
```

---

## 3236. CEO Subordinate Hierarchy

**Problem:** https://leetcode.com/problems/ceo-subordinate-hierarchy/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195511833  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE hierarchy AS (
    SELECT employee_id, employee_name, manager_id, salary,
           0 AS hierarchy_level, salary AS ceo_salary
    FROM Employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.employee_name, e.manager_id, e.salary,
           h.hierarchy_level + 1, h.ceo_salary
    FROM Employees e JOIN hierarchy h ON e.manager_id = h.employee_id
)
SELECT employee_id AS subordinate_id,
       employee_name AS subordinate_name,
       hierarchy_level, salary - ceo_salary AS salary_difference
FROM hierarchy WHERE hierarchy_level > 0
ORDER BY hierarchy_level, subordinate_id;
```

---

## 3246. Premier League Table Ranking

**Problem:** https://leetcode.com/problems/premier-league-table-ranking/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242285  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT team_id,team_name,wins*3+draws AS points,RANK() OVER(ORDER BY wins*3+draws DESC) AS position FROM TeamStats ORDER BY points DESC,team_name;
```

---

## 3252. Premier League Table Ranking II

**Problem:** https://leetcode.com/problems/premier-league-table-ranking-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612313  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH RankedTeams AS (
    SELECT
        team_name,
        wins * 3 + draws AS points,
        RANK() OVER (
            ORDER BY wins * 3 + draws DESC
        ) AS position,
        COUNT(*) OVER () AS total_teams
    FROM TeamStats
)
SELECT
    team_name,
    points,
    position,
    CASE
        WHEN position <= CEIL(total_teams / 3.0)
            THEN 'Tier 1'
        WHEN position <= CEIL(2 * total_teams / 3.0)
            THEN 'Tier 2'
        ELSE 'Tier 3'
    END AS tier
FROM RankedTeams
ORDER BY points DESC, team_name ASC;
```

---

## 3262. Find Overlapping Shifts

**Problem:** https://leetcode.com/problems/find-overlapping-shifts/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242370  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT a.employee_id, COUNT(*) AS overlapping_shifts
FROM EmployeeShifts a JOIN EmployeeShifts b
 ON a.employee_id=b.employee_id AND a.start_time<b.start_time
 AND a.end_time>b.start_time
GROUP BY a.employee_id ORDER BY a.employee_id;
```

---

## 3268. Find Overlapping Shifts II

**Problem:** https://leetcode.com/problems/find-overlapping-shifts-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242455  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH endpoints AS (
 SELECT employee_id,start_time AS t FROM EmployeeShifts
 UNION SELECT employee_id,end_time FROM EmployeeShifts
), segments AS (
 SELECT employee_id,t AS start_time,
 LEAD(t) OVER(PARTITION BY employee_id ORDER BY t) AS end_time
 FROM endpoints
), coverage AS (
 SELECT s.employee_id,s.start_time,s.end_time,COUNT(*) AS concurrent_count
 FROM segments s JOIN EmployeeShifts e ON e.employee_id=s.employee_id
 AND e.start_time<=s.start_time AND e.end_time>=s.end_time
 WHERE s.end_time IS NOT NULL
 GROUP BY s.employee_id,s.start_time,s.end_time
)
SELECT employee_id,MAX(concurrent_count) AS max_overlapping_shifts,
 SUM(concurrent_count*(concurrent_count-1)/2 *
 TIMESTAMPDIFF(MINUTE,start_time,end_time)) AS total_overlap_duration
FROM coverage GROUP BY employee_id ORDER BY employee_id;
```

---

## 3278. Find Candidates for Data Scientist Position II

**Problem:** https://leetcode.com/problems/find-candidates-for-data-scientist-position-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242547  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH req AS (SELECT project_id,COUNT(*) AS n FROM Projects GROUP BY project_id),
 matched AS (
 SELECT p.project_id,c.candidate_id,COUNT(*) AS n,
 100+SUM(CASE WHEN c.proficiency>p.importance THEN 10
 WHEN c.proficiency<p.importance THEN -5 ELSE 0 END) AS score
 FROM Projects p JOIN Candidates c ON c.skill=p.skill
 GROUP BY p.project_id,c.candidate_id
), ranked AS (
 SELECT m.project_id,m.candidate_id,m.score,
 ROW_NUMBER() OVER(PARTITION BY m.project_id ORDER BY m.score DESC,m.candidate_id) AS rn
 FROM matched m JOIN req r ON r.project_id=m.project_id AND r.n=m.n
)
SELECT project_id,candidate_id,score FROM ranked WHERE rn=1 ORDER BY project_id;
```

---

## 3293. Calculate Product Final Price

**Problem:** https://leetcode.com/problems/calculate-product-final-price/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242637  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT p.product_id,p.price*(100-COALESCE(d.discount,0))/100 AS final_price,p.category
FROM Products p LEFT JOIN Discounts d ON p.category=d.category
ORDER BY p.product_id;
```

---

## 3308. Find Top Performing Driver

**Problem:** https://leetcode.com/problems/find-top-performing-driver/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612509  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH DriverStats AS (
    SELECT
        v.fuel_type,
        d.driver_id,
        ROUND(AVG(t.rating), 2) AS rating,
        SUM(t.distance) AS distance,
        d.accidents
    FROM Drivers d
    JOIN Vehicles v
        ON d.driver_id = v.driver_id
    JOIN Trips t
        ON v.vehicle_id = t.vehicle_id
    GROUP BY
        v.fuel_type,
        d.driver_id,
        d.accidents
),
RankedDrivers AS (
    SELECT
        *,
        RANK() OVER (
            PARTITION BY fuel_type
            ORDER BY
                rating DESC,
                distance DESC,
                accidents ASC
        ) AS rn
    FROM DriverStats
)
SELECT
    fuel_type,
    driver_id,
    rating,
    distance
FROM RankedDrivers
WHERE rn = 1
ORDER BY fuel_type ASC;
```

---

## 3322. Premier League Table Ranking III

**Problem:** https://leetcode.com/problems/premier-league-table-ranking-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195513665  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH scores AS (
 SELECT season_id, team_id, team_name, wins * 3 + draws AS points,
        goals_for - goals_against AS goal_difference
 FROM SeasonStats
)
SELECT season_id, team_id, team_name, points, goal_difference,
       ROW_NUMBER() OVER (PARTITION BY season_id ORDER BY points DESC, goal_difference DESC, team_name) AS position
FROM scores
ORDER BY season_id, position, team_name;
```

---

## 3328. Find Cities in Each State II

**Problem:** https://leetcode.com/problems/find-cities-in-each-state-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242735  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT state,GROUP_CONCAT(city ORDER BY city SEPARATOR ', ') AS cities,
 SUM(LEFT(city,1)=LEFT(state,1)) AS matching_letter_count
FROM cities GROUP BY state
HAVING COUNT(*)>=3 AND matching_letter_count>=1
ORDER BY matching_letter_count DESC,state;
```

---

## 3338. Second Highest Salary II

**Problem:** https://leetcode.com/problems/second-highest-salary-ii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242844  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT emp_id,dept,DENSE_RANK() OVER(PARTITION BY dept ORDER BY salary DESC) AS rk
 FROM employees
)
SELECT emp_id,dept FROM ranked WHERE rk=2 ORDER BY emp_id;
```

---

## 3358. Books with NULL Ratings

**Problem:** https://leetcode.com/problems/books-with-null-ratings/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187242926  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT book_id,title,author,published_year
FROM books WHERE rating IS NULL ORDER BY book_id;
```

---

## 3368. First Letter Capitalization

**Problem:** https://leetcode.com/problems/first-letter-capitalization/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612706  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH RECURSIVE Words AS (
    SELECT
        content_id,
        content_text,
        SUBSTRING_INDEX(content_text, ' ', 1) AS word,
        SUBSTRING(
            content_text,
            LENGTH(SUBSTRING_INDEX(content_text, ' ', 1)) + 2
        ) AS remaining_text,
        1 AS pos
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        SUBSTRING_INDEX(remaining_text, ' ', 1),
        SUBSTRING(
            remaining_text,
            LENGTH(SUBSTRING_INDEX(remaining_text, ' ', 1)) + 2
        ),
        pos + 1
    FROM Words
    WHERE remaining_text != ''
)
SELECT
    content_id,
    content_text AS original_text,
    GROUP_CONCAT(
        CONCAT(
            UPPER(LEFT(word, 1)),
            LOWER(SUBSTRING(word, 2))
        )
        ORDER BY pos SEPARATOR ' '
    ) AS converted_text
FROM Words
GROUP BY content_id, content_text;
```

---

## 3374. First Letter Capitalization II

**Problem:** https://leetcode.com/problems/first-letter-capitalization-ii/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195618310  
**Language:** mysql

### Description

Table:  user_content 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| content_id   | int     |
| content_text | varchar |
+--------------+---------+
content_id is the unique key for this table.
Each row contains a unique ID and the corresponding text content.
```
 
 
 A  word  is a maximal non-empty sequence of characters that does not contain a space. 
 
 Write a solution to transform the text in the  content_text  column by applying the following rules to each word: 
 
 
 If the word starts with a character that is  not  an English letter, leave the entire word  unchanged . 
 
 Otherwise, if the word consists of two or more non-empty parts of English letters connected by hyphens  - , convert the  first letter of each part  to uppercase and the  remaining letters of each part  to lowercase. For example,  top-rated  becomes  Top-Rated  and  FR-ONT-end  becomes  Fr-Ont-End . 
 
 Otherwise, convert the  first letter  of the word to uppercase and all  remaining English letters  to lowercase. Any special characters remain unchanged. 
 
 
 All other  formatting  and  spacing  must remain  unchanged . 
 
 Return  the result table that includes both the original  content_text  and the modified text following the above rules . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 user_content table: 
 
```text
+------------+---------------------------------+
| content_id | content_text                    |
+------------+---------------------------------+
| 1          | hello world of SQL              |
| 2          | the QUICK-brown fox             |
| 3          | modern-day DATA science         |
| 4          | web-based FRONT-end development |
+------------+---------------------------------+
```
 
 
 Output: 
 
```text
+------------+---------------------------------+---------------------------------+
| content_id | original_text                   | converted_text                  |
+------------+---------------------------------+---------------------------------+
| 1          | hello world of SQL              | Hello World Of Sql              |
| 2          | the QUICK-brown fox             | The Quick-Brown Fox             |
| 3          | modern-day DATA science         | Modern-Day Data Science         |
| 4          | web-based FRONT-end development | Web-Based Front-End Development |
+------------+---------------------------------+---------------------------------+
```
 
 
 Explanation: 
 
 
 For content_id = 1:
	 
 
 Each word's first letter is capitalized: "Hello World Of Sql". 
 
 
 
 For content_id = 2:
	 
 
 The hyphenated word "QUICK-brown" becomes "Quick-Brown". 
 
 Other words follow the normal capitalization rules. 
 
 
 
 For content_id = 3:
	 
 
 The hyphenated word "modern-day" becomes "Modern-Day". 
 
 "DATA" is converted to "Data". 
 
 
 
 For content_id = 4:
	 
 
 "web-based" becomes "Web-Based". 
 
 "FRONT-end" becomes "Front-End". 
 
 
 
 
 
   
 
 Constraints: 
 
 
 content_text  contains only English letters, spaces, and the characters  \ ,  @ ,  - ,  / ,  ^ , and  , .

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql

WITH RECURSIVE chars AS (
    SELECT
        content_id,
        content_text,
        1 AS pos
    FROM user_content
    WHERE CHAR_LENGTH(content_text) > 0

    UNION ALL

    SELECT
        content_id,
        content_text,
        pos + 1
    FROM chars
    WHERE pos < CHAR_LENGTH(content_text)
),
parts AS (
    SELECT
        content_id,
        pos,
        SUBSTRING(content_text, pos, 1) AS ch,
        SUBSTRING(content_text, pos - 1, 1) AS prev_ch,
        SUBSTRING_INDEX(
            SUBSTRING_INDEX(content_text, ' ', 
                1 + CHAR_LENGTH(LEFT(content_text, pos - 1))
                - CHAR_LENGTH(REPLACE(LEFT(content_text, pos - 1), ' ', ''))
            ),
            ' ', -1
        ) AS word
    FROM chars
),
converted AS (
    SELECT
        content_id,
        pos,
        CASE
            WHEN LEFT(word, 1) NOT REGEXP '^[A-Za-z]$'
                THEN ch
            WHEN ch REGEXP '^[A-Za-z]$'
                 AND (
                     pos = 1
                     OR prev_ch = ' '
                     OR (
                         prev_ch = '-'
                         AND word REGEXP
                             '^[A-Za-z]+(-[A-Za-z]+)+$'
                     )
                 )
                THEN UPPER(ch)
            WHEN ch REGEXP '^[A-Za-z]$'
                THEN LOWER(ch)
            ELSE ch
        END AS new_ch
    FROM parts
)
SELECT
    u.content_id,
    u.content_text AS original_text,
    COALESCE(
        GROUP_CONCAT(c.new_ch ORDER BY c.pos SEPARATOR ''),
        ''
    ) AS converted_text
FROM user_content u
LEFT JOIN converted c
    ON u.content_id = c.content_id
GROUP BY u.content_id, u.content_text
ORDER BY u.content_id;
```

---

## 3384. Team Dominance by Pass Success

**Problem:** https://leetcode.com/problems/team-dominance-by-pass-success/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187243012  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT a.team_name,IF(p.time_stamp<='45:00',1,2) AS half_number,
 SUM(IF(a.team_name=b.team_name,1,-1)) AS dominance
FROM Passes p JOIN Teams a ON a.player_id=p.pass_from
 JOIN Teams b ON b.player_id=p.pass_to
GROUP BY a.team_name,half_number ORDER BY a.team_name,half_number;
```

---

## 3390. Longest Team Pass Streak

**Problem:** https://leetcode.com/problems/longest-team-pass-streak/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187251378  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH passes_with_teams AS (
 SELECT f.team_name AS team_name, p.time_stamp,
        (f.team_name=t.team_name) AS successful
 FROM Passes p
 JOIN Teams f ON f.player_id=p.pass_from
 JOIN Teams t ON t.player_id=p.pass_to
), grouped AS (
 SELECT team_name, successful,
 SUM(successful=0) OVER (
 PARTITION BY team_name ORDER BY time_stamp
 ROWS UNBOUNDED PRECEDING
 ) AS grp
 FROM passes_with_teams
), streaks AS (
 SELECT team_name, grp, COUNT(*) AS streak
 FROM grouped WHERE successful=1
 GROUP BY team_name, grp
)
SELECT team_name, MAX(streak) AS longest_streak
FROM streaks GROUP BY team_name ORDER BY team_name;
```

---

## 3401. Find Circular Gift Exchange Chains

**Problem:** https://leetcode.com/problems/find-circular-gift-exchange-chains/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187243183  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE walk AS (
 SELECT giver_id AS start_id,receiver_id,gift_value AS total_gift_value,
 1 AS chain_length,CAST(CONCAT(',',giver_id,',') AS CHAR(10000)) AS visited
 FROM SecretSanta
 UNION ALL
 SELECT w.start_id,s.receiver_id,w.total_gift_value+s.gift_value,
 w.chain_length+1,CONCAT(w.visited,s.giver_id,',')
 FROM walk w JOIN SecretSanta s ON s.giver_id=w.receiver_id
 WHERE w.receiver_id<>w.start_id AND LOCATE(CONCAT(',',s.giver_id,','),w.visited)=0
), cycles AS (
 SELECT start_id,chain_length,total_gift_value
 FROM walk WHERE receiver_id=start_id
), distinct_cycles AS (
 SELECT chain_length,total_gift_value FROM cycles GROUP BY chain_length,total_gift_value
)
SELECT ROW_NUMBER() OVER(ORDER BY chain_length DESC,total_gift_value DESC) AS chain_id,
 chain_length,total_gift_value FROM distinct_cycles
ORDER BY chain_length DESC,total_gift_value DESC;
```

---

## 3415. Find Products with Three Consecutive Digits 

**Problem:** https://leetcode.com/problems/find-products-with-three-consecutive-digits/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195514625  
**Language:** mysql

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT product_id, name FROM Products WHERE REGEXP_LIKE(name, '(^|[^0-9])[0-9]{3}([^0-9]|$)') ORDER BY product_id;
```

---

## 3421. Find Students Who Improved

**Problem:** https://leetcode.com/problems/find-students-who-improved/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187243249  
**Language:** mysql

### Description

Table:  Scores 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student_id  | int     |
| subject     | varchar |
| score       | int     |
| exam_date   | varchar |
+-------------+---------+
(student_id, subject, exam_date) is the primary key for this table.
Each row contains information about a student's score in a specific subject on a particular exam date. score is between 0 and 100 (inclusive).
```
 
 
 Write a solution to find the  students who have shown improvement . A student is considered to have shown improvement if they meet  both  of these conditions: 
 
 
 Have taken exams in the  same subject  on at least two different dates 
 
 Their  latest score  in that subject is  higher  than their  first score 
 
 
 Return  the result table   ordered by   student_id,   subject   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 Scores table: 
 
```text
+------------+----------+-------+------------+
| student_id | subject  | score | exam_date  |
+------------+----------+-------+------------+
| 101        | Math     | 70    | 2023-01-15 |
| 101        | Math     | 85    | 2023-02-15 |
| 101        | Physics  | 65    | 2023-01-15 |
| 101        | Physics  | 60    | 2023-02-15 |
| 102        | Math     | 80    | 2023-01-15 |
| 102        | Math     | 85    | 2023-02-15 |
| 103        | Math     | 90    | 2023-01-15 |
| 104        | Physics  | 75    | 2023-01-15 |
| 104        | Physics  | 85    | 2023-02-15 |
+------------+----------+-------+------------+
```
 
 
 Output: 
 
```text
+------------+----------+-------------+--------------+
| student_id | subject  | first_score | latest_score |
+------------+----------+-------------+--------------+
| 101        | Math     | 70          | 85           |
| 102        | Math     | 80          | 85           |
| 104        | Physics  | 75          | 85           |
+------------+----------+-------------+--------------+
```
 
 
 Explanation: 
 
 
 Student 101 in Math: Improved from 70 to 85 
 
 Student 101 in Physics: No improvement (dropped from 65 to 60) 
 
 Student 102 in Math: Improved from 80 to 85 
 
 Student 103 in Math: Only one exam, not eligible 
 
 Student 104 in Physics: Improved from 75 to 85 
 
 
 Result table is ordered by student_id, subject.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH ranked AS (
 SELECT student_id,subject,score,
 ROW_NUMBER() OVER(PARTITION BY student_id,subject ORDER BY exam_date) AS first_rn,
 ROW_NUMBER() OVER(PARTITION BY student_id,subject ORDER BY exam_date DESC) AS last_rn
 FROM Scores
), agg AS (
 SELECT student_id,subject,MAX(IF(first_rn=1,score,NULL)) AS first_score,
 MAX(IF(last_rn=1,score,NULL)) AS latest_score,COUNT(*) AS exams
 FROM ranked GROUP BY student_id,subject
)
SELECT student_id,subject,first_score,latest_score
FROM agg WHERE exams>=2 AND latest_score>first_score
ORDER BY student_id,subject;
```

---

## 3436. Find Valid Emails

**Problem:** https://leetcode.com/problems/find-valid-emails/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612800  
**Language:** mysql

### Description

Table:  Users 
 
```text
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| user_id         | int     |
| email           | varchar |
+-----------------+---------+
(user_id) is the unique key for this table.
Each row contains a user's unique ID and email address.
```
 
 
 Write a solution to find all the  valid email addresses . A valid email address meets the following criteria: 
 
 
 It contains exactly one  @  symbol. 
 
 It ends with  .com . 
 
 The part before the  @  symbol contains only  alphanumeric  characters and  underscores . 
 
 The part after the  @  symbol and before  .com  contains a domain name  that contains only letters . 
 
 
 Return  the result table ordered by   user_id   in   ascending  order . 
 
   
 
 Example: 
 
 
 Input: 
 
 Users table: 
 
```text
+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+
```
 
 
 Output: 
 
```text
+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+
```
 
 
 Explanation: 
 
 
 alice@example.com  is valid because it contains one  @ , alice is alphanumeric, and example.com starts with a letter and ends with .com. 
 
 bob_at_example.com  is invalid because it contains an underscore instead of an  @ . 
 
 charlie@example.net  is invalid because the domain does not end with  .com . 
 
 david@domain.com  is valid because it meets all criteria. 
 
 eve@invalid  is invalid because the domain does not end with  .com . 
 
 
 Result table is ordered by user_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    user_id,
    email
FROM Users
WHERE REGEXP_LIKE(
    email,
    '^[A-Za-z0-9_]+@[A-Za-z]+[.]com$',
    'c'
)
ORDER BY user_id ASC;
```

---

## 3451. Find Invalid IP Addresses

**Problem:** https://leetcode.com/problems/find-invalid-ip-addresses/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187251561  
**Language:** mysql

### Description

Table:   logs 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| log_id      | int     |
| ip          | varchar |
| status_code | int     |
+-------------+---------+
log_id is the unique key for this table.
Each row contains server access log information including IP address and HTTP status code.
```
 
 
 Write a solution to find  invalid IP addresses . Each octet in an IP address contains between  1  and  3  digits. An IPv4 address is invalid if it meets any of these conditions: 
 
 
 Contains a number  greater than   255  in any octet. 
 
 Has  leading zeros  in any octet (for example,  01.02.03.04 ). 
 
 Has  fewer or more  than  4  octets. 
 
 
 Return  the result table  ordered by   invalid_count ,  ip   in  descending  order respectively .  
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 logs table: 
 
```text
+--------+---------------+-------------+
| log_id | ip            | status_code | 
+--------+---------------+-------------+
| 1      | 192.168.1.1   | 200         | 
| 2      | 256.1.2.3     | 404         | 
| 3      | 192.168.001.1 | 200         | 
| 4      | 192.168.1.1   | 200         | 
| 5      | 192.168.1     | 500         | 
| 6      | 256.1.2.3     | 404         | 
| 7      | 192.168.001.1 | 200         | 
+--------+---------------+-------------+
```
 
 
 Output: 
 
```text
+---------------+--------------+
| ip            | invalid_count|
+---------------+--------------+
| 256.1.2.3     | 2            |
| 192.168.001.1 | 2            |
| 192.168.1     | 1            |
+---------------+--------------+
```
 
 
 Explanation: 
 
 
 256.1.2.3 is invalid because 256 > 255 
 
 192.168.001.1 is invalid because of leading zeros 
 
 192.168.1 is invalid because it has only 3 octets 
 
 
 The output table is ordered by invalid_count, ip in descending order respectively.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT ip, COUNT(*) AS invalid_count
FROM logs
WHERE NOT REGEXP_LIKE(ip,
 '^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)[.](25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)[.](25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)[.](25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)$', 'c')
GROUP BY ip ORDER BY invalid_count DESC, ip DESC;
```

---

## 3465. Find Products with Valid Serial Numbers

**Problem:** https://leetcode.com/problems/find-products-with-valid-serial-numbers/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187243537  
**Language:** mysql

### Description

Table:  products 
 
```text
+--------------+------------+
| Column Name  | Type       |
+--------------+------------+
| product_id   | int        |
| product_name | varchar    |
| description  | varchar    |
+--------------+------------+
(product_id) is the unique key for this table.
Each row in the table represents a product with its unique ID, name, and description.
```
 
 
 Write a solution to find all products whose description  contains a valid serial number  pattern. A valid serial number follows these rules: 
 
 
 It starts with the letters  SN  (case-sensitive). 
 
 Followed by exactly  4  digits. 
 
 It must have a hyphen (-)  followed by exactly   4  digits. 
 
 The serial number must be within the description (it may not necessarily start at the beginning). 
 
 
 Return  the result table ordered by   product_id   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 products table: 
 
```text
+------------+--------------+------------------------------------------------------+
| product_id | product_name | description                                          |
+------------+--------------+------------------------------------------------------+
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 3          | Widget C     | Product SN1234-56789 is available now                |
| 4          | Widget D     | No serial number here                                |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
+------------+--------------+------------------------------------------------------+
```
 
 
 Output: 
 
```text
+------------+--------------+------------------------------------------------------+
| product_id | product_name | description                                          |
+------------+--------------+------------------------------------------------------+
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
+------------+--------------+------------------------------------------------------+
```
 
 
 Explanation: 
 
 
 Product 1:  Valid serial number SN1234-5678 
 
 Product 2:  Valid serial number SN9876-1234 
 
 Product 3:  Invalid serial number SN1234-56789 (contains 5 digits after the hyphen) 
 
 Product 4:  No serial number in the description 
 
 Product 5:  Valid serial number SN4321-8765 
 
 
 The result table is ordered by product_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT product_id,product_name,description FROM products
WHERE REGEXP_LIKE(description,'(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}([^A-Za-z0-9]|$)','c')
ORDER BY product_id;
```

---

## 3475. DNA Pattern Recognition 

**Problem:** https://leetcode.com/problems/dna-pattern-recognition/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187243607  
**Language:** mysql

### Description

Table:  Samples 
 
```text
+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| sample_id      | int     |
| dna_sequence   | varchar |
| species        | varchar |
+----------------+---------+
sample_id is the unique key for this table.
Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.
```
 
 
 Biologists are studying basic patterns in DNA sequences. Write a solution to identify  sample_id  with the following patterns: 
 
 
 Sequences that  start  with  ATG  (a common  start codon ) 
 
 Sequences that  end  with either  TAA ,  TAG , or  TGA  ( stop codons ) 
 
 Sequences containing the motif  ATAT  (a simple repeated pattern) 
 
 Sequences that have  at least   3   consecutive   G  (like  GGG  or  GGGG ) 
 
 
 Return  the result table ordered by  sample_id in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 Samples table: 
 
```text
+-----------+------------------+-----------+
| sample_id | dna_sequence     | species   |
+-----------+------------------+-----------+
| 1         | ATGCTAGCTAGCTAA  | Human     |
| 2         | GGGTCAATCATC     | Human     |
| 3         | ATATATCGTAGCTA   | Human     |
| 4         | ATGGGGTCATCATAA  | Mouse     |
| 5         | TCAGTCAGTCAG     | Mouse     |
| 6         | ATATCGCGCTAG     | Zebrafish |
| 7         | CGTATGCGTCGTA    | Zebrafish |
+-----------+------------------+-----------+
```
 
 
 Output: 
 
```text
+-----------+------------------+-------------+-------------+------------+------------+------------+
| sample_id | dna_sequence     | species     | has_start   | has_stop   | has_atat   | has_ggg    |
+-----------+------------------+-------------+-------------+------------+------------+------------+
| 1         | ATGCTAGCTAGCTAA  | Human       | 1           | 1          | 0          | 0          |
| 2         | GGGTCAATCATC     | Human       | 0           | 0          | 0          | 1          |
| 3         | ATATATCGTAGCTA   | Human       | 0           | 0          | 1          | 0          |
| 4         | ATGGGGTCATCATAA  | Mouse       | 1           | 1          | 0          | 1          |
| 5         | TCAGTCAGTCAG     | Mouse       | 0           | 0          | 0          | 0          |
| 6         | ATATCGCGCTAG     | Zebrafish   | 0           | 1          | 1          | 0          |
| 7         | CGTATGCGTCGTA    | Zebrafish   | 0           | 0          | 0          | 0          |
+-----------+------------------+-------------+-------------+------------+------------+------------+
```
 
 
 Explanation: 
 
 
 Sample 1 (ATGCTAGCTAGCTAA):
	 
 
 Starts with ATG (has_start = 1) 
 
 Ends with TAA (has_stop = 1) 
 
 Does not contain ATAT (has_atat = 0) 
 
 Does not contain at least 3 consecutive 'G's (has_ggg = 0) 
 
 
 
 Sample 2 (GGGTCAATCATC):
	 
 
 Does not start with ATG (has_start = 0) 
 
 Does not end with TAA, TAG, or TGA (has_stop = 0) 
 
 Does not contain ATAT (has_atat = 0) 
 
 Contains GGG (has_ggg = 1) 
 
 
 
 Sample 3 (ATATATCGTAGCTA):
	 
 
 Does not start with ATG (has_start = 0) 
 
 Does not end with TAA, TAG, or TGA (has_stop = 0) 
 
 Contains ATAT (has_atat = 1) 
 
 Does not contain at least 3 consecutive 'G's (has_ggg = 0) 
 
 
 
 Sample 4 (ATGGGGTCATCATAA):
	 
 
 Starts with ATG (has_start = 1) 
 
 Ends with TAA (has_stop = 1) 
 
 Does not contain ATAT (has_atat = 0) 
 
 Contains GGGG (has_ggg = 1) 
 
 
 
 Sample 5 (TCAGTCAGTCAG):
	 
 
 Does not match any patterns (all fields = 0) 
 
 
 
 Sample 6 (ATATCGCGCTAG):
	 
 
 Does not start with ATG (has_start = 0) 
 
 Ends with TAG (has_stop = 1) 
 
 Starts with ATAT (has_atat = 1) 
 
 Does not contain at least 3 consecutive 'G's (has_ggg = 0) 
 
 
 
 Sample 7 (CGTATGCGTCGTA):
	 
 
 Does not start with ATG (has_start = 0) 
 
 Does not end with TAA, "TAG", or "TGA" (has_stop = 0) 
 
 Does not contain ATAT (has_atat = 0) 
 
 Does not contain at least 3 consecutive 'G's (has_ggg = 0) 
 
 
 
 
 Note: 
 
 
 The result is ordered by sample_id in ascending order 
 
 For each pattern, 1 indicates the pattern is present and 0 indicates it is not present

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT sample_id,dna_sequence,species,
 (dna_sequence LIKE 'ATG%') AS has_start,
 REGEXP_LIKE(dna_sequence,'(TAA|TAG|TGA)$','c') AS has_stop,
 (dna_sequence LIKE '%ATAT%') AS has_atat,
 REGEXP_LIKE(dna_sequence,'GGG+','c') AS has_ggg
FROM Samples ORDER BY sample_id;
```

---

## 3482. Analyze Organization Hierarchy

**Problem:** https://leetcode.com/problems/analyze-organization-hierarchy/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195515504  
**Language:** mysql

### Description

Table:  Employees 
 
```text
+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| employee_id    | int     |
| employee_name  | varchar |
| manager_id     | int     |
| salary         | int     |
| department     | varchar |
+----------------+----------+
employee_id is the unique key for this table.
Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department.
manager_id is null for the top-level manager (CEO).
```
 
 
 Write a solution to analyze the organizational hierarchy and answer the following: 
 
 
 Hierarchy Levels:  For each employee, determine their level in the organization (CEO is level  1 , employees reporting directly to the CEO are level  2 , and so on). 
 
 Team Size:  For each employee who is a manager, count the total number of employees under them (direct and indirect reports). 
 
 Salary Budget:  For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary). 
 
 
 Return  the result table ordered by  the result ordered by  level  in  ascending  order, then by  budget  in  descending  order, and finally by  employee_name  in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 Employees table: 
 
```text
+-------------+---------------+------------+--------+-------------+
| employee_id | employee_name | manager_id | salary | department  |
+-------------+---------------+------------+--------+-------------+
| 1           | Alice         | null       | 12000  | Executive   |
| 2           | Bob           | 1          | 10000  | Sales       |
| 3           | Charlie       | 1          | 10000  | Engineering |
| 4           | David         | 2          | 7500   | Sales       |
| 5           | Eva           | 2          | 7500   | Sales       |
| 6           | Frank         | 3          | 9000   | Engineering |
| 7           | Grace         | 3          | 8500   | Engineering |
| 8           | Hank          | 4          | 6000   | Sales       |
| 9           | Ivy           | 6          | 7000   | Engineering |
| 10          | Judy          | 6          | 7000   | Engineering |
+-------------+---------------+------------+--------+-------------+
```
 
 
 Output: 
 
```text
+-------------+---------------+-------+-----------+--------+
| employee_id | employee_name | level | team_size | budget |
+-------------+---------------+-------+-----------+--------+
| 1           | Alice         | 1     | 9         | 84500  |
| 3           | Charlie       | 2     | 4         | 41500  |
| 2           | Bob           | 2     | 3         | 31000  |
| 6           | Frank         | 3     | 2         | 23000  |
| 4           | David         | 3     | 1         | 13500  |
| 7           | Grace         | 3     | 0         | 8500   |
| 5           | Eva           | 3     | 0         | 7500   |
| 9           | Ivy           | 4     | 0         | 7000   |
| 10          | Judy          | 4     | 0         | 7000   |
| 8           | Hank          | 4     | 0         | 6000   |
+-------------+---------------+-------+-----------+--------+
```
 
 
 Explanation: 
 
 
 Organization Structure: 
 
 
 Alice (ID: 1) is the CEO (level 1) with no manager 
 
 Bob (ID: 2) and Charlie (ID: 3) report directly to Alice (level 2) 
 
 David (ID: 4), Eva (ID: 5) report to Bob, while Frank (ID: 6) and Grace (ID: 7) report to Charlie (level 3) 
 
 Hank (ID: 8) reports to David, and Ivy (ID: 9) and Judy (ID: 10) report to Frank (level 4) 
 
 
 
 Level Calculation: 
 
 
 The CEO (Alice) is at level 1 
 
 Each subsequent level of management adds 1 to the level 
 
 
 
 Team Size Calculation: 
 
 
 Alice has 9 employees under her (the entire company except herself) 
 
 Bob has 3 employees (David, Eva, and Hank) 
 
 Charlie has 4 employees (Frank, Grace, Ivy, and Judy) 
 
 David has 1 employee (Hank) 
 
 Frank has 2 employees (Ivy and Judy) 
 
 Eva, Grace, Hank, Ivy, and Judy have no direct reports (team_size = 0) 
 
 
 
 Budget Calculation: 
 
 
 Alice's budget: Her salary (12000) + all employees' salaries (72500) = 84500 
 
 Charlie's budget: His salary (10000) + Frank's budget (23000) + Grace's salary (8500) = 41500 
 
 Bob's budget: His salary (10000) + David's budget (13500) + Eva's salary (7500) = 31000 
 
 Frank's budget: His salary (9000) + Ivy's salary (7000) + Judy's salary (7000) = 23000 
 
 David's budget: His salary (7500) + Hank's salary (6000) = 13500 
 
 Employees with no direct reports have budgets equal to their own salary 
 
 
 
 
 Note: 
 
 
 The result is ordered first by level in ascending order 
 
 Within the same level, employees are ordered by budget in descending order then by name in ascending order

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH RECURSIVE hierarchy AS (
 SELECT employee_id, employee_name, manager_id, salary, 1 AS level
 FROM Employees WHERE manager_id IS NULL
 UNION ALL
 SELECT e.employee_id, e.employee_name, e.manager_id, e.salary, h.level+1
 FROM Employees e JOIN hierarchy h ON e.manager_id=h.employee_id
), descendants AS (
 SELECT employee_id AS manager_id, employee_id AS member_id FROM Employees
 UNION ALL
 SELECT d.manager_id, e.employee_id
 FROM descendants d JOIN Employees e ON e.manager_id=d.member_id
)
SELECT h.employee_id, h.employee_name, h.level,
       COUNT(*)-1 AS team_size, SUM(e.salary) AS budget
FROM hierarchy h JOIN descendants d ON d.manager_id=h.employee_id
JOIN Employees e ON e.employee_id=d.member_id
GROUP BY h.employee_id, h.employee_name, h.level
ORDER BY h.level, budget DESC, h.employee_name;
```

---

## 3497. Analyze Subscription Conversion 

**Problem:** https://leetcode.com/problems/analyze-subscription-conversion/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195515615  
**Language:** mysql

### Description

Table:  UserActivity 
 
```text
+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| user_id          | int     |
| activity_date    | date    |
| activity_type    | varchar |
| activity_duration| int     |
+------------------+---------+
(user_id, activity_date, activity_type) is the unique key for this table.
activity_type is one of ('free_trial', 'paid', 'cancelled').
activity_duration is the number of minutes the user spent on the platform that day.
Each row represents a user's activity on a specific date.
```
 
 
 A subscription service wants to analyze user behavior patterns. The company offers a  7 -day  free trial , after which users can subscribe to a  paid plan  or  cancel . Write a solution to: 
 
 
 Find users who converted from free trial to paid subscription 
 
 Calculate each user's  average daily activity duration  during their  free trial  period (rounded to  2  decimal places) 
 
 Calculate each user's  average daily activity duration  during their  paid  subscription period (rounded to  2  decimal places) 
 
 
 Return  the result table ordered by  user_id  in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 UserActivity table: 
 
```text
+---------+---------------+---------------+-------------------+
| user_id | activity_date | activity_type | activity_duration |
+---------+---------------+---------------+-------------------+
| 1       | 2023-01-01    | free_trial    | 45                |
| 1       | 2023-01-02    | free_trial    | 30                |
| 1       | 2023-01-05    | free_trial    | 60                |
| 1       | 2023-01-10    | paid          | 75                |
| 1       | 2023-01-12    | paid          | 90                |
| 1       | 2023-01-15    | paid          | 65                |
| 2       | 2023-02-01    | free_trial    | 55                |
| 2       | 2023-02-03    | free_trial    | 25                |
| 2       | 2023-02-07    | free_trial    | 50                |
| 2       | 2023-02-10    | cancelled     | 0                 |
| 3       | 2023-03-05    | free_trial    | 70                |
| 3       | 2023-03-06    | free_trial    | 60                |
| 3       | 2023-03-08    | free_trial    | 80                |
| 3       | 2023-03-12    | paid          | 50                |
| 3       | 2023-03-15    | paid          | 55                |
| 3       | 2023-03-20    | paid          | 85                |
| 4       | 2023-04-01    | free_trial    | 40                |
| 4       | 2023-04-03    | free_trial    | 35                |
| 4       | 2023-04-05    | paid          | 45                |
| 4       | 2023-04-07    | cancelled     | 0                 |
+---------+---------------+---------------+-------------------+
```
 
 
 Output: 
 
```text
+---------+--------------------+-------------------+
| user_id | trial_avg_duration | paid_avg_duration |
+---------+--------------------+-------------------+
| 1       | 45.00              | 76.67             |
| 3       | 70.00              | 63.33             |
| 4       | 37.50              | 45.00             |
+---------+--------------------+-------------------+
```
 
 
 Explanation: 
 
 
 User 1: 
 
 
 Had 3 days of free trial with durations of 45, 30, and 60 minutes. 
 
 Average trial duration: (45 + 30 + 60) / 3 = 45.00 minutes. 
 
 Had 3 days of paid subscription with durations of 75, 90, and 65 minutes. 
 
 Average paid duration: (75 + 90 + 65) / 3 = 76.67 minutes. 
 
 
 
 User 2: 
 
 
 Had 3 days of free trial with durations of 55, 25, and 50 minutes. 
 
 Average trial duration: (55 + 25 + 50) / 3 = 43.33 minutes. 
 
 Did not convert to a paid subscription (only had free_trial and cancelled activities). 
 
 Not included in the output because they didn't convert to paid. 
 
 
 
 User 3: 
 
 
 Had 3 days of free trial with durations of 70, 60, and 80 minutes. 
 
 Average trial duration: (70 + 60 + 80) / 3 = 70.00 minutes. 
 
 Had 3 days of paid subscription with durations of 50, 55, and 85 minutes. 
 
 Average paid duration: (50 + 55 + 85) / 3 = 63.33 minutes. 
 
 
 
 User 4: 
 
 
 Had 2 days of free trial with durations of 40 and 35 minutes. 
 
 Average trial duration: (40 + 35) / 2 = 37.50 minutes. 
 
 Had 1 day of paid subscription with duration of 45 minutes before cancelling. 
 
 Average paid duration: 45.00 minutes. 
 
 
 
 
 The result table only includes users who converted from free trial to paid subscription (users 1, 3, and 4), and is ordered by user_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT user_id,
 ROUND(AVG(CASE WHEN activity_type='free_trial' THEN activity_duration END),2) AS trial_avg_duration,
 ROUND(AVG(CASE WHEN activity_type='paid' THEN activity_duration END),2) AS paid_avg_duration
FROM UserActivity
GROUP BY user_id
HAVING SUM(activity_type='free_trial')>0 AND SUM(activity_type='paid')>0
ORDER BY user_id;
```

---

## 3521. Find Product Recommendation Pairs

**Problem:** https://leetcode.com/problems/find-product-recommendation-pairs/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195612909  
**Language:** mysql

### Description

Table:  ProductPurchases 
 
```text
+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) is the unique key for this table.
Each row represents a purchase of a product by a user in a specific quantity.
```
 
 
 Table:  ProductInfo 
 
```text
+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the primary key for this table.
Each row assigns a category and price to a product.
```
 
 
 Amazon wants to implement the  Customers who bought this also bought...  feature based on  co-purchase patterns . Write a solution to : 
 
 
 Identify  distinct  product pairs frequently  purchased together by the same customers  (where  product1_id  <  product2_id ) 
 
 For  each product pair , determine how many customers purchased  both  products 
 
 
 A product pair  is considered for recommendation  if   at least   3   different  customers have purchased  both products . 
 
 Return  the  result table ordered by  customer_count  in  descending  order, and in case of a tie, by  product1_id  in  ascending  order, and then by  product2_id  in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 ProductPurchases table: 
 
```text
+---------+------------+----------+
| user_id | product_id | quantity |
+---------+------------+----------+
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 103        | 3        |
| 2       | 101        | 1        |
| 2       | 102        | 5        |
| 2       | 104        | 1        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 105        | 4        |
| 4       | 101        | 1        |
| 4       | 102        | 1        |
| 4       | 103        | 2        |
| 4       | 104        | 3        |
| 5       | 102        | 2        |
| 5       | 104        | 1        |
+---------+------------+----------+
```
 
 
 ProductInfo table: 
 
```text
+------------+-------------+-------+
| product_id | category    | price |
+------------+-------------+-------+
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Clothing    | 35    |
| 104        | Kitchen     | 50    |
| 105        | Sports      | 75    |
+------------+-------------+-------+
```
 
 
 Output: 
 
```text
+-------------+-------------+-------------------+-------------------+----------------+
| product1_id | product2_id | product1_category | product2_category | customer_count |
+-------------+-------------+-------------------+-------------------+----------------+
| 101         | 102         | Electronics       | Books             | 3              |
| 101         | 103         | Electronics       | Clothing          | 3              |
| 102         | 104         | Books             | Kitchen           | 3              |
+-------------+-------------+-------------------+-------------------+----------------+
```
 
 
 Explanation: 
 
 
 Product pair (101, 102): 
 
 
 Purchased by users 1, 2, and 4 (3 customers) 
 
 Product 101 is in Electronics category 
 
 Product 102 is in Books category 
 
 
 
 Product pair (101, 103): 
 
 
 Purchased by users 1, 3, and 4 (3 customers) 
 
 Product 101 is in Electronics category 
 
 Product 103 is in Clothing category 
 
 
 
 Product pair (102, 104): 
 
 
 Purchased by users 2, 4, and 5 (3 customers) 
 
 Product 102 is in Books category 
 
 Product 104 is in Kitchen category 
 
 
 
 
 The result is ordered by customer_count in descending order. For pairs with the same customer_count, they are ordered by product1_id and then product2_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    p1.product_id AS product1_id,
    p2.product_id AS product2_id,
    i1.category AS product1_category,
    i2.category AS product2_category,
    COUNT(*) AS customer_count
FROM ProductPurchases p1
JOIN ProductPurchases p2
    ON p1.user_id = p2.user_id
    AND p1.product_id < p2.product_id
JOIN ProductInfo i1
    ON p1.product_id = i1.product_id
JOIN ProductInfo i2
    ON p2.product_id = i2.product_id
GROUP BY
    p1.product_id,
    p2.product_id,
    i1.category,
    i2.category
HAVING COUNT(*) >= 3
ORDER BY
    customer_count DESC,
    product1_id ASC,
    product2_id ASC;
```

---

## 3554. Find Category Recommendation Pairs

**Problem:** https://leetcode.com/problems/find-category-recommendation-pairs/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195516596  
**Language:** mysql

### Description

Table:  ProductPurchases 
 
```text
+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) is the unique identifier for this table. 
Each row represents a purchase of a product by a user in a specific quantity.
```
 
 
 Table:  ProductInfo 
 
```text
+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the unique identifier for this table.
Each row assigns a category and price to a product.
```
 
 
 Amazon wants to understand shopping patterns across product categories. Write a solution to: 
 
 
 Find all  category pairs  (where  category1  <  category2 ) 
 
 For  each category pair , determine the number of  unique   customers  who purchased products from  both  categories 
 
 
 A category pair is considered  reportable  if at least  3  different customers have purchased products from both categories. 
 
 Return  the result table of reportable category pairs ordered by  customer_count  in  descending  order, and in case of a tie, by  category1  in  ascending  order lexicographically, and then by  category2  in  ascending  order. 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 ProductPurchases table: 
 
```text
+---------+------------+----------+
| user_id | product_id | quantity |
+---------+------------+----------+
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 201        | 3        |
| 1       | 301        | 1        |
| 2       | 101        | 1        |
| 2       | 102        | 2        |
| 2       | 103        | 1        |
| 2       | 201        | 5        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 301        | 4        |
| 3       | 401        | 2        |
| 4       | 101        | 1        |
| 4       | 201        | 3        |
| 4       | 301        | 1        |
| 4       | 401        | 2        |
| 5       | 102        | 2        |
| 5       | 103        | 1        |
| 5       | 201        | 2        |
| 5       | 202        | 3        |
+---------+------------+----------+
```
 
 
 ProductInfo table: 
 
```text
+------------+-------------+-------+
| product_id | category    | price |
+------------+-------------+-------+
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Books       | 35    |
| 201        | Clothing    | 45    |
| 202        | Clothing    | 60    |
| 301        | Sports      | 75    |
| 401        | Kitchen     | 50    |
+------------+-------------+-------+
```
 
 
 Output: 
 
```text
+-------------+-------------+----------------+
| category1   | category2   | customer_count |
+-------------+-------------+----------------+
| Books       | Clothing    | 3              |
| Books       | Electronics | 3              |
| Clothing    | Electronics | 3              |
| Electronics | Sports      | 3              |
+-------------+-------------+----------------+
```
 
 
 Explanation: 
 
 
 Books-Clothing :

	 
 
 User 1 purchased products from Books (102) and Clothing (201) 
 
 User 2 purchased products from Books (102, 103) and Clothing (201) 
 
 User 5 purchased products from Books (102, 103) and Clothing (201, 202) 
 
 Total: 3 customers purchased from both categories 
 
 
 
 Books-Electronics :
	 
 
 User 1 purchased products from Books (102) and Electronics (101) 
 
 User 2 purchased products from Books (102, 103) and Electronics (101) 
 
 User 3 purchased products from Books (103) and Electronics (101) 
 
 Total: 3 customers purchased from both categories 
 
 
 
 Clothing-Electronics :
	 
 
 User 1 purchased products from Clothing (201) and Electronics (101) 
 
 User 2 purchased products from Clothing (201) and Electronics (101) 
 
 User 4 purchased products from Clothing (201) and Electronics (101) 
 
 Total: 3 customers purchased from both categories 
 
 
 
 Electronics-Sports :
	 
 
 User 1 purchased products from Electronics (101) and Sports (301) 
 
 User 3 purchased products from Electronics (101) and Sports (301) 
 
 User 4 purchased products from Electronics (101) and Sports (301) 
 
 Total: 3 customers purchased from both categories 
 
 
 
 Other category pairs like Clothing-Sports (only 2 customers: Users 1 and 4) and Books-Kitchen (only 1 customer: User 3) have fewer than 3 shared customers and are not included in the result. 
 
 
 The result is ordered by customer_count in descending order. Since all pairs have the same customer_count of 3, they are ordered by category1 (then category2) in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH cats AS (
 SELECT DISTINCT p.user_id, i.category
 FROM ProductPurchases p JOIN ProductInfo i USING(product_id)
)
SELECT a.category AS category1, b.category AS category2, COUNT(*) AS customer_count
FROM cats a JOIN cats b ON a.user_id=b.user_id AND a.category<b.category
GROUP BY a.category,b.category HAVING COUNT(*)>=3
ORDER BY customer_count DESC, category1, category2;
```

---

## 3564. Seasonal Sales Analysis

**Problem:** https://leetcode.com/problems/seasonal-sales-analysis/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195516705  
**Language:** mysql

### Description

Table:  sales 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_id       | int     |
| product_id    | int     |
| sale_date     | date    |
| quantity      | int     |
| price         | decimal |
+---------------+---------+
sale_id is the unique identifier for this table.
Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.
```
 
 
 Table:  products 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| category      | varchar |
+---------------+---------+
product_id is the unique identifier for this table.
Each row contains information about a product including its name and category.
```
 
 
 Write a solution to find the most popular product category for each season. The seasons are defined as: 
 
 
 Winter : December, January, February 
 
 Spring : March, April, May 
 
 Summer : June, July, August 
 
 Fall : September, October, November 
 
 
 The  popularity  of a  category  is determined by the  total quantity sold  in that  season . If there is a  tie , select the category with the highest  total revenue  ( quantity × price ). If there is still a tie, return the lexicographically smaller category. 
 
 Return  the result table ordered by season in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 sales table: 
 
```text
+---------+------------+------------+----------+-------+
| sale_id | product_id | sale_date  | quantity | price |
+---------+------------+------------+----------+-------+
| 1       | 1          | 2023-01-15 | 5        | 10.00 |
| 2       | 2          | 2023-01-20 | 4        | 15.00 |
| 3       | 3          | 2023-03-10 | 3        | 18.00 |
| 4       | 4          | 2023-04-05 | 1        | 20.00 |
| 5       | 1          | 2023-05-20 | 2        | 10.00 |
| 6       | 2          | 2023-06-12 | 4        | 15.00 |
| 7       | 5          | 2023-06-15 | 5        | 12.00 |
| 8       | 3          | 2023-07-24 | 2        | 18.00 |
| 9       | 4          | 2023-08-01 | 5        | 20.00 |
| 10      | 5          | 2023-09-03 | 3        | 12.00 |
| 11      | 1          | 2023-09-25 | 6        | 10.00 |
| 12      | 2          | 2023-11-10 | 4        | 15.00 |
| 13      | 3          | 2023-12-05 | 6        | 18.00 |
| 14      | 4          | 2023-12-22 | 3        | 20.00 |
| 15      | 5          | 2024-02-14 | 2        | 12.00 |
+---------+------------+------------+----------+-------+
```
 
 
 products table: 
 
```text
+------------+-----------------+----------+
| product_id | product_name    | category |
+------------+-----------------+----------+
| 1          | Warm Jacket     | Apparel  |
| 2          | Designer Jeans  | Apparel  |
| 3          | Cutting Board   | Kitchen  |
| 4          | Smart Speaker   | Tech     |
| 5          | Yoga Mat        | Fitness  |
+------------+-----------------+----------+
```
 
 
 Output: 
 
```text
+---------+----------+----------------+---------------+
| season  | category | total_quantity | total_revenue |
+---------+----------+----------------+---------------+
| Fall    | Apparel  | 10             | 120.00        |
| Spring  | Kitchen  | 3              | 54.00         |
| Summer  | Tech     | 5              | 100.00        |
| Winter  | Apparel  | 9              | 110.00        |
+---------+----------+----------------+---------------+
```
 
 
 Explanation: 
 
 
 Fall (Sep, Oct, Nov): 
 
 
 Apparel: 10 items sold (6 Jackets in Sep, 4 Jeans in Nov), revenue $120.00 (6×$10.00 + 4×$15.00) 
 
 Fitness: 3 Yoga Mats sold in Sep, revenue $36.00 
 
 Most popular: Apparel with highest total quantity (10) 
 
 
 
 Spring (Mar, Apr, May): 
 
 
 Kitchen: 3 Cutting Boards sold in Mar, revenue $54.00 
 
 Tech: 1 Smart Speaker sold in Apr, revenue $20.00 
 
 Apparel: 2 Warm Jackets sold in May, revenue $20.00 
 
 Most popular: Kitchen with highest total quantity (3) and highest revenue ($54.00) 
 
 
 
 Summer (Jun, Jul, Aug): 
 
 
 Apparel: 4 Designer Jeans sold in Jun, revenue $60.00 
 
 Fitness: 5 Yoga Mats sold in Jun, revenue $60.00 
 
 Kitchen: 2 Cutting Boards sold in Jul, revenue $36.00 
 
 Tech: 5 Smart Speakers sold in Aug, revenue $100.00 
 
 Most popular: Tech and Fitness both have 5 items, but Tech has higher revenue ($100.00 vs $60.00) 
 
 
 
 Winter (Dec, Jan, Feb): 
 
 
 Apparel: 9 items sold (5 Jackets in Jan, 4 Jeans in Jan), revenue $110.00 
 
 Kitchen: 6 Cutting Boards sold in Dec, revenue $108.00 
 
 Tech: 3 Smart Speakers sold in Dec, revenue $60.00 
 
 Fitness: 2 Yoga Mats sold in Feb, revenue $24.00 
 
 Most popular: Apparel with highest total quantity (9) and highest revenue ($110.00) 
 
 
 
 
 The result table is ordered by season in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH totals AS (
 SELECT CASE WHEN MONTH(s.sale_date) IN (12,1,2) THEN 'Winter'
             WHEN MONTH(s.sale_date) IN (3,4,5) THEN 'Spring'
             WHEN MONTH(s.sale_date) IN (6,7,8) THEN 'Summer' ELSE 'Fall' END AS season,
        p.category, SUM(s.quantity) AS total_quantity,
        SUM(s.quantity*s.price) AS total_revenue
 FROM sales s JOIN products p USING(product_id)
 GROUP BY season,p.category
), ranked AS (
 SELECT *, ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC,total_revenue DESC,category) rn
 FROM totals
)
SELECT season,category,total_quantity,total_revenue FROM ranked WHERE rn=1 ORDER BY season;
```

---

## 3570. Find Books with No Available Copies

**Problem:** https://leetcode.com/problems/find-books-with-no-available-copies/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195613031  
**Language:** mysql

### Description

Table:  library_books 
 
```text
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| book_id          | int     |
| title            | varchar |
| author           | varchar |
| genre            | varchar |
| publication_year | int     |
| total_copies     | int     |
+------------------+---------+
book_id is the unique identifier for this table.
Each row contains information about a book in the library, including the total number of copies owned by the library.
```
 
 
 Table:  borrowing_records 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| record_id     | int     |
| book_id       | int     |
| borrower_name | varchar |
| borrow_date   | date    |
| return_date   | date    |
+---------------+---------+
record_id is the unique identifier for this table.
Each row represents a borrowing transaction and return_date is NULL if the book is currently borrowed and hasn't been returned yet.
```
 
 
 Write a solution to find  all books  that are  currently borrowed (not returned)  and have  zero copies available  in the library. 
 
 
 A book is considered  currently borrowed  if there exists a   borrowing record with a  NULL   return_date 
 
 
 Return  the result table ordered by current borrowers in  descending  order, then by book title in  ascending  order. 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 library_books table: 
 
```text
+---------+------------------------+------------------+----------+------------------+--------------+
| book_id | title                  | author           | genre    | publication_year | total_copies |
+---------+------------------------+------------------+----------+------------------+--------------+
| 1       | The Great Gatsby       | F. Scott         | Fiction  | 1925             | 3            |
| 2       | To Kill a Mockingbird  | Harper Lee       | Fiction  | 1960             | 3            |
| 3       | 1984                   | George Orwell    | Dystopian| 1949             | 1            |
| 4       | Pride and Prejudice    | Jane Austen      | Romance  | 1813             | 2            |
| 5       | The Catcher in the Rye | J.D. Salinger    | Fiction  | 1951             | 1            |
| 6       | Brave New World        | Aldous Huxley    | Dystopian| 1932             | 4            |
+---------+------------------------+------------------+----------+------------------+--------------+
```
 
 
 borrowing_records table: 
 
```text
+-----------+---------+---------------+-------------+-------------+
| record_id | book_id | borrower_name | borrow_date | return_date |
+-----------+---------+---------------+-------------+-------------+
| 1         | 1       | Alice Smith   | 2024-01-15  | NULL        |
| 2         | 1       | Bob Johnson   | 2024-01-20  | NULL        |
| 3         | 2       | Carol White   | 2024-01-10  | 2024-01-25  |
| 4         | 3       | David Brown   | 2024-02-01  | NULL        |
| 5         | 4       | Emma Wilson   | 2024-01-05  | NULL        |
| 6         | 5       | Frank Davis   | 2024-01-18  | 2024-02-10  |
| 7         | 1       | Grace Miller  | 2024-02-05  | NULL        |
| 8         | 6       | Henry Taylor  | 2024-01-12  | NULL        |
| 9         | 2       | Ivan Clark    | 2024-02-12  | NULL        |
| 10        | 2       | Jane Adams    | 2024-02-15  | NULL        |
+-----------+---------+---------------+-------------+-------------+
```
 
 
 Output: 
 
```text
+---------+------------------+---------------+-----------+------------------+-------------------+
| book_id | title            | author        | genre     | publication_year | current_borrowers |
+---------+------------------+---------------+-----------+------------------+-------------------+
| 1       | The Great Gatsby | F. Scott      | Fiction   | 1925             | 3                 | 
| 3       | 1984             | George Orwell | Dystopian | 1949             | 1                 |
+---------+------------------+---------------+-----------+------------------+-------------------+
```
 
 
 Explanation: 
 
 
 The Great Gatsby (book_id = 1): 
 
 
 Total copies: 3 
 
 Currently borrowed by Alice Smith, Bob Johnson, and Grace Miller (3 borrowers) 
 
 Available copies: 3 - 3 = 0 
 
 Included because available_copies = 0 
 
 
 
 1984 (book_id = 3): 
 
 
 Total copies: 1 
 
 Currently borrowed by David Brown (1 borrower) 
 
 Available copies: 1 - 1 = 0 
 
 Included because available_copies = 0 
 
 
 
 Books not included: 
 
 
 To Kill a Mockingbird (book_id = 2): Total copies = 3, current borrowers = 2, available = 1 
 
 Pride and Prejudice (book_id = 4): Total copies = 2, current borrowers = 1, available = 1 
 
 The Catcher in the Rye (book_id = 5): Total copies = 1, current borrowers = 0, available = 1 
 
 Brave New World (book_id = 6): Total copies = 4, current borrowers = 1, available = 3 
 
 
 
 Result ordering: 
 
 
 The Great Gatsby appears first with 3 current borrowers 
 
 1984 appears second with 1 current borrower 
 
 
 
 
 Output table is ordered by current_borrowers in descending order, then by book_title in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    COUNT(*) AS current_borrowers
FROM library_books b
JOIN borrowing_records r
    ON b.book_id = r.book_id
WHERE r.return_date IS NULL
GROUP BY
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    b.total_copies
HAVING COUNT(*) = b.total_copies
ORDER BY
    current_borrowers DESC,
    b.title ASC;
```

---

## 3580. Find Consistently Improving Employees

**Problem:** https://leetcode.com/problems/find-consistently-improving-employees/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195517645  
**Language:** mysql

### Description

Table:  employees 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee.
```
 
 
 Table:  performance_reviews 
 
```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| review_id   | int  |
| employee_id | int  |
| review_date | date |
| rating      | int  |
+-------------+------+
review_id is the unique identifier for this table.
Each row represents a performance review for an employee. The rating is on a scale of 1-5 where 5 is excellent and 1 is poor.
```
 
 
 Write a solution to find employees who have consistently improved their performance over  their last three reviews . 
 
 
 An employee must have  at least  3  review  to be considered 
 
 The employee's  last  3  reviews  must show  strictly increasing ratings  (each review better than the previous) 
 
 Use the most recent  3  reviews based on  review_date  for each employee 
 
 Calculate the  improvement score  as the difference between the latest rating and the earliest rating among the last  3  reviews 
 
 
 Return  the result table ordered by  improvement score  in  descending  order, then by  name  in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 employees table: 
 
```text
+-------------+----------------+
| employee_id | name           |
+-------------+----------------+
| 1           | Alice Johnson  |
| 2           | Bob Smith      |
| 3           | Carol Davis    |
| 4           | David Wilson   |
| 5           | Emma Brown     |
+-------------+----------------+
```
 
 
 performance_reviews table: 
 
```text
+-----------+-------------+-------------+--------+
| review_id | employee_id | review_date | rating |
+-----------+-------------+-------------+--------+
| 1         | 1           | 2023-01-15  | 2      |
| 2         | 1           | 2023-04-15  | 3      |
| 3         | 1           | 2023-07-15  | 4      |
| 4         | 1           | 2023-10-15  | 5      |
| 5         | 2           | 2023-02-01  | 3      |
| 6         | 2           | 2023-05-01  | 2      |
| 7         | 2           | 2023-08-01  | 4      |
| 8         | 2           | 2023-11-01  | 5      |
| 9         | 3           | 2023-03-10  | 1      |
| 10        | 3           | 2023-06-10  | 2      |
| 11        | 3           | 2023-09-10  | 3      |
| 12        | 3           | 2023-12-10  | 4      |
| 13        | 4           | 2023-01-20  | 4      |
| 14        | 4           | 2023-04-20  | 4      |
| 15        | 4           | 2023-07-20  | 4      |
| 16        | 5           | 2023-02-15  | 3      |
| 17        | 5           | 2023-05-15  | 2      |
+-----------+-------------+-------------+--------+
```
 
 
 Output: 
 
```text
+-------------+----------------+-------------------+
| employee_id | name           | improvement_score |
+-------------+----------------+-------------------+
| 2           | Bob Smith      | 3                 |
| 1           | Alice Johnson  | 2                 |
| 3           | Carol Davis    | 2                 |
+-------------+----------------+-------------------+
```
 
 
 Explanation: 
 
 
 Alice Johnson (employee_id = 1): 
 
 
 Has 4 reviews with ratings: 2, 3, 4, 5 
 
 Last 3 reviews (by date): 2023-04-15 (3), 2023-07-15 (4), 2023-10-15 (5) 
 
 Ratings are strictly increasing: 3 → 4 → 5 
 
 Improvement score: 5 - 3 = 2 
 
 
 
 Carol Davis (employee_id = 3): 
 
 
 Has 4 reviews with ratings: 1, 2, 3, 4 
 
 Last 3 reviews (by date): 2023-06-10 (2), 2023-09-10 (3), 2023-12-10 (4) 
 
 Ratings are strictly increasing: 2 → 3 → 4 
 
 Improvement score: 4 - 2 = 2 
 
 
 
 Bob Smith (employee_id = 2): 
 
 
 Has 4 reviews with ratings: 3, 2, 4, 5 
 
 Last 3 reviews (by date): 2023-05-01 (2), 2023-08-01 (4), 2023-11-01 (5) 
 
 Ratings are strictly increasing: 2 → 4 → 5 
 
 Improvement score: 5 - 2 = 3 
 
 
 
 Employees not included: 
 
 
 David Wilson (employee_id = 4): Last 3 reviews are all 4 (no improvement) 
 
 Emma Brown (employee_id = 5): Only has 2 reviews (needs at least 3) 
 
 
 
 
 The output table is ordered by improvement_score in descending order, then by name in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH last3 AS (
 SELECT employee_id,review_date,rating,
        ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC,review_id DESC) rn
 FROM performance_reviews
), pivoted AS (
 SELECT employee_id,MAX(CASE WHEN rn=1 THEN rating END) newest,
 MAX(CASE WHEN rn=2 THEN rating END) middle,
 MAX(CASE WHEN rn=3 THEN rating END) oldest
 FROM last3 WHERE rn<=3 GROUP BY employee_id
)
SELECT e.employee_id,e.name, p.newest-p.oldest AS improvement_score
FROM pivoted p JOIN employees e USING(employee_id)
WHERE oldest IS NOT NULL AND newest>middle AND middle>oldest
ORDER BY improvement_score DESC,e.name;
```

---

## 3586. Find COVID Recovery Patients

**Problem:** https://leetcode.com/problems/find-covid-recovery-patients/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195613185  
**Language:** mysql

### Description

Table:  patients 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| patient_id  | int     |
| patient_name| varchar |
| age         | int     |
+-------------+---------+
patient_id is the unique identifier for this table.
Each row contains information about a patient.
```
 
 
 Table:  covid_tests 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| test_id     | int     |
| patient_id  | int     |
| test_date   | date    |
| result      | varchar |
+-------------+---------+
test_id is the unique identifier for this table.
Each row represents a COVID test result. The result can be Positive, Negative, or Inconclusive.
```
 
 
 Write a solution to find patients who have  recovered from COVID  - patients who tested positive but later tested negative. 
 
 
 A patient is considered recovered if they have  at least one   Positive  test followed by at least one  Negative  test on a  later date 
 
 Calculate the  recovery time  in days as the  difference  between the  first positive test  and the  first negative test  after that  positive test 
 
 Only include  patients who have both positive and negative test results 
 
 
 Return  the result table ordered by  recovery_time  in  ascending  order, then by  patient_name  in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 patients table: 
 
```text
+------------+--------------+-----+
| patient_id | patient_name | age |
+------------+--------------+-----+
| 1          | Alice Smith  | 28  |
| 2          | Bob Johnson  | 35  |
| 3          | Carol Davis  | 42  |
| 4          | David Wilson | 31  |
| 5          | Emma Brown   | 29  |
+------------+--------------+-----+
```
 
 
 covid_tests table: 
 
```text
+---------+------------+------------+--------------+
| test_id | patient_id | test_date  | result       |
+---------+------------+------------+--------------+
| 1       | 1          | 2023-01-15 | Positive     |
| 2       | 1          | 2023-01-25 | Negative     |
| 3       | 2          | 2023-02-01 | Positive     |
| 4       | 2          | 2023-02-05 | Inconclusive |
| 5       | 2          | 2023-02-12 | Negative     |
| 6       | 3          | 2023-01-20 | Negative     |
| 7       | 3          | 2023-02-10 | Positive     |
| 8       | 3          | 2023-02-20 | Negative     |
| 9       | 4          | 2023-01-10 | Positive     |
| 10      | 4          | 2023-01-18 | Positive     |
| 11      | 5          | 2023-02-15 | Negative     |
| 12      | 5          | 2023-02-20 | Negative     |
+---------+------------+------------+--------------+
```
 
 
 Output: 
 
```text
+------------+--------------+-----+---------------+
| patient_id | patient_name | age | recovery_time |
+------------+--------------+-----+---------------+
| 1          | Alice Smith  | 28  | 10            |
| 3          | Carol Davis  | 42  | 10            |
| 2          | Bob Johnson  | 35  | 11            |
+------------+--------------+-----+---------------+
```
 
 
 Explanation: 
 
 
 Alice Smith (patient_id = 1): 
 
 
 First positive test: 2023-01-15 
 
 First negative test after positive: 2023-01-25 
 
 Recovery time: 25 - 15 = 10 days 
 
 
 
 Bob Johnson (patient_id = 2): 
 
 
 First positive test: 2023-02-01 
 
 Inconclusive test on 2023-02-05 (ignored for recovery calculation) 
 
 First negative test after positive: 2023-02-12 
 
 Recovery time: 12 - 1 = 11 days 
 
 
 
 Carol Davis (patient_id = 3): 
 
 
 Had negative test on 2023-01-20 (before positive test) 
 
 First positive test: 2023-02-10 
 
 First negative test after positive: 2023-02-20 
 
 Recovery time: 20 - 10 = 10 days 
 
 
 
 Patients not included: 
 
 
 David Wilson (patient_id = 4): Only has positive tests, no negative test after positive 
 
 Emma Brown (patient_id = 5): Only has negative tests, never tested positive 
 
 
 
 
 Output table is ordered by recovery_time in ascending order, and then by patient_name in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH FirstPositive AS (
    SELECT
        patient_id,
        MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
FirstNegative AS (
    SELECT
        t.patient_id,
        MIN(t.test_date) AS negative_date
    FROM covid_tests t
    JOIN FirstPositive p
        ON t.patient_id = p.patient_id
    WHERE t.result = 'Negative'
      AND t.test_date > p.positive_date
    GROUP BY t.patient_id
)
SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(n.negative_date, f.positive_date)
        AS recovery_time
FROM patients p
JOIN FirstPositive f
    ON p.patient_id = f.patient_id
JOIN FirstNegative n
    ON p.patient_id = n.patient_id
ORDER BY
    recovery_time ASC,
    p.patient_name ASC;
```

---

## 3601. Find Drivers with Improved Fuel Efficiency

**Problem:** https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195518573  
**Language:** mysql

### Description

Table:  drivers 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| driver_id   | int     |
| driver_name | varchar |
+-------------+---------+
driver_id is the unique identifier for this table.
Each row contains information about a driver.
```
 
 
 Table:  trips 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trip_id       | int     |
| driver_id     | int     |
| trip_date     | date    |
| distance_km   | decimal |
| fuel_consumed | decimal |
+---------------+---------+
trip_id is the unique identifier for this table.
Each row represents a trip made by a driver, including the distance traveled and fuel consumed for that trip.
```
 
 
 Write a solution to find drivers whose  fuel efficiency has improved  by  comparing  their average fuel efficiency in the  first half  of the year with the  second half  of the year. 
 
 
 Calculate  fuel efficiency  as  distance_km / fuel_consumed  for  each  trip 
 
 First half : January to June,  Second half : July to December 
 
 Only include drivers who have trips in  both halves  of the year 
 
 Calculate the  efficiency improvement  as ( second_half_avg - first_half_avg ) 
 
 Round  all   results   to   2   decimal   places 
 
 
 Return  the result table ordered by efficiency improvement in  descending  order, then by driver name in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 drivers table: 
 
```text
+-----------+---------------+
| driver_id | driver_name   |
+-----------+---------------+
| 1         | Alice Johnson |
| 2         | Bob Smith     |
| 3         | Carol Davis   |
| 4         | David Wilson  |
| 5         | Emma Brown    |
+-----------+---------------+
```
 
 
 trips table: 
 
```text
+---------+-----------+------------+-------------+---------------+
| trip_id | driver_id | trip_date  | distance_km | fuel_consumed |
+---------+-----------+------------+-------------+---------------+
| 1       | 1         | 2023-02-15 | 120.5       | 10.2          |
| 2       | 1         | 2023-03-20 | 200.0       | 16.5          |
| 3       | 1         | 2023-08-10 | 150.0       | 11.0          |
| 4       | 1         | 2023-09-25 | 180.0       | 12.5          |
| 5       | 2         | 2023-01-10 | 100.0       | 9.0           |
| 6       | 2         | 2023-04-15 | 250.0       | 22.0          |
| 7       | 2         | 2023-10-05 | 200.0       | 15.0          |
| 8       | 3         | 2023-03-12 | 80.0        | 8.5           |
| 9       | 3         | 2023-05-18 | 90.0        | 9.2           |
| 10      | 4         | 2023-07-22 | 160.0       | 12.8          |
| 11      | 4         | 2023-11-30 | 140.0       | 11.0          |
| 12      | 5         | 2023-02-28 | 110.0       | 11.5          |
+---------+-----------+------------+-------------+---------------+
```
 
 
 Output: 
 
```text
+-----------+---------------+------------------+-------------------+------------------------+
| driver_id | driver_name   | first_half_avg   | second_half_avg   | efficiency_improvement |
+-----------+---------------+------------------+-------------------+------------------------+
| 2         | Bob Smith     | 11.24            | 13.33             | 2.10                   |
| 1         | Alice Johnson | 11.97            | 14.02             | 2.05                   |
+-----------+---------------+------------------+-------------------+------------------------+
```
 
 
 Explanation: 
 
 
 Alice Johnson (driver_id = 1): 
 
 
 First half trips (Jan-Jun): Feb 15 (120.5/10.2 = 11.81), Mar 20 (200.0/16.5 = 12.12) 
 
 First half average efficiency: (11.81 + 12.12) / 2 = 11.97 
 
 Second half trips (Jul-Dec): Aug 10 (150.0/11.0 = 13.64), Sep 25 (180.0/12.5 = 14.40) 
 
 Second half average efficiency: (13.64 + 14.40) / 2 = 14.02 
 
 Efficiency improvement: 14.02 - 11.97 = 2.05 
 
 
 
 Bob Smith (driver_id = 2): 
 
 
 First half trips: Jan 10 (100.0/9.0 = 11.11), Apr 15 (250.0/22.0 = 11.36) 
 
 First half average efficiency: (11.11 + 11.36) / 2 = 11.24 
 
 Second half trips: Oct 5 (200.0/15.0 = 13.33) 
 
 Second half average efficiency: 13.33 
 
 Efficiency improvement: 13.33 - 11.24 = 2.10 (rounded to 2 decimal places) 
 
 
 
 Drivers not included: 
 
 
 Carol Davis (driver_id = 3): Only has trips in first half (Mar, May) 
 
 David Wilson (driver_id = 4): Only has trips in second half (Jul, Nov) 
 
 Emma Brown (driver_id = 5): Only has trips in first half (Feb) 
 
 
 
 
 The output table is ordered by efficiency improvement in descending order then by name in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH halves AS (
 SELECT driver_id,
 AVG(CASE WHEN MONTH(trip_date)<=6 THEN distance_km/fuel_consumed END) AS first_half_avg,
 AVG(CASE WHEN MONTH(trip_date)>6 THEN distance_km/fuel_consumed END) AS second_half_avg
 FROM trips GROUP BY driver_id
)
SELECT d.driver_id,d.driver_name,ROUND(h.first_half_avg,2) AS first_half_avg,
 ROUND(h.second_half_avg,2) AS second_half_avg,
 ROUND(h.second_half_avg-h.first_half_avg,2) AS efficiency_improvement
FROM halves h JOIN drivers d USING(driver_id)
WHERE h.first_half_avg IS NOT NULL AND h.second_half_avg>h.first_half_avg
ORDER BY efficiency_improvement DESC,d.driver_name;
```

---

## 3611. Find Overbooked Employees

**Problem:** https://leetcode.com/problems/find-overbooked-employees/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Database  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195613344  
**Language:** mysql

### Description

Table:  employees 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| employee_name | varchar |
| department    | varchar |
+---------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee and their department.
```
 
 
 Table:  meetings 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| meeting_id    | int     |
| employee_id   | int     |
| meeting_date  | date    |
| meeting_type  | varchar |
| duration_hours| decimal |
+---------------+---------+
meeting_id is the unique identifier for this table.
Each row represents a meeting attended by an employee. meeting_type can be 'Team', 'Client', or 'Training'.
```
 
 
 Write a solution to find employees who are  meeting-heavy  - employees who spend more than  50%  of their working time in meetings during any given week. 
 
 
 Assume a standard work week is  40  hours 
 
 Calculate  total meeting hours  per employee  per week  ( Monday to Sunday ) 
 
 An employee is meeting-heavy if their weekly meeting hours  >   20  hours ( 50%  of  40  hours) 
 
 Count how many weeks each employee was meeting-heavy 
 
 Only include  employees who were meeting-heavy for  at least  2  weeks 
 
 
 Return  the result table ordered by the number of meeting-heavy weeks in  descending  order, then by employee name in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 employees table: 
 
```text
+-------------+----------------+-------------+
| employee_id | employee_name  | department  |
+-------------+----------------+-------------+
| 1           | Alice Johnson  | Engineering |
| 2           | Bob Smith      | Marketing   |
| 3           | Carol Davis    | Sales       |
| 4           | David Wilson   | Engineering |
| 5           | Emma Brown     | HR          |
+-------------+----------------+-------------+
```
 
 
 meetings table: 
 
```text
+------------+-------------+--------------+--------------+----------------+
| meeting_id | employee_id | meeting_date | meeting_type | duration_hours |
+------------+-------------+--------------+--------------+----------------+
| 1          | 1           | 2023-06-05   | Team         | 8.0            |
| 2          | 1           | 2023-06-06   | Client       | 6.0            |
| 3          | 1           | 2023-06-07   | Training     | 7.0            |
| 4          | 1           | 2023-06-12   | Team         | 12.0           |
| 5          | 1           | 2023-06-13   | Client       | 9.0            |
| 6          | 2           | 2023-06-05   | Team         | 15.0           |
| 7          | 2           | 2023-06-06   | Client       | 8.0            |
| 8          | 2           | 2023-06-12   | Training     | 10.0           |
| 9          | 3           | 2023-06-05   | Team         | 4.0            |
| 10         | 3           | 2023-06-06   | Client       | 3.0            |
| 11         | 4           | 2023-06-05   | Team         | 25.0           |
| 12         | 4           | 2023-06-19   | Client       | 22.0           |
| 13         | 5           | 2023-06-05   | Training     | 2.0            |
+------------+-------------+--------------+--------------+----------------+
```
 
 
 Output: 
 
```text
+-------------+----------------+-------------+---------------------+
| employee_id | employee_name  | department  | meeting_heavy_weeks |
+-------------+----------------+-------------+---------------------+
| 1           | Alice Johnson  | Engineering | 2                   |
| 4           | David Wilson   | Engineering | 2                   |
+-------------+----------------+-------------+---------------------+
```
 
 
 Explanation: 
 
 
 Alice Johnson (employee_id = 1): 
 
 
 Week of June 5-11 (2023-06-05 to 2023-06-11): 8.0 + 6.0 + 7.0 = 21.0 hours (> 20 hours) 
 
 Week of June 12-18 (2023-06-12 to 2023-06-18): 12.0 + 9.0 = 21.0 hours (> 20 hours) 
 
 Meeting-heavy for 2 weeks 
 
 
 
 David Wilson (employee_id = 4): 
 
 
 Week of June 5-11: 25.0 hours (> 20 hours) 
 
 Week of June 19-25: 22.0 hours (> 20 hours) 
 
 Meeting-heavy for 2 weeks 
 
 
 
 Employees not included: 
 
 
 Bob Smith (employee_id = 2): Week of June 5-11: 15.0 + 8.0 = 23.0 hours (> 20), Week of June 12-18: 10.0 hours (< 20). Only 1 meeting-heavy week 
 
 Carol Davis (employee_id = 3): Week of June 5-11: 4.0 + 3.0 = 7.0 hours (< 20). No meeting-heavy weeks 
 
 Emma Brown (employee_id = 5): Week of June 5-11: 2.0 hours (< 20). No meeting-heavy weeks 
 
 
 
 
 The result table is ordered by meeting_heavy_weeks in descending order, then by employee name in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH WeeklyMeetings AS (
    SELECT
        employee_id,
        YEARWEEK(meeting_date, 1) AS week_id,
        SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY
        employee_id,
        YEARWEEK(meeting_date, 1)
    HAVING SUM(duration_hours) > 20
),
HeavyWeeks AS (
    SELECT
        employee_id,
        COUNT(*) AS meeting_heavy_weeks
    FROM WeeklyMeetings
    GROUP BY employee_id
    HAVING COUNT(*) >= 2
)
SELECT
    e.employee_id,
    e.employee_name,
    e.department,
    h.meeting_heavy_weeks
FROM HeavyWeeks h
JOIN employees e
    ON h.employee_id = e.employee_id
ORDER BY
    h.meeting_heavy_weeks DESC,
    e.employee_name ASC;
```

---

## 3617. Find Students with Study Spiral Pattern

**Problem:** https://leetcode.com/problems/find-students-with-study-spiral-pattern/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195613481  
**Language:** mysql

### Description

Table:  students 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| student_name | varchar |
| major        | varchar |
+--------------+---------+
student_id is the unique identifier for this table.
Each row contains information about a student and their academic major.
```
 
 
 Table:  study_sessions 
 
```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| session_id    | int     |
| student_id    | int     |
| subject       | varchar |
| session_date  | date    |
| hours_studied | decimal |
+---------------+---------+
session_id is the unique identifier for this table.
Each row represents a study session by a student for a specific subject.
```
 
 
 Write a solution to find students who follow the  Study Spiral Pattern  - students who consistently study multiple subjects in a rotating cycle. 
 
 
 A Study Spiral Pattern means a student studies at least  3  different subjects  in a repeating sequence 
 
 The pattern must repeat for  at least  2  complete cycles  (minimum  6  study sessions) 
 
 Sessions must be  consecutive dates  with no gaps longer than  2  days between sessions 
 
 Calculate the  cycle length  (number of different subjects in the pattern) 
 
 Calculate the  total study hours  across all sessions in the pattern 
 
 Only include students with cycle length of  at least  3  subjects 
 
 
 Return  the result table ordered by cycle length in  descending  order, then by total study hours in  descending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 students table: 
 
```text
+------------+--------------+------------------+
| student_id | student_name | major            |
+------------+--------------+------------------+
| 1          | Alice Chen   | Computer Science |
| 2          | Bob Johnson  | Mathematics      |
| 3          | Carol Davis  | Physics          |
| 4          | David Wilson | Chemistry        |
| 5          | Emma Brown   | Biology          |
+------------+--------------+------------------+
```
 
 
 study_sessions table: 
 
```text
+------------+------------+------------+--------------+---------------+
| session_id | student_id | subject    | session_date | hours_studied |
+------------+------------+------------+--------------+---------------+
| 1          | 1          | Math       | 2023-10-01   | 2.5           |
| 2          | 1          | Physics    | 2023-10-02   | 3.0           |
| 3          | 1          | Chemistry  | 2023-10-03   | 2.0           |
| 4          | 1          | Math       | 2023-10-04   | 2.5           |
| 5          | 1          | Physics    | 2023-10-05   | 3.0           |
| 6          | 1          | Chemistry  | 2023-10-06   | 2.0           |
| 7          | 2          | Algebra    | 2023-10-01   | 4.0           |
| 8          | 2          | Calculus   | 2023-10-02   | 3.5           |
| 9          | 2          | Statistics | 2023-10-03   | 2.5           |
| 10         | 2          | Geometry   | 2023-10-04   | 3.0           |
| 11         | 2          | Algebra    | 2023-10-05   | 4.0           |
| 12         | 2          | Calculus   | 2023-10-06   | 3.5           |
| 13         | 2          | Statistics | 2023-10-07   | 2.5           |
| 14         | 2          | Geometry   | 2023-10-08   | 3.0           |
| 15         | 3          | Biology    | 2023-10-01   | 2.0           |
| 16         | 3          | Chemistry  | 2023-10-02   | 2.5           |
| 17         | 3          | Biology    | 2023-10-03   | 2.0           |
| 18         | 3          | Chemistry  | 2023-10-04   | 2.5           |
| 19         | 4          | Organic    | 2023-10-01   | 3.0           |
| 20         | 4          | Physical   | 2023-10-05   | 2.5           |
+------------+------------+------------+--------------+---------------+
```
 
 
 Output: 
 
```text
+------------+--------------+------------------+--------------+-------------------+
| student_id | student_name | major            | cycle_length | total_study_hours |
+------------+--------------+------------------+--------------+-------------------+
| 2          | Bob Johnson  | Mathematics      | 4            | 26.0              |
| 1          | Alice Chen   | Computer Science | 3            | 15.0              |
+------------+--------------+------------------+--------------+-------------------+
```
 
 
 Explanation: 
 
 
 Alice Chen (student_id = 1): 
 
 
 Study sequence: Math → Physics → Chemistry → Math → Physics → Chemistry 
 
 Pattern: 3 subjects (Math, Physics, Chemistry) repeating for 2 complete cycles 
 
 Consecutive dates: Oct 1-6 with no gaps > 2 days 
 
 Cycle length: 3 subjects 
 
 Total hours: 2.5 + 3.0 + 2.0 + 2.5 + 3.0 + 2.0 = 15.0 hours 
 
 
 
 Bob Johnson (student_id = 2): 
 
 
 Study sequence: Algebra → Calculus → Statistics → Geometry → Algebra → Calculus → Statistics → Geometry 
 
 Pattern: 4 subjects (Algebra, Calculus, Statistics, Geometry) repeating for 2 complete cycles 
 
 Consecutive dates: Oct 1-8 with no gaps > 2 days 
 
 Cycle length: 4 subjects 
 
 Total hours: 4.0 + 3.5 + 2.5 + 3.0 + 4.0 + 3.5 + 2.5 + 3.0 = 26.0 hours 
 
 
 
 Students not included: 
 
 
 Carol Davis (student_id = 3): Only 2 subjects (Biology, Chemistry) - doesn't meet minimum 3 subjects requirement 
 
 David Wilson (student_id = 4): Only 2 study sessions with a 4-day gap - doesn't meet consecutive dates requirement 
 
 Emma Brown (student_id = 5): No study sessions recorded 
 
 
 
 
 The result table is ordered by cycle_length in descending order, then by total_study_hours in descending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH OrderedSessions AS (
    SELECT
        student_id,
        subject,
        session_date,
        hours_studied,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS rn,
        LAG(session_date) OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS prev_date
    FROM study_sessions
),
StudentStats AS (
    SELECT
        student_id,
        COUNT(*) AS total_sessions,
        COUNT(DISTINCT subject) AS cycle_length,
        SUM(hours_studied) AS total_study_hours,
        SUM(
            CASE
                WHEN DATEDIFF(session_date, prev_date) > 2
                THEN 1 ELSE 0
            END
        ) AS invalid_gaps
    FROM OrderedSessions
    GROUP BY student_id
),
ValidStudents AS (
    SELECT *
    FROM StudentStats
    WHERE cycle_length >= 3
      AND total_sessions >= 2 * cycle_length
      AND MOD(total_sessions, cycle_length) = 0
      AND invalid_gaps = 0
),
PatternCheck AS (
    SELECT
        v.student_id,
        COUNT(*) AS matching_sessions
    FROM ValidStudents v
    JOIN OrderedSessions a
        ON v.student_id = a.student_id
    JOIN OrderedSessions b
        ON a.student_id = b.student_id
        AND b.rn =
            MOD(a.rn - 1, v.cycle_length) + 1
    WHERE a.subject = b.subject
    GROUP BY v.student_id
)
SELECT
    s.student_id,
    s.student_name,
    s.major,
    v.cycle_length,
    v.total_study_hours
FROM ValidStudents v
JOIN PatternCheck p
    ON v.student_id = p.student_id
JOIN students s
    ON v.student_id = s.student_id
WHERE p.matching_sessions = v.total_sessions
ORDER BY
    v.cycle_length DESC,
    v.total_study_hours DESC;
```

---

## 3626. Find Stores with Inventory Imbalance

**Problem:** https://leetcode.com/problems/find-stores-with-inventory-imbalance/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195613699  
**Language:** mysql

### Description

Table:  stores 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| store_id    | int     |
| store_name  | varchar |
| location    | varchar |
+-------------+---------+
store_id is the unique identifier for this table.
Each row contains information about a store and its location.
```
 
 
 Table:  inventory 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| inventory_id| int     |
| store_id    | int     |
| product_name| varchar |
| quantity    | int     |
| price       | decimal |
+-------------+---------+
inventory_id is the unique identifier for this table.
Each row represents the inventory of a specific product at a specific store.
```
 
 
 Write a solution to find stores that have  inventory imbalance  - stores where the most expensive product has lower stock than the cheapest product. 
 
 
 For each store, identify the  most expensive product  (highest price) and its quantity 
 
 For each store, identify the  cheapest product  (lowest price) and its quantity 
 
 A store has inventory imbalance if the most expensive product's quantity is  less than  the cheapest product's quantity 
 
 Calculate the  imbalance ratio  as (cheapest_quantity / most_expensive_quantity) 
 
 Round  the imbalance ratio to  2  decimal places 
 
 Only include stores that have  at least  3  different products 
 
 
 Return  the result table ordered by imbalance ratio in  descending  order, then by store name in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 stores table: 
 
```text
+----------+----------------+-------------+
| store_id | store_name     | location    |
+----------+----------------+-------------+
| 1        | Downtown Tech  | New York    |
| 2        | Suburb Mall    | Chicago     |
| 3        | City Center    | Los Angeles |
| 4        | Corner Shop    | Miami       |
| 5        | Plaza Store    | Seattle     |
+----------+----------------+-------------+
```
 
 
 inventory table: 
 
```text
+--------------+----------+--------------+----------+--------+
| inventory_id | store_id | product_name | quantity | price  |
+--------------+----------+--------------+----------+--------+
| 1            | 1        | Laptop       | 5        | 999.99 |
| 2            | 1        | Mouse        | 50       | 19.99  |
| 3            | 1        | Keyboard     | 25       | 79.99  |
| 4            | 1        | Monitor      | 15       | 299.99 |
| 5            | 2        | Phone        | 3        | 699.99 |
| 6            | 2        | Charger      | 100      | 25.99  |
| 7            | 2        | Case         | 75       | 15.99  |
| 8            | 2        | Headphones   | 20       | 149.99 |
| 9            | 3        | Tablet       | 2        | 499.99 |
| 10           | 3        | Stylus       | 80       | 29.99  |
| 11           | 3        | Cover        | 60       | 39.99  |
| 12           | 4        | Watch        | 10       | 299.99 |
| 13           | 4        | Band         | 25       | 49.99  |
| 14           | 5        | Camera       | 8        | 599.99 |
| 15           | 5        | Lens         | 12       | 199.99 |
+--------------+----------+--------------+----------+--------+
```
 
 
 Output: 
 
```text
+----------+----------------+-------------+------------------+--------------------+------------------+
| store_id | store_name     | location    | most_exp_product | cheapest_product   | imbalance_ratio  |
+----------+----------------+-------------+------------------+--------------------+------------------+
| 3        | City Center    | Los Angeles | Tablet           | Stylus             | 40.00            |
| 2        | Suburb Mall    | Chicago     | Phone            | Case               | 25.00            |
| 1        | Downtown Tech  | New York    | Laptop           | Mouse              | 10.00            |
+----------+----------------+-------------+------------------+--------------------+------------------+
```
 
 
 Explanation: 
 
 
 Downtown Tech (store_id = 1): 
 
 
 Most expensive product: Laptop ($999.99) with quantity 5 
 
 Cheapest product: Mouse ($19.99) with quantity 50 
 
 Inventory imbalance: 5 < 50 (expensive product has lower stock) 
 
 Imbalance ratio: 50 / 5 = 10.00 
 
 Has 4 products (≥ 3), so qualifies 
 
 
 
 Suburb Mall (store_id = 2): 
 
 
 Most expensive product: Phone ($699.99) with quantity 3 
 
 Cheapest product: Case ($15.99) with quantity 75 
 
 Inventory imbalance: 3 < 75 (expensive product has lower stock) 
 
 Imbalance ratio: 75 / 3 = 25.00 
 
 Has 4 products (≥ 3), so qualifies 
 
 
 
 City Center (store_id = 3): 
 
 
 Most expensive product: Tablet ($499.99) with quantity 2 
 
 Cheapest product: Stylus ($29.99) with quantity 80 
 
 Inventory imbalance: 2 < 80 (expensive product has lower stock) 
 
 Imbalance ratio: 80 / 2 = 40.00 
 
 Has 3 products (≥ 3), so qualifies 
 
 
 
 Stores not included: 
 
 
 Corner Shop (store_id = 4): Only has 2 products (Watch, Band) - doesn't meet minimum 3 products requirement 
 
 Plaza Store (store_id = 5): Only has 2 products (Camera, Lens) - doesn't meet minimum 3 products requirement 
 
 
 
 
 The Results table is ordered by imbalance ratio in descending order, then by store name in ascending order

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH RankedProducts AS (
    SELECT
        store_id,
        product_name,
        quantity,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price DESC, quantity DESC, inventory_id
        ) AS expensive_rank,
        ROW_NUMBER() OVER (
            PARTITION BY store_id
            ORDER BY price ASC, quantity DESC, inventory_id
        ) AS cheap_rank,
        COUNT(*) OVER (
            PARTITION BY store_id
        ) AS product_count
    FROM inventory
)
SELECT
    s.store_id,
    s.store_name,
    s.location,
    e.product_name AS most_exp_product,
    c.product_name AS cheapest_product,
    ROUND(c.quantity / e.quantity, 2) AS imbalance_ratio
FROM stores s
JOIN RankedProducts e
    ON s.store_id = e.store_id
    AND e.expensive_rank = 1
JOIN RankedProducts c
    ON s.store_id = c.store_id
    AND c.cheap_rank = 1
WHERE e.product_count >= 3
  AND e.quantity < c.quantity
ORDER BY
    imbalance_ratio DESC,
    s.store_name ASC;
```

---

## 3642. Find Books with Polarized Opinions

**Problem:** https://leetcode.com/problems/find-books-with-polarized-opinions/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195613923  
**Language:** mysql

### Description

Table:  books 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| book_id     | int     |
| title       | varchar |
| author      | varchar |
| genre       | varchar |
| pages       | int     |
+-------------+---------+
book_id is the unique ID for this table.
Each row contains information about a book including its genre and page count.
```
 
 
 Table:  reading_sessions 
 
```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| session_id     | int     |
| book_id        | int     |
| reader_name    | varchar |
| pages_read     | int     |
| session_rating | int     |
+----------------+---------+
session_id is the unique ID for this table.
Each row represents a reading session where someone read a portion of a book. session_rating is on a scale of 1-5.
```
 
 
 Write a solution to find books that have  polarized opinions  - books that receive both very high ratings and very low ratings from different readers. 
 
 
 A book has polarized opinions if it has  at least one rating ≥ 4  and  at least one rating ≤ 2 
 
 Only consider books that have  at least  5  reading sessions 
 
 Calculate the  rating spread  as ( highest_rating - lowest_rating ) 
 
 Calculate the  polarization score  as the number of extreme ratings ( ratings ≤ 2 or ≥ 4 ) divided by total sessions 
 
 Only include  books where  polarization score ≥ 0.6  (at least  60%  extreme ratings) 
 
 
 Return  the result table ordered by polarization score in  descending  order, then by title in  descending  order . 
The  polarization score  should be rounded to 2 decimal places. 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 books table: 
 
```text
+---------+------------------------+---------------+----------+-------+
| book_id | title                  | author        | genre    | pages |
+---------+------------------------+---------------+----------+-------+
| 1       | The Great Gatsby       | F. Scott      | Fiction  | 180   |
| 2       | To Kill a Mockingbird  | Harper Lee    | Fiction  | 281   |
| 3       | 1984                   | George Orwell | Dystopian| 328   |
| 4       | Pride and Prejudice    | Jane Austen   | Romance  | 432   |
| 5       | The Catcher in the Rye | J.D. Salinger | Fiction  | 277   |
+---------+------------------------+---------------+----------+-------+
```
 
 
 reading_sessions table: 
 
```text
+------------+---------+-------------+------------+----------------+
| session_id | book_id | reader_name | pages_read | session_rating |
+------------+---------+-------------+------------+----------------+
| 1          | 1       | Alice       | 50         | 5              |
| 2          | 1       | Bob         | 60         | 1              |
| 3          | 1       | Carol       | 40         | 4              |
| 4          | 1       | David       | 30         | 2              |
| 5          | 1       | Emma        | 45         | 5              |
| 6          | 2       | Frank       | 80         | 4              |
| 7          | 2       | Grace       | 70         | 4              |
| 8          | 2       | Henry       | 90         | 5              |
| 9          | 2       | Ivy         | 60         | 4              |
| 10         | 2       | Jack        | 75         | 4              |
| 11         | 3       | Kate        | 100        | 2              |
| 12         | 3       | Liam        | 120        | 1              |
| 13         | 3       | Mia         | 80         | 2              |
| 14         | 3       | Noah        | 90         | 1              |
| 15         | 3       | Olivia      | 110        | 4              |
| 16         | 3       | Paul        | 95         | 5              |
| 17         | 4       | Quinn       | 150        | 3              |
| 18         | 4       | Ruby        | 140        | 3              |
| 19         | 5       | Sam         | 80         | 1              |
| 20         | 5       | Tara        | 70         | 2              |
+------------+---------+-------------+------------+----------------+
```
 
 
 Output: 
 
```text
+---------+------------------+---------------+-----------+-------+---------------+--------------------+
| book_id | title            | author        | genre     | pages | rating_spread | polarization_score |
+---------+------------------+---------------+-----------+-------+---------------+--------------------+
| 1       | The Great Gatsby | F. Scott      | Fiction   | 180   | 4             | 1.00               |
| 3       | 1984             | George Orwell | Dystopian | 328   | 4             | 1.00               |
+---------+------------------+---------------+-----------+-------+---------------+--------------------+
```
 
 
 Explanation: 
 
 
 The Great Gatsby (book_id = 1): 
 
 
 Has 5 reading sessions (meets minimum requirement) 
 
 Ratings: 5, 1, 4, 2, 5 
 
 Has ratings ≥ 4: 5, 4, 5 (3 sessions) 
 
 Has ratings ≤ 2: 1, 2 (2 sessions) 
 
 Rating spread: 5 - 1 = 4 
 
 Extreme ratings (≤2 or ≥4): All 5 sessions (5, 1, 4, 2, 5) 
 
 Polarization score: 5/5 = 1.00 (≥ 0.6, qualifies) 
 
 
 
 1984 (book_id = 3): 
 
 
 Has 6 reading sessions (meets minimum requirement) 
 
 Ratings: 2, 1, 2, 1, 4, 5 
 
 Has ratings ≥ 4: 4, 5 (2 sessions) 
 
 Has ratings ≤ 2: 2, 1, 2, 1 (4 sessions) 
 
 Rating spread: 5 - 1 = 4 
 
 Extreme ratings (≤2 or ≥4): All 6 sessions (2, 1, 2, 1, 4, 5) 
 
 Polarization score: 6/6 = 1.00 (≥ 0.6, qualifies) 
 
 
 
 Books not included: 
 
 
 To Kill a Mockingbird (book_id = 2): All ratings are 4-5, no low ratings (≤2) 
 
 Pride and Prejudice (book_id = 4): Only 2 sessions (< 5 minimum) 
 
 The Catcher in the Rye (book_id = 5): Only 2 sessions (< 5 minimum) 
 
 
 
 
 The result table is ordered by polarization score in descending order, then by book title in descending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,
    MAX(r.session_rating) - MIN(r.session_rating)
        AS rating_spread,
    ROUND(
        SUM(
            CASE
                WHEN r.session_rating <= 2
                  OR r.session_rating >= 4
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS polarization_score
FROM books b
JOIN reading_sessions r
    ON b.book_id = r.book_id
GROUP BY
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages
HAVING
    COUNT(*) >= 5
    AND MAX(r.session_rating) >= 4
    AND MIN(r.session_rating) <= 2
    AND SUM(
        CASE
            WHEN r.session_rating <= 2
              OR r.session_rating >= 4
            THEN 1
            ELSE 0
        END
    ) * 5 >= COUNT(*) * 3
ORDER BY
    polarization_score DESC,
    b.title DESC;
```

---

## 3657. Find Loyal Customers

**Problem:** https://leetcode.com/problems/find-loyal-customers/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195521048  
**Language:** mysql

### Description

Table:  customer_transactions 
 
```text
+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| transaction_id   | int     |
| customer_id      | int     |
| transaction_date | date    |
| amount           | decimal |
| transaction_type | varchar |
+------------------+---------+
transaction_id is the unique identifier for this table.
transaction_type can be either 'purchase' or 'refund'.
```
 
 
 Write a solution to find  loyal customers . A customer is considered  loyal  if they meet ALL the following criteria: 
 
 
 Made  at least   3  purchase transactions. 
 
 Have been active for  at least   30  days. 
 
 Their  refund rate  is less than  20%  . 
 
 
 Refund rate  is the proportion of transactions that are refunds, calculated as the number of refund transactions divided by the total number of transactions (purchases plus refunds). 
 
 Return  the result table ordered by   customer_id   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 customer_transactions table: 
 
```text
+----------------+-------------+------------------+--------+------------------+
| transaction_id | customer_id | transaction_date | amount | transaction_type |
+----------------+-------------+------------------+--------+------------------+
| 1              | 101         | 2024-01-05       | 150.00 | purchase         |
| 2              | 101         | 2024-01-15       | 200.00 | purchase         |
| 3              | 101         | 2024-02-10       | 180.00 | purchase         |
| 4              | 101         | 2024-02-20       | 250.00 | purchase         |
| 5              | 102         | 2024-01-10       | 100.00 | purchase         |
| 6              | 102         | 2024-01-12       | 120.00 | purchase         |
| 7              | 102         | 2024-01-15       | 80.00  | refund           |
| 8              | 102         | 2024-01-18       | 90.00  | refund           |
| 9              | 102         | 2024-02-15       | 130.00 | purchase         |
| 10             | 103         | 2024-01-01       | 500.00 | purchase         |
| 11             | 103         | 2024-01-02       | 450.00 | purchase         |
| 12             | 103         | 2024-01-03       | 400.00 | purchase         |
| 13             | 104         | 2024-01-01       | 200.00 | purchase         |
| 14             | 104         | 2024-02-01       | 250.00 | purchase         |
| 15             | 104         | 2024-02-15       | 300.00 | purchase         |
| 16             | 104         | 2024-03-01       | 350.00 | purchase         |
| 17             | 104         | 2024-03-10       | 280.00 | purchase         |
| 18             | 104         | 2024-03-15       | 100.00 | refund           |
+----------------+-------------+------------------+--------+------------------+
```
 
 
 Output: 
 
```text
+-------------+
| customer_id |
+-------------+
| 101         |
| 104         |
+-------------+
```
 
 
 Explanation: 
 
 
 Customer 101 :

	 
 
 Purchase transactions: 4 (IDs: 1, 2, 3, 4)  
 
 Refund transactions: 0 
 
 Refund rate: 0/4 = 0% (less than 20%)  
 
 Active period: Jan 5 to Feb 20 = 46 days (at least 30 days)  
 
 Qualifies as loyal  
 
 
 
 Customer 102 :
	 
 
 Purchase transactions: 3 (IDs: 5, 6, 9)  
 
 Refund transactions: 2 (IDs: 7, 8) 
 
 Refund rate: 2/5 = 40% (exceeds 20%)  
 
 Not loyal  
 
 
 
 Customer 103 :
	 
 
 Purchase transactions: 3 (IDs: 10, 11, 12)  
 
 Refund transactions: 0 
 
 Refund rate: 0/3 = 0% (less than 20%)  
 
 Active period: Jan 1 to Jan 3 = 2 days (less than 30 days)  
 
 Not loyal  
 
 
 
 Customer 104 :
	 
 
 Purchase transactions: 5 (IDs: 13, 14, 15, 16, 17)  
 
 Refund transactions: 1 (ID: 18) 
 
 Refund rate: 1/6 = 16.67% (less than 20%)  
 
 Active period: Jan 1 to Mar 15 = 73 days (at least 30 days)  
 
 Qualifies as loyal  
 
 
 
 
 The result table is ordered by customer_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
SELECT customer_id FROM customer_transactions
GROUP BY customer_id
HAVING SUM(transaction_type='purchase')>=3
 AND DATEDIFF(MAX(transaction_date),MIN(transaction_date))>=30
 AND AVG(transaction_type='refund')<0.20
ORDER BY customer_id;
```

---

## 3673. Find Zombie Sessions

**Problem:** https://leetcode.com/problems/find-zombie-sessions/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195614075  
**Language:** mysql

### Description

Table:  app_events 
 
```text
+------------------+----------+
| Column Name      | Type     | 
+------------------+----------+
| event_id         | int      |
| user_id          | int      |
| event_timestamp  | datetime |
| event_type       | varchar  |
| session_id       | varchar  |
| event_value      | int      |
+------------------+----------+
event_id is the unique identifier for this table.
event_type can be app_open, click, scroll, purchase, or app_close.
session_id groups events within the same user session.
event_value represents: for purchase - amount in dollars, for scroll - pixels scrolled, for others - NULL.
```
 
 
 Write a solution to identify  zombie sessions,  sessions where users appear active but show abnormal behavior patterns. A session is considered a  zombie session  if it meets ALL the following criteria: 
 
 
 The session duration is  more than   30  minutes. 
 
 Has  at least   5  scroll events. 
 
 The  click-to-scroll ratio  is less than  0.20  . 
 
 No purchases  were made during the session. 
 
 
 Return  the result table ordered by   scroll_count   in  descending  order, then by   session_id   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 app_events table: 
 
```text
+----------+---------+---------------------+------------+------------+-------------+
| event_id | user_id | event_timestamp     | event_type | session_id | event_value |
+----------+---------+---------------------+------------+------------+-------------+
| 1        | 201     | 2024-03-01 10:00:00 | app_open   | S001       | NULL        |
| 2        | 201     | 2024-03-01 10:05:00 | scroll     | S001       | 500         |
| 3        | 201     | 2024-03-01 10:10:00 | scroll     | S001       | 750         |
| 4        | 201     | 2024-03-01 10:15:00 | scroll     | S001       | 600         |
| 5        | 201     | 2024-03-01 10:20:00 | scroll     | S001       | 800         |
| 6        | 201     | 2024-03-01 10:25:00 | scroll     | S001       | 550         |
| 7        | 201     | 2024-03-01 10:30:00 | scroll     | S001       | 900         |
| 8        | 201     | 2024-03-01 10:35:00 | app_close  | S001       | NULL        |
| 9        | 202     | 2024-03-01 11:00:00 | app_open   | S002       | NULL        |
| 10       | 202     | 2024-03-01 11:02:00 | click      | S002       | NULL        |
| 11       | 202     | 2024-03-01 11:05:00 | scroll     | S002       | 400         |
| 12       | 202     | 2024-03-01 11:08:00 | click      | S002       | NULL        |
| 13       | 202     | 2024-03-01 11:10:00 | scroll     | S002       | 350         |
| 14       | 202     | 2024-03-01 11:15:00 | purchase   | S002       | 50          |
| 15       | 202     | 2024-03-01 11:20:00 | app_close  | S002       | NULL        |
| 16       | 203     | 2024-03-01 12:00:00 | app_open   | S003       | NULL        |
| 17       | 203     | 2024-03-01 12:10:00 | scroll     | S003       | 1000        |
| 18       | 203     | 2024-03-01 12:20:00 | scroll     | S003       | 1200        |
| 19       | 203     | 2024-03-01 12:25:00 | click      | S003       | NULL        |
| 20       | 203     | 2024-03-01 12:30:00 | scroll     | S003       | 800         |
| 21       | 203     | 2024-03-01 12:40:00 | scroll     | S003       | 900         |
| 22       | 203     | 2024-03-01 12:50:00 | scroll     | S003       | 1100        |
| 23       | 203     | 2024-03-01 13:00:00 | app_close  | S003       | NULL        |
| 24       | 204     | 2024-03-01 14:00:00 | app_open   | S004       | NULL        |
| 25       | 204     | 2024-03-01 14:05:00 | scroll     | S004       | 600         |
| 26       | 204     | 2024-03-01 14:08:00 | scroll     | S004       | 700         |
| 27       | 204     | 2024-03-01 14:10:00 | click      | S004       | NULL        |
| 28       | 204     | 2024-03-01 14:12:00 | app_close  | S004       | NULL        |
+----------+---------+---------------------+------------+------------+-------------+
```
 
 
 Output: 
 
```text
+------------+---------+--------------------------+--------------+
| session_id | user_id | session_duration_minutes | scroll_count |
+------------+---------+--------------------------+--------------+
| S001       | 201     | 35                       | 6            |
+------------+---------+--------------------------+--------------+
```
 
 
 Explanation: 
 
 
 Session S001 (User 201) :

	 
 
 Duration: 10:00:00 to 10:35:00 = 35 minutes (more than 30)  
 
 Scroll events: 6 (at least 5)  
 
 Click events: 0 
 
 Click-to-scroll ratio: 0/6 = 0.00 (less than 0.20)  
 
 Purchases: 0 (no purchases)  
 
 S001 is a zombie session (meets all criteria) 
 
 
 
 Session S002 (User 202) :
	 
 
 Duration: 11:00:00 to 11:20:00 = 20 minutes (less than 30)  
 
 Has a purchase event  
 
 S002 is not a zombie session  
 
 
 
 Session S003 (User 203) :
	 
 
 Duration: 12:00:00 to 13:00:00 = 60 minutes (more than 30)  
 
 Scroll events: 5 (at least 5)  
 
 Click events: 1 
 
 Click-to-scroll ratio: 1/5 = 0.20 (not less than 0.20)  
 
 Purchases: 0 (no purchases)  
 
 S003 is not a zombie session (click-to-scroll ratio equals 0.20, needs to be less) 
 
 
 
 Session S004 (User 204) :
	 
 
 Duration: 14:00:00 to 14:12:00 = 12 minutes (less than 30)  
 
 Scroll events: 2 (less than 5)  
 
 S004  is not a zombie session  
 
 
 
 
 The result table is ordered by scroll_count in descending order, then by session_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    session_id,
    user_id,
    TIMESTAMPDIFF(
        MINUTE,
        MIN(event_timestamp),
        MAX(event_timestamp)
    ) AS session_duration_minutes,
    SUM(event_type = 'scroll') AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING
    session_duration_minutes > 30
    AND scroll_count >= 5
    AND SUM(event_type = 'click') * 5 < scroll_count
    AND SUM(event_type = 'purchase') = 0
ORDER BY
    scroll_count DESC,
    session_id ASC;
```

---

## 3705. Find Golden Hour Customers

**Problem:** https://leetcode.com/problems/find-golden-hour-customers/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195614213  
**Language:** mysql

### Description

Table:  restaurant_orders 
 
```text
+------------------+----------+
| Column Name      | Type     | 
+------------------+----------+
| order_id         | int      |
| customer_id      | int      |
| order_timestamp  | datetime |
| order_amount     | decimal  |
| payment_method   | varchar  |
| order_rating     | int      |
+------------------+----------+
order_id is the unique identifier for this table.
payment_method can be cash, card, or app.
order_rating is between 1 and 5, where 5 is the best (NULL if not rated).
order_timestamp contains both date and time information.
```
 
 
 Write a solution to find  golden hour customers  - customers who consistently order during peak hours and provide high satisfaction. A customer is a  golden hour customer  if they meet ALL the following criteria: 
 
 
 Made  at least   3  orders. 
 
 At least   60%  of their orders are during  peak hours  ( 11:00 - 14:00  or  18:00 - 21:00 ). 
 
 Their  average rating  for rated orders is at least  4.0,  round it to  2  decimal places. 
 
 Have rated  at least   50%  of their orders. 
 
 
 Return  the result table ordered by   average_rating   in  descending  order, then by   customer_id ​​​​​​​  in  descending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 restaurant_orders table: 
 
```text
+----------+-------------+---------------------+--------------+----------------+--------------+
| order_id | customer_id | order_timestamp     | order_amount | payment_method | order_rating |
+----------+-------------+---------------------+--------------+----------------+--------------+
| 1        | 101         | 2024-03-01 12:30:00 | 25.50        | card           | 5            |
| 2        | 101         | 2024-03-02 19:15:00 | 32.00        | app            | 4            |
| 3        | 101         | 2024-03-03 13:45:00 | 28.75        | card           | 5            |
| 4        | 101         | 2024-03-04 20:30:00 | 41.00        | app            | NULL         |
| 5        | 102         | 2024-03-01 11:30:00 | 18.50        | cash           | 4            |
| 6        | 102         | 2024-03-02 12:00:00 | 22.00        | card           | 3            |
| 7        | 102         | 2024-03-03 15:30:00 | 19.75        | cash           | NULL         |
| 8        | 103         | 2024-03-01 19:00:00 | 55.00        | app            | 5            |
| 9        | 103         | 2024-03-02 20:45:00 | 48.50        | app            | 4            |
| 10       | 103         | 2024-03-03 18:30:00 | 62.00        | card           | 5            |
| 11       | 104         | 2024-03-01 10:00:00 | 15.00        | cash           | 3            |
| 12       | 104         | 2024-03-02 09:30:00 | 18.00        | cash           | 2            |
| 13       | 104         | 2024-03-03 16:00:00 | 20.00        | card           | 3            |
| 14       | 105         | 2024-03-01 12:15:00 | 30.00        | app            | 4            |
| 15       | 105         | 2024-03-02 13:00:00 | 35.50        | app            | 5            |
| 16       | 105         | 2024-03-03 11:45:00 | 28.00        | card           | 4            |
+----------+-------------+---------------------+--------------+----------------+--------------+
```
 
 
 Output: 
 
```text
+-------------+--------------+----------------------+----------------+
| customer_id | total_orders | peak_hour_percentage | average_rating |
+-------------+--------------+----------------------+----------------+
| 103         | 3            | 100                  | 4.67           |
| 101         | 4            | 100                  | 4.67           |
| 105         | 3            | 100                  | 4.33           |
+-------------+--------------+----------------------+----------------+
```
 
 
 Explanation: 
 
 
 Customer 101 :

	 
 
 Total orders: 4 (at least 3)  
 
 Peak hour orders: 4 out of 4 (12:30, 19:15, 13:45, and 20:30 are in peak hours) 
 
 Peak hour percentage: 100% (at least 60%)  
 
 Rated orders: 3 out of 4 (75% rating completion)  
 
 Average rating: (5+4+5)/3 = 4.67 (at least 4.0)  
 
 Result:  Golden hour customer 
 
 
 
 Customer 102 :
	 
 
 Total orders: 3 (at least 3)  
 
 Peak hour orders: 2 out of 3 (11:30, 12:00 are in peak hours; 15:30 is not) 
 
 Peak hour percentage: 2/3 = 66.67% (at least 60%)  
 
 Rated orders: 2 out of 3 (66.67% rating completion)  
 
 Average rating: (4+3)/2 = 3.5 (less than 4.0)  
 
 Result:  Not a golden hour customer  (average rating too low) 
 
 
 
 Customer 103 :
	 
 
 Total orders: 3 (at least 3)  
 
 Peak hour orders: 3 out of 3 (19:00, 20:45, 18:30 all in evening peak) 
 
 Peak hour percentage: 3/3 = 100% (at least 60%)  
 
 Rated orders: 3 out of 3 (100% rating completion)  
 
 Average rating: (5+4+5)/3 = 4.67 (at least 4.0)  
 
 Result:  Golden hour customer 
 
 
 
 Customer 104 :
	 
 
 Total orders: 3 (at least 3)  
 
 Peak hour orders: 0 out of 3 (10:00, 09:30, 16:00 all outside peak hours) 
 
 Peak hour percentage: 0/3 = 0% (less than 60%)  
 
 Result:  Not a golden hour customer  (insufficient peak hour orders) 
 
 
 
 Customer 105 :
	 
 
 Total orders: 3 (at least 3)  
 
 Peak hour orders: 3 out of 3 (12:15, 13:00, 11:45 all in lunch peak) 
 
 Peak hour percentage: 3/3 = 100% (at least 60%)  
 
 Rated orders: 3 out of 3 (100% rating completion)  
 
 Average rating: (4+5+4)/3 = 4.33 (at least 4.0)  
 
 Result:  Golden hour customer 
 
 
 
 
 The results table is ordered by average_rating DESC, then customer_id DESC.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

SELECT
    customer_id,
    COUNT(*) AS total_orders,
    ROUND(
        100 * SUM(
            TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'
            OR TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'
        ) / COUNT(*)
    ) AS peak_hour_percentage,
    ROUND(AVG(order_rating), 2) AS average_rating
FROM restaurant_orders
GROUP BY customer_id
HAVING
    COUNT(*) >= 3
    AND 5 * SUM(
        TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'
        OR TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'
    ) >= 3 * COUNT(*)
    AND AVG(order_rating) >= 4.0
    AND 2 * COUNT(order_rating) >= COUNT(*)
ORDER BY
    average_rating DESC,
    customer_id DESC;
```

---

## 3716. Find Churn Risk Customers

**Problem:** https://leetcode.com/problems/find-churn-risk-customers/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195614336  
**Language:** mysql

### Description

Table:  subscription_events 
 
```text
+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| event_id         | int     |
| user_id          | int     |
| event_date       | date    |
| event_type       | varchar |
| plan_name        | varchar |
| monthly_amount   | decimal |
+------------------+---------+
event_id is the unique identifier for this table.
event_type can be start, upgrade, downgrade, or cancel.
plan_name can be basic, standard, premium, or NULL (when event_type is cancel).
monthly_amount represents the monthly subscription cost after this event.
For cancel events, monthly_amount is 0.
```
 
 
 Write a solution to  Find Churn Risk Customers  - users who show warning signs before churning. A user is considered  churn risk customer  if they meet ALL the following criteria: 
 
 
 Currently have an  active subscription  (their last event is not cancel). 
 
 Have performed  at least one  downgrade in their subscription history. 
 
 Their  current plan revenue  is less than  50%  of their historical maximum plan revenue. 
 
 Have been a subscriber for  at least   60  days. 
 
 
 Return  the result table ordered by   days_as_subscriber   in  descending  order, then by   user_id   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 subscription_events table: 
 
```text
+----------+---------+------------+------------+-----------+----------------+
| event_id | user_id | event_date | event_type | plan_name | monthly_amount |
+----------+---------+------------+------------+-----------+----------------+
| 1        | 501     | 2024-01-01 | start      | premium   | 29.99          |
| 2        | 501     | 2024-02-15 | downgrade  | standard  | 19.99          |
| 3        | 501     | 2024-03-20 | downgrade  | basic     | 9.99           |
| 4        | 502     | 2024-01-05 | start      | standard  | 19.99          |
| 5        | 502     | 2024-02-10 | upgrade    | premium   | 29.99          |
| 6        | 502     | 2024-03-15 | downgrade  | basic     | 9.99           |
| 7        | 503     | 2024-01-10 | start      | basic     | 9.99           |
| 8        | 503     | 2024-02-20 | upgrade    | standard  | 19.99          |
| 9        | 503     | 2024-03-25 | upgrade    | premium   | 29.99          |
| 10       | 504     | 2024-01-15 | start      | premium   | 29.99          |
| 11       | 504     | 2024-03-01 | downgrade  | standard  | 19.99          |
| 12       | 504     | 2024-03-30 | cancel     | NULL      | 0.00           |
| 13       | 505     | 2024-02-01 | start      | basic     | 9.99           |
| 14       | 505     | 2024-02-28 | upgrade    | standard  | 19.99          |
| 15       | 506     | 2024-01-20 | start      | premium   | 29.99          |
| 16       | 506     | 2024-03-10 | downgrade  | basic     | 9.99           |
+----------+---------+------------+------------+-----------+----------------+
```
 
 
 Output: 
 
```text
+----------+--------------+------------------------+-----------------------+--------------------+
| user_id  | current_plan | current_monthly_amount | max_historical_amount | days_as_subscriber |
+----------+--------------+------------------------+-----------------------+--------------------+
| 501      | basic        | 9.99                   | 29.99                 | 79                 |
| 502      | basic        | 9.99                   | 29.99                 | 70                 |
+----------+--------------+------------------------+-----------------------+--------------------+
```
 
 
 Explanation: 
 
 
 User 501 :

	 
 
 Currently active: Last event is downgrade to basic (not cancelled)  
 
 Has downgrades: Yes, 2 downgrades in history  
 
 Current revenue (9.99) vs max (29.99): 9.99/29.99 = 33.3% (less than 50%)  
 
 Days as subscriber: Jan 1 to Mar 20 = 79 days (at least 60)  
 
 Result:  Churn Risk Customer 
 
 
 
 User 502 :
	 
 
 Currently active: Last event is downgrade to basic (not cancelled)  
 
 Has downgrades: Yes, 1 downgrade in history  
 
 Current revenue (9.99) vs max (29.99): 9.99/29.99 = 33.3% (less than 50%)  
 
 Days as subscriber: Jan 5 to Mar 15 = 70 days (at least 60)  
 
 Result:  Churn Risk Customer 
 
 
 
 User 503 :
	 
 
 Currently active: Last event is upgrade to premium (not cancelled)  
 
 Has downgrades: No downgrades in history  
 
 Result:  Not at-risk  (no downgrade history) 
 
 
 
 User 504 :
	 
 
 Currently active: Last event is cancel 
 
 Result:  Not at-risk  (subscription cancelled) 
 
 
 
 User 505 :
	 
 
 Currently active: Last event is 'upgrade' to standard (not cancelled)  
 
 Has downgrades: No downgrades in history  
 
 Result:  Not at-risk  (no downgrade history) 
 
 
 
 User 506 :
	 
 
 Currently active: Last event is downgrade to basic (not cancelled)  
 
 Has downgrades: Yes, 1 downgrade in history  
 
 Current revenue (9.99) vs max (29.99): 9.99/29.99 = 33.3% (less than 50%)  
 
 Days as subscriber: Jan 20 to Mar 10 = 50 days (less than 60)  
 
 Result:  Not at-risk  (insufficient subscription duration) 
 
 
 
 
 Result table is ordered by days_as_subscriber DESC, then user_id ASC. 
 
 Note:  days_as_subscriber is calculated from the first event date to the last event date for each user.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH RankedEvents AS (
    SELECT
        user_id,
        event_type,
        plan_name,
        monthly_amount,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC, event_id DESC
        ) AS rn
    FROM subscription_events
),
UserStats AS (
    SELECT
        user_id,
        MAX(monthly_amount) AS max_historical_amount,
        MIN(event_date) AS first_date,
        MAX(event_date) AS last_date,
        SUM(event_type = 'downgrade') AS downgrade_count
    FROM subscription_events
    GROUP BY user_id
)
SELECT
    r.user_id,
    r.plan_name AS current_plan,
    r.monthly_amount AS current_monthly_amount,
    s.max_historical_amount,
    DATEDIFF(s.last_date, s.first_date) AS days_as_subscriber
FROM RankedEvents r
JOIN UserStats s
    ON r.user_id = s.user_id
WHERE r.rn = 1
  AND r.event_type <> 'cancel'
  AND s.downgrade_count >= 1
  AND r.monthly_amount * 2 < s.max_historical_amount
  AND DATEDIFF(s.last_date, s.first_date) >= 60
ORDER BY
    days_as_subscriber DESC,
    r.user_id ASC;
```

---

## 3764. Most Common Course Pairs

**Problem:** https://leetcode.com/problems/most-common-course-pairs/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195614458  
**Language:** mysql

### Description

Table:  course_completions 
 
```text
+-------------------+---------+
| Column Name       | Type    | 
+-------------------+---------+
| user_id           | int     |
| course_id         | int     |
| course_name       | varchar |
| completion_date   | date    |
| course_rating     | int     |
+-------------------+---------+
(user_id, course_id) is the combination of columns with unique values for this table.
Each row represents a completed course by a user with their rating (1-5 scale).
```
 
 
 Write a solution to identify  skill mastery pathways  by analyzing course completion sequences among top-performing students: 
 
 
 Consider only  top-performing students  (those who completed  at least  5  courses  with an  average rating of  4  or higher ). 
 
 For each top performer, identify the  sequence of courses  they completed in chronological order. 
 
 Find all  consecutive course pairs  ( Course A → Course B ) taken by these students. 
 
 Return the  pair frequency , identifying which course transitions are most common among high achievers. 
 
 
 Return  the result table ordered by   pair frequency in  descending  order   and then by first course name and second course name in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 course_completions table: 
 
```text
+---------+-----------+------------------+-----------------+---------------+
| user_id | course_id | course_name      | completion_date | course_rating |
+---------+-----------+------------------+-----------------+---------------+
| 1       | 101       | Python Basics    | 2024-01-05      | 5             |
| 1       | 102       | SQL Fundamentals | 2024-02-10      | 4             |
| 1       | 103       | JavaScript       | 2024-03-15      | 5             |
| 1       | 104       | React Basics     | 2024-04-20      | 4             |
| 1       | 105       | Node.js          | 2024-05-25      | 5             |
| 1       | 106       | Docker           | 2024-06-30      | 4             |
| 2       | 101       | Python Basics    | 2024-01-08      | 4             |
| 2       | 104       | React Basics     | 2024-02-14      | 5             |
| 2       | 105       | Node.js          | 2024-03-20      | 4             |
| 2       | 106       | Docker           | 2024-04-25      | 5             |
| 2       | 107       | AWS Fundamentals | 2024-05-30      | 4             |
| 3       | 101       | Python Basics    | 2024-01-10      | 3             |
| 3       | 102       | SQL Fundamentals | 2024-02-12      | 3             |
| 3       | 103       | JavaScript       | 2024-03-18      | 3             |
| 3       | 104       | React Basics     | 2024-04-22      | 2             |
| 3       | 105       | Node.js          | 2024-05-28      | 3             |
| 4       | 101       | Python Basics    | 2024-01-12      | 5             |
| 4       | 108       | Data Science     | 2024-02-16      | 5             |
| 4       | 109       | Machine Learning | 2024-03-22      | 5             |
+---------+-----------+------------------+-----------------+---------------+
```
 
 
 Output: 
 
```text
+------------------+------------------+------------------+
| first_course     | second_course    | transition_count |
+------------------+------------------+------------------+
| Node.js          | Docker           | 2                |
| React Basics     | Node.js          | 2                |
| Docker           | AWS Fundamentals | 1                |
| JavaScript       | React Basics     | 1                |
| Python Basics    | React Basics     | 1                |
| Python Basics    | SQL Fundamentals | 1                |
| SQL Fundamentals | JavaScript       | 1                |
+------------------+------------------+------------------+
```
 
 
 Explanation: 
 
 
 User 1 : Completed 6 courses with average rating 4.5 (qualifies as top performer) 
 
 User 2 : Completed 5 courses with average rating 4.4 (qualifies as top performer) 
 
 User 3 : Completed 5 courses but average rating is 2.8 (does not qualify) 
 
 User 4 : Completed only 3 courses (does not qualify) 
 
 Course Pairs Among Top Performers :
	 
 
 User 1: Python Basics → SQL Fundamentals → JavaScript → React Basics → Node.js → Docker 
 
 User 2: Python Basics → React Basics → Node.js → Docker → AWS Fundamentals 
 
 Most common transitions: Node.js → Docker (2 times), React Basics → Node.js (2 times) 
 
 
 
 
 Results are ordered by transition_count in descending order, then by first_course in ascending order, and then by second_course in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH TopStudents AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5
       AND AVG(course_rating) >= 4
),
CoursePairs AS (
    SELECT
        c.course_name AS first_course,
        LEAD(c.course_name) OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date, c.course_id
        ) AS second_course
    FROM course_completions c
    JOIN TopStudents t
        ON c.user_id = t.user_id
)
SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM CoursePairs
WHERE second_course IS NOT NULL
GROUP BY first_course, second_course
ORDER BY
    transition_count DESC,
    first_course ASC,
    second_course ASC;
```

---

## 3793. Find Users with High Token Usage

**Problem:** https://leetcode.com/problems/find-users-with-high-token-usage/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195524309  
**Language:** mysql

### Description

Table:  prompts 
 
```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| prompt      | varchar |
| tokens      | int     |
+-------------+---------+
(user_id, prompt) is the primary key (unique value) for this table.
Each row represents a prompt submitted by a user to an AI system along with the number of tokens consumed.
```
 
 
 Write a solution to analyze  AI prompt usage patterns  based on the following requirements: 
 
 
 For each user, calculate the  total number of prompts  they have submitted. 
 
 For each user, calculate the  average tokens used per prompt  (Rounded to  2  decimal places). 
 
 Only include users who have submitted  at least  3  prompts . 
 
 Only include users who have submitted  at least one prompt  with  tokens   greater than  their own average token usage. 
 
 
 Return  the result table ordered by  average tokens  in  descending  order, and then by  user_id  in  ascending  order. 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 prompts table: 
 
```text
+---------+--------------------------+--------+
| user_id | prompt                   | tokens |
+---------+--------------------------+--------+
| 1       | Write a blog outline     | 120    |
| 1       | Generate SQL query       | 80     |
| 1       | Summarize an article     | 200    |
| 2       | Create resume bullet     | 60     |
| 2       | Improve LinkedIn bio     | 70     |
| 3       | Explain neural networks  | 300    |
| 3       | Generate interview Q&A   | 250    |
| 3       | Write cover letter       | 180    |
| 3       | Optimize Python code     | 220    |
+---------+--------------------------+--------+
```
 
 
 Output: 
 
```text
+---------+---------------+------------+
| user_id | prompt_count  | avg_tokens |
+---------+---------------+------------+
| 3       | 4             | 237.5      |
| 1       | 3             | 133.33     |
+---------+---------------+------------+
```
 
 
 Explanation: 
 
 
 User 1 :

	 
 
 Total prompts = 3 
 
 Average tokens = (120 + 80 + 200) / 3 = 133.33 
 
 Has a prompt with 200 tokens, which is greater than the average 
 
 Included in the result 
 
 
 
 User 2 :
	 
 
 Total prompts = 2 (less than the required minimum) 
 
 Excluded from the result 
 
 
 
 User 3 :
	 
 
 Total prompts = 4 
 
 Average tokens = (300 + 250 + 180 + 220) / 4 = 237.5 
 
 Has prompts with 300 and 250 tokens, both greater than the average 
 
 Included in the result 
 
 
 
 
 The Results table is ordered by avg_tokens in descending order, then by user_id in ascending order

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH stats AS (
 SELECT user_id,COUNT(*) AS prompt_count,AVG(tokens) AS avg_tokens,MAX(tokens) AS max_tokens
 FROM prompts GROUP BY user_id
)
SELECT user_id,prompt_count,ROUND(avg_tokens,2) AS avg_tokens
FROM stats WHERE prompt_count>=3 AND max_tokens>avg_tokens
ORDER BY avg_tokens DESC,user_id;
```

---

## 3808. Find Emotionally Consistent Users

**Problem:** https://leetcode.com/problems/find-emotionally-consistent-users/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195614570  
**Language:** mysql

### Description

Table:  reactions 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| content_id   | int     |
| reaction     | varchar |
+--------------+---------+
(user_id, content_id) is the primary key (unique value) for this table.
Each row represents a reaction given by a user to a piece of content.
```
 
 
 Write a solution to identify  emotionally consistent users  based on the following requirements: 
 
 
 For each user, count the total number of reactions they have given. 
 
 Only include users who have reacted to  at least  5  different content items . 
 
 A user is considered  emotionally consistent  if  at least  60%  of their reactions are of the  same type . 
 
 
 Return  the result table ordered by   reaction_ratio   in  descending  order and then by   user_id   in  ascending  order . 
 
 Note: 
 
 
 reaction_ratio  should be rounded to  2  decimal places 
 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 reactions table: 
 
```text
+---------+------------+----------+
| user_id | content_id | reaction |
+---------+------------+----------+
| 1       | 101        | like     |
| 1       | 102        | like     |
| 1       | 103        | like     |
| 1       | 104        | wow      |
| 1       | 105        | like     |
| 2       | 201        | like     |
| 2       | 202        | wow      |
| 2       | 203        | sad      |
| 2       | 204        | like     |
| 2       | 205        | wow      |
| 3       | 301        | love     |
| 3       | 302        | love     |
| 3       | 303        | love     |
| 3       | 304        | love     |
| 3       | 305        | love     |
+---------+------------+----------+
```
 
 
 Output: 
 
```text
+---------+-------------------+----------------+
| user_id | dominant_reaction | reaction_ratio |
+---------+-------------------+----------------+
| 3       | love              | 1.00           |
| 1       | like              | 0.80           |
+---------+-------------------+----------------+
```
 
 
 Explanation: 
 
 
 User 1 :

	 
 
 Total reactions = 5 
 
 like appears 4 times 
 
 reaction_ratio = 4 / 5 = 0.80 
 
 Meets the 60% consistency requirement 
 
 
 
 User 2 :
	 
 
 Total reactions = 5 
 
 Most frequent reaction appears only 2 times 
 
 reaction_ratio = 2 / 5 = 0.40 
 
 Does not meet the consistency requirement 
 
 
 
 User 3 :
	 
 
 Total reactions = 5 
 
 'love' appears 5 times 
 
 reaction_ratio = 5 / 5 = 1.00 
 
 Meets the consistency requirement 
 
 
 
 
 The Results table is ordered by reaction_ratio in descending order, then by user_id in ascending order.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
# Write your MySQL query statement below

WITH ReactionCounts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS cnt
    FROM reactions
    GROUP BY user_id, reaction
),
UserStats AS (
    SELECT
        user_id,
        MAX(cnt) AS max_count,
        SUM(cnt) AS total_count
    FROM ReactionCounts
    GROUP BY user_id
    HAVING SUM(cnt) >= 5
       AND 5 * MAX(cnt) >= 3 * SUM(cnt)
)
SELECT
    r.user_id,
    r.reaction AS dominant_reaction,
    ROUND(r.cnt / u.total_count, 2) AS reaction_ratio
FROM ReactionCounts r
JOIN UserStats u
    ON r.user_id = u.user_id
   AND r.cnt = u.max_count
ORDER BY
    reaction_ratio DESC,
    r.user_id ASC;
```

---

## 3832. Find Users with Persistent Behavior Patterns

**Problem:** https://leetcode.com/problems/find-users-with-persistent-behavior-patterns/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195525174  
**Language:** mysql

### Description

Table:  activity 
 
```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| action_date  | date    |
| action       | varchar |
+--------------+---------+
(user_id, action_date, action) is the primary key (unique value) for this table.
Each row represents a user performing a specific action on a given date.
```
 
 
 Write a solution to identify  behaviorally stable users  based on the following definition: 
 
 
 A user is considered  behaviorally stable  if there exists a sequence of  at least  5  consecutive days  such that:

	 
 
 The user performed  exactly one action per day  during that period. 
 
 The  action is the same  on all those consecutive days. 
 
 
 
 If a user has multiple qualifying sequences, only consider the sequence with the  maximum length . 
 
 If multiple qualifying sequences have the same maximum length, consider the sequence with the  lexicographically smallest action . If there is still a tie, consider the sequence with the  latest start date . 
 
 
 Return  the result table ordered by   streak_length   in  descending  order ,  then by  user_id   in  ascending  order . 
 
 The result format is in the following example. 
 
   
 
 Example: 
 
 
 Input: 
 
 activity table: 
 
```text
+---------+-------------+--------+
| user_id | action_date | action |
+---------+-------------+--------+
| 1       | 2024-01-01  | login  |
| 1       | 2024-01-02  | login  |
| 1       | 2024-01-03  | login  |
| 1       | 2024-01-04  | login  |
| 1       | 2024-01-05  | login  |
| 1       | 2024-01-06  | logout |
| 2       | 2024-01-01  | click  |
| 2       | 2024-01-02  | click  |
| 2       | 2024-01-03  | click  |
| 2       | 2024-01-04  | click  |
| 3       | 2024-01-01  | view   |
| 3       | 2024-01-02  | view   |
| 3       | 2024-01-03  | view   |
| 3       | 2024-01-04  | view   |
| 3       | 2024-01-05  | view   |
| 3       | 2024-01-06  | view   |
| 3       | 2024-01-07  | view   |
+---------+-------------+--------+
```
 
 
 Output: 
 
```text
+---------+--------+---------------+------------+------------+
| user_id | action | streak_length | start_date | end_date   |
+---------+--------+---------------+------------+------------+
| 3       | view   | 7             | 2024-01-01 | 2024-01-07 |
| 1       | login  | 5             | 2024-01-01 | 2024-01-05 |
+---------+--------+---------------+------------+------------+
```
 
 
 Explanation: 
 
 
 User 1 :

	 
 
 Performed  login  from 2024-01-01 to 2024-01-05 on consecutive days 
 
 Each day has exactly one action, and the action is the same 
 
 Streak length = 5 (meets minimum requirement) 
 
 The action changes on 2024-01-06, ending the streak 
 
 
 
 User 2 :
	 
 
 Performed  click  for only 4 consecutive days 
 
 Does not meet the minimum streak length of 5 
 
 Excluded from the result 
 
 
 
 User 3 :
	 
 
 Performed  view  for 7 consecutive days 
 
 This is the longest valid sequence for this user 
 
 Included in the result 
 
 
 
 
 The Results table is ordered by streak_length in descending order, then by user_id in ascending order

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```mysql
WITH daily AS (
 SELECT user_id,action_date,MIN(action) AS action
 FROM activity GROUP BY user_id,action_date HAVING COUNT(*)=1
), numbered AS (
 SELECT *,ROW_NUMBER() OVER (PARTITION BY user_id,action ORDER BY action_date) AS rn
 FROM daily
), islands AS (
 SELECT user_id,action,MIN(action_date) AS start_date,MAX(action_date) AS end_date,
 COUNT(*) AS streak_length
 FROM (SELECT *,DATE_SUB(action_date,INTERVAL rn DAY) AS grp FROM numbered) x
 GROUP BY user_id,action,grp HAVING COUNT(*)>=5
), ranked AS (
 SELECT *,ROW_NUMBER() OVER (PARTITION BY user_id
 ORDER BY streak_length DESC,action,start_date DESC) AS rnk FROM islands
)
SELECT user_id,action,streak_length,start_date,end_date FROM ranked WHERE rnk=1
ORDER BY streak_length DESC,user_id;
```

---
