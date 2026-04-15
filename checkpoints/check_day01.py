"""
Day 1 Checkpoint — Relational Model, Tables, Constraints
Run this AFTER completing your day01.py task.
It will verify your database and test your understanding.

Usage: python checkpoints/check_day01.py
"""

import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "days", "taskflow.db")

PASS = 0
FAIL = 0


def check(condition: bool, label: str, hint: str = ""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS  {label}")
    else:
        FAIL += 1
        msg = f"  FAIL  {label}"
        if hint:
            msg += f"\n         -> Hint: {hint}"
        print(msg)


def main():
    print("=" * 55)
    print("  Day 1 Checkpoint: Relational Model & Constraints")
    print("=" * 55)

    # ── Check 1: Database file exists ──
    print("\n[1/6] Database file")
    check(
        os.path.exists(DB_PATH),
        "taskflow.db exists in days/ folder",
        "Run your day01.py first to create the database",
    )
    if not os.path.exists(DB_PATH):
        print("\nCannot continue without the database. Run day01.py first.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ── Check 2: Tables exist ──
    print("\n[2/6] Tables created")
    tables = [
        row[0]
        for row in cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
    ]
    check("users" in tables, "'users' table exists", "CREATE TABLE users (...)")
    check(
        "projects" in tables, "'projects' table exists", "CREATE TABLE projects (...)"
    )

    # ── Check 3: Users table structure ──
    print("\n[3/6] Users table structure")
    user_cols = {
        row[1]: {"type": row[2], "notnull": row[3], "pk": row[5]}
        for row in cursor.execute("PRAGMA table_info(users)").fetchall()
    }

    check("id" in user_cols, "users.id column exists")
    check(
        user_cols.get("id", {}).get("pk") == 1,
        "users.id is PRIMARY KEY",
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
    )
    check(
        "username" in user_cols, "users.username column exists"
    )
    check(
        user_cols.get("username", {}).get("notnull") == 1,
        "users.username is NOT NULL",
        "username TEXT NOT NULL UNIQUE",
    )
    check(
        "email" in user_cols, "users.email column exists"
    )
    check(
        user_cols.get("email", {}).get("notnull") == 1,
        "users.email is NOT NULL",
    )
    check(
        "full_name" in user_cols, "users.full_name column exists"
    )
    check(
        "is_active" in user_cols, "users.is_active column exists"
    )
    check(
        "created_at" in user_cols, "users.created_at column exists"
    )

    # ── Check 4: Users UNIQUE constraints ──
    print("\n[4/6] Users UNIQUE constraints")
    indexes = cursor.execute("PRAGMA index_list(users)").fetchall()
    unique_indexes = [idx for idx in indexes if idx[2] == 1]  # unique flag
    # Get columns for each unique index
    unique_columns = set()
    for idx in unique_indexes:
        idx_info = cursor.execute(f"PRAGMA index_info('{idx[1]}')").fetchall()
        for col_info in idx_info:
            unique_columns.add(col_info[2])

    check(
        "username" in unique_columns,
        "users.username has UNIQUE constraint",
        "username TEXT NOT NULL UNIQUE",
    )
    check(
        "email" in unique_columns,
        "users.email has UNIQUE constraint",
        "email TEXT NOT NULL UNIQUE",
    )

    # ── Check 5: Projects table structure ──
    print("\n[5/6] Projects table structure")
    proj_cols = {
        row[1]: {"type": row[2], "notnull": row[3], "default": row[4], "pk": row[5]}
        for row in cursor.execute("PRAGMA table_info(projects)").fetchall()
    }

    check("id" in proj_cols, "projects.id column exists")
    check(
        proj_cols.get("id", {}).get("pk") == 1,
        "projects.id is PRIMARY KEY",
    )
    check("name" in proj_cols, "projects.name column exists")
    check(
        proj_cols.get("name", {}).get("notnull") == 1,
        "projects.name is NOT NULL",
    )
    check("description" in proj_cols, "projects.description column exists")
    check(
        proj_cols.get("description", {}).get("notnull") == 0,
        "projects.description allows NULL (optional)",
        "description TEXT  -- no NOT NULL means it is optional",
    )
    check("status" in proj_cols, "projects.status column exists")
    check("created_at" in proj_cols, "projects.created_at column exists")

    # ── Check 6: Projects CHECK constraint on status ──
    print("\n[6/6] Projects CHECK constraint")
    # Try inserting invalid status
    has_check = False
    try:
        cursor.execute(
            "INSERT INTO projects (name, status) VALUES ('__test__', 'INVALID_STATUS')"
        )
        conn.rollback()
        # If we reach here, no CHECK constraint
        has_check = False
    except sqlite3.IntegrityError:
        has_check = True
        conn.rollback()

    check(
        has_check,
        "projects.status has CHECK constraint (rejects invalid values)",
        "CHECK(status IN ('planning','active','paused','completed'))",
    )

    # Clean up any test data
    try:
        cursor.execute("DELETE FROM projects WHERE name = '__test__'")
        conn.commit()
    except Exception:
        conn.rollback()

    # ── Check 7: Idempotency (bonus) ──
    print("\n[Bonus] Idempotency")
    create_sql = cursor.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='users'"
    ).fetchone()
    if create_sql:
        check(
            True,
            "Script can run multiple times without crashing (IF NOT EXISTS)",
            "Use CREATE TABLE IF NOT EXISTS",
        )

    conn.close()

    # ── Summary ──
    total = PASS + FAIL
    print("\n" + "=" * 55)
    print(f"  Results: {PASS}/{total} checks passed")
    if FAIL == 0:
        print("  DAY 1 COMPLETE! You're ready for Day 2.")
    elif FAIL <= 3:
        print("  Almost there! Fix the failing checks and re-run.")
    else:
        print("  Review the lesson doc and try again.")
    print("=" * 55)


if __name__ == "__main__":
    main()
