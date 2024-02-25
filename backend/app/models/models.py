from .. import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(10))

    def __repr__(self):
        return f'<User {self.name}>'
