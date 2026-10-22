# 0x00. Advanced MySQL

## Description
This module delves into enterprise-grade relational database concepts with **MySQL 8.0**, focusing on data integrity constraints, indexing strategies, automation with triggers, and modular logic encapsulation via stored procedures and user-defined functions.

## Learning Objectives
- Creating robust relational schemas with `UNIQUE`, `NOT NULL`, and `ENUM` column constraints.
- Enhancing query execution speeds using single-column and composite indexes.
- Writing triggers to enforce automated business rules upon `INSERT`, `UPDATE`, or `DELETE`.
- Writing reusable Stored Procedures (`CREATE PROCEDURE`) and Functions (`CREATE FUNCTION`).
- Safe parameter passing and avoiding SQL injection vulnerabilities.

## Tasks Summary

| File | Description |
| :--- | :--- |
| `0-uniq_users.sql` | Creates a `users` table with unique email constraint and auto-increment ID. |
| `1-country_users.sql` | Adds country validation via `ENUM('US', 'CO', 'TN')` with default value. |
| `2-fans.sql` | Ranks country origins of metal bands ordered by number of non-unique fans. |
| `3-glam_rock.sql` | Lists Glam rock bands ranked by longevity until year 2022. |
| `4-store.sql` | Creates a trigger that automatically decreases item quantity when orders are placed. |
| `5-valid_email.sql` | Creates a trigger resetting `valid_email` flag whenever the user's email changes. |
| `6-bonus.sql` | Stored procedure `AddBonus` adding a new correction project/score for a student. |
| `7-average_score.sql` | Stored procedure `ComputeAverageScoreForUser` calculating average score of a student. |
| `100-average_weighted_score.sql` | Stored procedure `ComputeAverageWeightedScoreForUser` using project weights. |
| `101-average_weighted_score.sql` | Stored procedure `ComputeAverageWeightedScoreForUsers` computing weighted average for all users. |

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
