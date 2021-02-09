from ..config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor
from marshmallow import validates, ValidationError

from marshmallow.fields import String, Email, UUID, Nested, Integer, Method


class CommentSchema(ma.Schema):

    id = String(dump_only=True)
    post_id = Integer(dump_only=True)
    user_id = Integer(dump_only=True)
    content = String(required=True)
    parent_comment = String(load_only=True)
    comments = Method("get_comments")

    def get_comments(self, obj):
        print(obj.comments)
        return obj.comments




