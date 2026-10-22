# 0x01. NoSQL with MongoDB

## Description
This module covers non-relational document databases using **MongoDB** and the **PyMongo** Python client.

## Learning Objectives
- Understanding Document Database models vs Relational Database models.
- CRUD operations in MongoDB CLI (`show dbs`, `use`, `insert`, `find`, `update`, `remove`).
- Writing Python scripts with `pymongo` to interface with MongoDB.
- Querying with complex filters, projection, and regex matching.
- Aggregating metrics over large document datasets (e.g. Nginx access logs).

## Tasks Summary

| File | Description |
| :--- | :--- |
| `0-list_databases` | Script listing all MongoDB databases. |
| `1-use_or_create_database` | Command switching to or creating database `my_db`. |
| `2-insert` | Script inserting a document into collection `school`. |
| `3-all` | Script displaying all documents in `school`. |
| `4-match` | Script matching documents with `name="Holberton school"`. |
| `5-count` | Script counting documents in collection `school`. |
| `6-update` | Script adding an `address` field to a specific school document. |
| `7-delete` | Script deleting all documents matching `name="Holberton school"`. |
| `8-all.py` | Python function `list_all(mongo_collection)` listing all documents in a collection. |
| `9-insert_school.py` | Python function inserting a document based on `**kwargs`. |
| `10-update_topics.py` | Python function updating topics array for a school by name. |
| `11-schools_by_topic.py` | Python function returning list of schools having a specific topic. |
| `12-log_stats.py` | Python script providing analytics on Nginx logs collection (methods count, status checks). |

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
