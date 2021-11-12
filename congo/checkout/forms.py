from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators, StringField, IntegerField


class CheckoutForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    address = TextAreaField(u'Mailing Address', [validators.required(), validators.length(max=200)])
    zipcode = IntegerField(u'Zip Code', [validators.required()])
    credit_card_number = IntegerField('Credit Card Number', [validators.required()])
    credit_card_ccv = IntegerField('CCV', [validators.required()])
