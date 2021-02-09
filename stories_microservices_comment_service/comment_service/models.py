from .config.extentions import db




class Comment(db.Document):
    post_id = db.IntField()
    user_id = db.IntField()
    content = db.StringField(max_length=255,)
    comments = db.ListField(db.DictField())
    
    