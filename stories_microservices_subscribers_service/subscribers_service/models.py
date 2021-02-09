from .config.extentions import db




class SubscribersMail(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    def __init__(self, email):
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit() 