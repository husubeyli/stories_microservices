from enum import unique
from marshmallow import fields, validate
from auth_service.config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor
from marshmallow import validates, ValidationError
from auth_service.models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    image = AbsoluteURLFor(
        'uploaded_file',
        filename='<image>'
    )
    password = ma.String(load_only=True, required=True)
    email = fields.Email(required=True, validate=[validate.Length(min=1)])
    class Meta:
        model = User
        load_instance = True
        exclude = ('is_superuser', 'is_active')
    
    @validates('email')
    def validate_user_email(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValidationError(f'This "{email}" email is available to the user')

    
class LoginSchema(ma.Schema):
    password = ma.String(required=True,)
    email = fields.Email(required=True, unique=True, validate=[validate.Length(min=1)])

