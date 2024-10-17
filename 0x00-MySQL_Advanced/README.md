# 0x00. MySQL Advanced

## Project Overview

This project focuses on advanced MySQL concepts and techniques that improve database performance and functionality. The key topics include creating tables with constraints, optimizing queries using indexes, and implementing stored procedures, views, triggers, and functions.

## Learning Objectives

- How to create tables with constraints in MySQL
- How to optimize queries by adding indexes
- What stored procedures are, and how to create and use them in MySQL
- What functions are in MySQL and how to implement them
- What views are in MySQL and how to use them effectively
- What triggers are in MySQL and how to create them

## Resources

- [MySQL Cheatsheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/expressions.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## Key Concepts

### 1. **Creating Tables with Constraints**
   - Learn how to define tables with constraints such as `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and more to ensure data integrity.

### 2. **Optimizing Queries with Indexes**
   - Understand how adding indexes can improve query performance, especially for large datasets.

### 3. **Stored Procedures and Functions**
   - Learn the differences between stored procedures and functions.
   - Implement logic that can be reused by creating procedures and functions using SQL.

### 4. **Views**
   - Create virtual tables using views to simplify complex queries.
   - Understand the advantages of using views for data abstraction.

### 5. **Triggers**
   - Implement triggers to automate actions in response to specific database events (such as `INSERT`, `UPDATE`, or `DELETE`).

## Usage Examples

### Creating a Table with Constraints:
```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

Creating an Index:
```
CREATE INDEX idx_department_name ON departments(name);
```

Creating a Stored Procedure:
```
DELIMITER //
CREATE PROCEDURE GetEmployeeByDepartment(IN dept_id INT)
BEGIN
    SELECT * FROM employees WHERE department_id = dept_id;
END //
DELIMITER ;
```

Creating a View:
```
CREATE VIEW employee_view AS
SELECT id, name, department_id FROM employees WHERE department_id IS NOT NULL;
```

Creating a Trigger:
```
CREATE TRIGGER before_employee_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    SET NEW.name = UPPER(NEW.name);
END;
```
