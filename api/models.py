from manage import db

class TodoModel(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return '<Todo: {}>'.format(self.title)

    def json_dump(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed.strftime('%Y-%m-%d %H:%M:%S') if self.completed else None
        }