from flask import Blueprint, jsonify, request
from ..models.models import User, db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/get_user_list', methods=['GET'])
def get_user_list():
    users = User.query.all()
    return jsonify([{'uid': user.uid, 'name': user.name, 'gender': user.gender} for user in users])

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user = User(name=data['name'], gender=data['gender'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

@user_bp.route('/edit_user/<int:uid>', methods=['PUT'])
def edit_user(uid):
    user = User.query.filter_by(uid=uid).first()
    if user:
        data = request.json
        user.name = data.get('name', user.name)
        user.gender = data.get('gender', user.gender)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404



