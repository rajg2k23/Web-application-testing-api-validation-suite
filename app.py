from flask import Flask, jsonify, request, render_template_string
import sqlite3
from pathlib import Path
app=Flask(__name__); DB_DIR=Path('database'); DB_DIR.mkdir(exist_ok=True); DB_PATH=DB_DIR/'app.db'
HTML='''<!doctype html><html><head><title>QA Demo Application</title><style>body{font-family:Arial;max-width:800px;margin:40px auto}input,button{padding:10px;margin:5px 0}.card{border:1px solid #ddd;padding:15px;margin:10px 0;border-radius:8px}</style></head><body><h1>QA Demo Application</h1><p id="status">Application is running.</p><h2>Create User</h2><form id="user-form"><input id="name" placeholder="Name" required><input id="email" type="email" placeholder="Email" required><button type="submit">Create User</button></form><div id="message"></div><h2>Users</h2><div id="users"></div><script>async function loadUsers(){const r=await fetch('/api/users');const u=await r.json();document.getElementById('users').innerHTML=u.map(x=>`<div class="card" data-user-id="${x.id}"><strong>${x.name}</strong><br>${x.email}</div>`).join('')}document.getElementById('user-form').addEventListener('submit',async e=>{e.preventDefault();const r=await fetch('/api/users',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:document.getElementById('name').value,email:document.getElementById('email').value})});const d=await r.json();document.getElementById('message').textContent=r.ok?'User created successfully':d.error;if(r.ok){e.target.reset();loadUsers()}});loadUsers();</script></body></html>'''
def conn():
 c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c
def init_db():
 c=conn(); c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL UNIQUE)');
 if c.execute('SELECT COUNT(*) FROM users').fetchone()[0]==0:c.executemany('INSERT INTO users(name,email) VALUES(?,?)',[('Test User','test@example.com'),('Demo User','demo@example.com')])
 c.commit();c.close()
@app.route('/')
def home():return render_template_string(HTML)
@app.route('/api/health')
def health():return jsonify(status='ok')
@app.route('/api/users',methods=['GET'])
def users():
 c=conn(); rows=c.execute('SELECT id,name,email FROM users ORDER BY id').fetchall(); c.close(); return jsonify([dict(r) for r in rows])
@app.route('/api/users/<int:user_id>')
def user(user_id):
 c=conn(); r=c.execute('SELECT id,name,email FROM users WHERE id=?',(user_id,)).fetchone();c.close()
 return (jsonify(dict(r)),200) if r else (jsonify(error='User not found'),404)
@app.route('/api/users',methods=['POST'])
def create():
 d=request.get_json(silent=True) or {}; name=str(d.get('name','')).strip(); email=str(d.get('email','')).strip()
 if not name or not email:return jsonify(error='name and email are required'),400
 c=conn()
 try:
  cur=c.execute('INSERT INTO users(name,email) VALUES(?,?)',(name,email));c.commit();return jsonify(id=cur.lastrowid,name=name,email=email),201
 except sqlite3.IntegrityError:return jsonify(error='email already exists'),409
 finally:c.close()
if __name__=='__main__':init_db();app.run(host='127.0.0.1',port=5000,debug=False)
