import pytest,requests
BASE_URL='http://127.0.0.1:5000'
@pytest.fixture(scope='session')
def base_url(): return BASE_URL
@pytest.fixture(scope='session',autouse=True)
def verify_application_is_running():
 r=requests.get(f'{BASE_URL}/api/health',timeout=5); assert r.status_code==200; assert r.json()['status']=='ok'
