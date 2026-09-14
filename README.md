# Web Application Testing & API Validation Suite

A QA portfolio project demonstrating functional testing, regression testing, Selenium browser automation, REST API validation with Postman/Python, and SQL database verification.

## Stack
Python, Flask, Selenium, PyTest, Requests, SQLite/SQL, Postman

## Run
```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Tests
Keep the Flask app running, then:
```bash
pytest -v
```
Selenium tests require Chrome; Selenium 4 can manage the compatible driver automatically on current setups.

## Postman
Import `postman/WebApp_API_Collection.json` into Postman. It includes positive and negative REST API requests.

## SQL checks
```sql
SELECT id, name, email FROM users;
SELECT COUNT(*) AS total_users FROM users;
SELECT email, COUNT(*) AS duplicates FROM users GROUP BY email HAVING COUNT(*) > 1;
```

## Resume-relevant coverage
- Functional and regression testing
- Selenium UI automation
- REST API validation
- Positive/negative test cases
- SQL/database validation
- PyTest fixtures and assertions
- Postman API collection
