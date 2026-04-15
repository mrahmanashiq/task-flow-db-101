# TaskFlow — SQL & Database Mastery Learning Plan

> Project-based learning: Build a task management system from scratch
> Start: Raw Python + Raw SQL | End: FastAPI + ORM + Distributed Systems

---

## Phase 1: Raw Python + Raw SQL + SQLite (Days 1–15)

| Day | Topic | Status |
|-----|-------|--------|
| 1   | Relational model — tables, PK, constraints, CREATE TABLE | [ ] |
| 2   | DML — INSERT, SELECT, UPDATE, DELETE, filtering, sorting | [ ] |
| 3   | Foreign keys, one-to-many relationships | [ ] |
| 4   | JOINs — INNER, LEFT, self-join | [ ] |
| 5   | Aggregations — GROUP BY, HAVING, COUNT/SUM/AVG | [ ] |
| 6   | Many-to-many, junction tables | [ ] |
| 7   | Subqueries — scalar, correlated, IN/EXISTS | [ ] |
| 8   | NULL semantics, 3-valued logic, COALESCE, CASE | [ ] |
| 9   | CTEs + recursive CTEs | [ ] |
| 10  | Window functions — ROW_NUMBER, RANK, LAG/LEAD | [ ] |
| 11  | Set operations + time-based queries | [ ] |
| 12  | Indexes + EXPLAIN query plans | [ ] |
| 13  | Transactions — BEGIN/COMMIT/ROLLBACK | [ ] |
| 14  | Schema design review — normalization (1NF–3NF) | [ ] |
| 15  | Capstone CLI app — full TaskFlow with reports | [ ] |

## Phase 2: MySQL/PostgreSQL (Days 16–22)

| Day | Topic | Status |
|-----|-------|--------|
| 16  | MySQL setup, migrate schema, dialect differences | [ ] |
| 17  | Isolation levels — dirty/phantom read experiments | [ ] |
| 18  | Locking — row locks, deadlock simulation | [ ] |
| 19  | Stored procedures + triggers | [ ] |
| 20  | JSON columns, indexing JSON paths | [ ] |
| 21  | Security — roles, grants, SQL injection prevention | [ ] |
| 22  | Backup/restore, EXPLAIN ANALYZE deep-dive | [ ] |

## Phase 3: Python + ORM + FastAPI (Days 23–32)

| Day | Topic | Status |
|-----|-------|--------|
| 23  | SQLAlchemy Core — Engine, Connection, raw SQL via SA | [ ] |
| 24  | SQLAlchemy ORM — models, sessions, CRUD | [ ] |
| 25  | Relationships — lazy vs eager, N+1 problem | [ ] |
| 26  | Alembic migrations — init, auto-generate, rollback | [ ] |
| 27  | Repository pattern + Unit of Work | [ ] |
| 28  | FastAPI + SQLAlchemy integration | [ ] |
| 29  | Pagination — offset vs keyset, filtering API | [ ] |
| 30  | Transactions in FastAPI — middleware, DI | [ ] |
| 31  | Advanced ORM queries — window functions, CTEs in SA | [ ] |
| 32  | Testing — fixtures, test DB, factory pattern | [ ] |

## Phase 4: Scaling & NoSQL (Days 33–40)

| Day | Topic | Status |
|-----|-------|--------|
| 33  | Partitioning — range/hash on task history | [ ] |
| 34  | Replication — leader-follower setup | [ ] |
| 35  | Redis — caching, session store, rate limiting | [ ] |
| 36  | MongoDB — document modeling | [ ] |
| 37  | Polyglot persistence — right store per use case | [ ] |
| 38  | ETL basics — materialized views, star schema | [ ] |
| 39  | Multi-tenant schema design | [ ] |
| 40  | Capstone — production-ready TaskFlow | [ ] |
