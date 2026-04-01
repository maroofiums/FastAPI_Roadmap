from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

print('root', client.get('/').status_code, client.get('/').json())
user_data = {'name': 'Alice', 'email': 'alice@example.com'}
r = client.post('/users/', json=user_data)
print('create_user', r.status_code, r.json())
user_id = r.json()['id']
post_data = {'title': 'Hello', 'content': 'World', 'user_id': user_id}
r = client.post('/posts/', json=post_data)
print('create_post', r.status_code, r.json())
print('get_posts', client.get('/posts/?page=1&limit=10').status_code, client.get('/posts/?page=1&limit=10').json())
print('get_posts_by_user', client.get(f'/posts/user/{user_id}').status_code, client.get(f'/posts/user/{user_id}').json())
