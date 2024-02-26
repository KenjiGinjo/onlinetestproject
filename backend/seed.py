from app import create_app, db  # Adjust the import according to your project structure
from app.models.models import User  # Adjust the import path to where your User model is defined

# Initialize the Flask application context
app = create_app()
app.app_context().push()

# Seed data function
def seed_data():
    # List of user data to add
    users_data = [
        {'name': 'Alice', 'gender': 'Female'},
        {'name': 'Bob', 'gender': 'Male'},
        {'name': 'Charlie', 'gender': 'Male'},
        {'name': 'Diana', 'gender': 'Female'},
        {'name': 'Eve', 'gender': 'Female'},
        {'name': 'Frank', 'gender': 'Male'},
        {'name': 'Grace', 'gender': 'Female'},
        {'name': 'Henry', 'gender': 'Male'},
        {'name': 'Ivy', 'gender': 'Female'},
        {'name': 'Jack', 'gender': 'Male'},
    ]

    # Create and add users to the session
    for user_data in users_data:
        user = User(name=user_data['name'], gender=user_data['gender'])
        db.session.add(user)

    # Commit the session to the database
    db.session.commit()
    print('Users seeded successfully!')

if __name__ == '__main__':
    seed_data()
