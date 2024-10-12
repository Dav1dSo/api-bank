from factory import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'