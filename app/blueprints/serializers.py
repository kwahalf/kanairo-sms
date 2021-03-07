from flask_restplus import fields
from app import api



profile = api.model('profile', {
    'email': fields.String(required=True, description='user email adress'),
    'password': fields.String(required=True, description='user password'),
})

sms = api.model('SMS', {
    'to_phone_number': fields.String(required=True, description='Id to be displayed as from on the handset'),
    'sender_id': fields.String(required=True, description='ID to be displayed as from on the handset'),
    'callback_url': fields.String(required=True, description='URL to send back the DLRS'),
    'sms_text': fields.String(required=True, description='SMS to be sent to the handset'),
})


sms_response = api.model('SMSResponse', {
    'to_phone_number': fields.String(required=True, description='Id to be displayed as from on the handset'),
    'sender_id': fields.String(required=True, description='ID to be displayed as from on the handset'),
    'callback_url': fields.String(required=True, description='URL to send back the DLRS'),
    'sms_text': fields.String(required=True, description='SMS to be sent to the handset'),
    'status': fields.String(required=True, description='Status of the message on the Kanairo system'),
    'id': fields.Integer(required=True, description='Unique identifier for the SMS'),
})