# Day 1: The Relational Model — Tables, Rows, Columns, Keys, Constraints

## Concepts

### What is a Relational Database?
A relational database stores data in **tables** (also called relations). Each table has:
- **Columns** (attributes) — define WHAT data is stored (name, type, constraints)
- **Rows** (tuples/records) — each row is ONE instance of the entity
- **Schema** — the structure definition (column names, types, rules)

### Primary Key (PK)
- Uniquely identifies EVERY row in a table
- Rules: Must be UNIQUE + NOT NULL
- Can be single column or composite (multiple columns)
- Convention: use `id INTEGER PRIMARY KEY` (auto-increment)

### Data Types (SQLite)
| Type | Use For | Example |
|------|---------|---------|
| INTEGER | Whole numbers, IDs, counts | `id`, `age`, `priority` |
| TEXT | Strings, names, descriptions | `name`, `email`, `status` |
| REAL | Decimal numbers | `price`, `rating` |
| BLOB | Binary data | Files, images |
| NULL | Missing/unknown value | Any column unless constrained |

> Note: SQLite is dynamically typed (flexible), but MySQL/PostgreSQL are strict.
> We start with SQLite for simplicity, then learn strict typing in Phase 2.

### Constraints — Rules That Protect Your Data
| Constraint | What It Does | Example |
|------------|-------------|---------|
| PRIMARY KEY | Unique identifier for each row | `id INTEGER PRIMARY KEY` |
| NOT NULL | Column cannot be empty | `name TEXT NOT NULL` |
| UNIQUE | No duplicate values in this column | `email TEXT UNIQUE` |
| DEFAULT | Auto-fill if no value given | `status TEXT DEFAULT 'active'` |
| CHECK | Custom validation rule | `CHECK(priority BETWEEN 1 AND 5)` |

### CREATE TABLE Syntax
```sql
CREATE TABLE table_name (
    column1  TYPE  CONSTRAINTS,
    column2  TYPE  CONSTRAINTS,
    ...
);
```

### Real Example
```sql
CREATE TABLE users (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    username   TEXT    NOT NULL UNIQUE,
    email      TEXT    NOT NULL UNIQUE,
    full_name  TEXT    NOT NULL,
    is_active  INTEGER NOT NULL DEFAULT 1,   -- SQLite has no BOOLEAN, use 0/1
    created_at TEXT    NOT NULL DEFAULT (datetime('now'))
);
```

### Python's sqlite3 Module — The Basics
```python
import sqlite3

# 1. Connect (creates file if not exists)
conn = sqlite3.connect("taskflow.db")

# 2. Get a cursor (executes SQL)
cursor = conn.cursor()

# 3. Execute SQL
cursor.execute("CREATE TABLE ...")

# 4. Commit changes (SAVE to disk)
conn.commit()

# 5. Close when done
conn.close()
```

### Key Concept: Why Constraints Matter
Without constraints, your database accepts garbage:
- A user with no name? Allowed without NOT NULL
- Two users with same email? Allowed without UNIQUE
- Priority of 999? Allowed without CHECK

**Constraints are your first line of defense for data integrity.**

---

## Your Task — Build It Yourself

### Task 1: Create the `users` table
Create a file `days/day01.py` that:
1. Connects to `taskflow.db`
2. Creates a `users` table with these columns:
   - `id` — auto-incrementing primary key
   - `username` — required, unique
   - `email` — required, unique
   - `full_name` — required
   - `is_active` — integer (0 or 1), default 1
   - `created_at` — auto-set to current timestamp

### Task 2: Create the `projects` table
In the same file, also create:
- `id` — auto-incrementing primary key
- `name` — required, unique
- `description` — optional (can be NULL)
- `status` — must be one of: 'planning', 'active', 'paused', 'completed' (use CHECK)
- `created_at` — auto-set to current timestamp

### Task 3: Verify your tables
After creating both tables, write code that:
- Queries `sqlite_master` to list all tables
- Prints the schema of each table
- Prints "Tables created successfully!" if both exist

### Bonus Challenge
- What happens if you run the script twice? Fix it so it doesn't crash.
  (Hint: `CREATE TABLE IF NOT EXISTS`)
- Add a CHECK constraint on `users.is_active` to only allow 0 or 1

### Expected Output
```
=== TaskFlow Database Setup ===
Creating users table...
Creating projects table...

=== Verification ===
Tables found: ['users', 'projects']

Schema for 'users':
  id INTEGER PRIMARY KEY AUTOINCREMENT
  username TEXT NOT NULL UNIQUE
  ...

Schema for 'projects':
  ...

All tables created successfully!
```

---

## Hints (only look if stuck)

<details>
<summary>Hint 1: sqlite3 connect</summary>
`conn = sqlite3.connect("days/taskflow.db")` — put the DB file in the days folder
</details>

<details>
<summary>Hint 2: CHECK constraint for status</summary>
`status TEXT NOT NULL DEFAULT 'planning' CHECK(status IN ('planning','active','paused','completed'))`
</details>

<details>
<summary>Hint 3: List all tables</summary>
`cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()`
</details>

<details>
<summary>Hint 4: Get table schema</summary>
`cursor.execute("PRAGMA table_info(users)").fetchall()` returns column details
</details>
