from ..config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor
from marshmallow import validates, ValidationError, fields, validate
from ..models import SubscribersMail




class SubscriberSchema(ma.SQLAlchemyAutoSchema):

    email = fields.Email(required=True, validate=[validate.Length(min=1)])
    class Meta:
        model = SubscribersMail
        include_fk = True
        load_instance = True

    @validates('email')
    def validate_user_email(self, email):
        user = SubscribersMail.query.filter_by(email=email).first()
        if user:
            raise ValidationError(f'This "{email}" email is available to the user')
            