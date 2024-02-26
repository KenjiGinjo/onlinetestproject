from flask import Blueprint, jsonify, request
from ..models.models import User, db
from sqlalchemy import desc  


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_user_list():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    pagination = User.query.order_by(User.uid.desc()).paginate(page=page, per_page=per_page, error_out=False)
    users = pagination.items 
    
    users_data = [{'uid': user.uid, 'name': user.name, 'gender': user.gender} for user in users]
    
    return jsonify({
        'users': users_data,
        'total': pagination.total,
        'pages': pagination.pages, 
        'page': page  
    })

@user_bp.route('/user', methods=['POST'])
def add_user():
    data = request.json
    user = User(name=data['name'], gender=data['gender'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

@user_bp.route('/user/<int:uid>', methods=['PUT'])
def edit_user(uid):
    user = User.query.filter_by(uid=uid).first()
    if user:
        data = request.json
        user.name = data.get('name', user.name)
        user.gender = data.get('gender', user.gender)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404



