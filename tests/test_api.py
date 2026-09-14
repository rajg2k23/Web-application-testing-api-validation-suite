import requests
def test_health_endpoint(base_url):
 r=requests.get(f'{base_url}/api/health');assert r.status_code==200;assert r.json()['status']=='ok'
def test_get_users_returns_list(base_url):
 r=requests.get(f'{base_url}/api/users');assert r.status_code==200;assert isinstance(r.json(),list)
def test_get_existing_user(base_url):
 r=requests.get(f'{base_url}/api/users/1');assert r.status_code==200;assert all(k in r.json() for k in ['id','name','email'])
def test_get_missing_user_returns_404(base_url):
 r=requests.get(f'{base_url}/api/users/999999');assert r.status_code==404
def test_create_user(base_url):
 r=requests.post(f'{base_url}/api/users',json={'name':'PyTest User','email':'pytest_user@example.com'});assert r.status_code in (201,409)
def test_create_user_requires_fields(base_url):
 r=requests.post(f'{base_url}/api/users',json={'name':'Missing Email'});assert r.status_code==400
