import unittest
from app import create_app, db
from app.models.models import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_user_list(self):
        # 添加测试用户
        user1 = User(name="Test User 1", gender="Male")
        user2 = User(name="Test User 2", gender="Female")
        with self.app.app_context():
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
        
        # 发起 GET 请求
        response = self.client.get('/get_user_list')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Test User 1")
        self.assertEqual(data[1]['name'], "Test User 2")

    def test_add_user(self):
        # 测试添加用户
        response = self.client.post('/add_user', json={'name': 'New User', 'gender': 'Non-binary'})
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertIn('User added successfully', data['message'])

        # 验证用户是否真的被添加
        with self.app.app_context():
            user = User.query.filter_by(name='New User').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.gender, 'Non-binary')

if __name__ == '__main__':
    unittest.main()
