"""
Day 1: Relational Model — Tables, Primary Keys, Constraints
============================================================
Project: TaskFlow

YOUR TASK:
1. Create the 'users' table with proper columns and constraints
2. Create the 'projects' table with a CHECK constraint on status
3. Verify both tables were created

Read: docs/day01-relational-model.md for the full lesson

When done, run: python checkpoints/check_day01.py
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "taskflow.db")


def create_database():
    # Step 1: Connect to database (creates taskflow.db if not exists)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("=== TaskFlow Database Setup ===\n")

    # ── Step 2: Create users table ──
    # TODO: Write your CREATE TABLE statement for users
    # Columns needed:
    #   id         - auto-incrementing primary key
    #   username   - required, must be unique
    #   email      - required, must be unique
    #   full_name  - required
    #   is_active  - integer (0 or 1), default 1
    #   created_at - auto-set to current timestamp

    print("Creating users table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            full_name TEXT NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)

    # ── Step 3: Create projects table ──
    # TODO: Write your CREATE TABLE statement for projects
    # Columns needed:
    #   id          - auto-incrementing primary key
    #   name        - required, must be unique
    #   description - optional (can be NULL)
    #   status      - must be one of: 'planning', 'active', 'paused', 'completed'
    #   created_at  - auto-set to current timestamp

    print("Creating projects table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'planning' CHECK(status IN ('planning', 'active', 'paused', 'completed')),
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)

    # ── Step 4: Save changes ──
    conn.commit()

    # ── Step 5: Verify ──
    print("\n=== Verification ===")

    # TODO: Query sqlite_master to get all table names
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print(f"Tables found: {[t[0] for t in tables]}")

    # TODO: For each table, print its schema using PRAGMA table_info(table_name)
    user_columns = cursor.execute("PRAGMA table_info(users)").fetchall()
    print(user_columns)

    conn.close()
    print("\nDone!")


if __name__ == "__main__":
    create_database()
