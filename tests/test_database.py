import sqlite3
from pathlib import Path
DB_PATH=Path('database/app.db')
def test_users_table_exists():
 assert DB_PATH.exists();c=sqlite3.connect(DB_PATH);tables=c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'").fetchall();c.close();assert tables==[('users',)]
def test_user_records_have_required_fields():
 c=sqlite3.connect(DB_PATH);rows=c.execute('SELECT id,name,email FROM users').fetchall();c.close();assert len(rows)>=2
 for uid,name,email in rows: assert uid is not None and name and email
