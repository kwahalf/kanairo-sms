import random
import requests
from flask import current_app
from flask_restplus import Resource
from flask import abort, request
from app.blueprints.serializers import  api, sms, sms_response
from app.models import User
from app import client

ns = api.namespace('sms', description='SMS sending operations')
api.add_namespace(ns)

@client.task
def send_dlr(data):
    """ Function to send DLRS in the background.
    """
    status_list = ["DELIVERD", "FAILED", "UNCONFIRMED"]
    with current_app.app_context():
        msg = {
            "id": data["id"],
            "status": random.choice(status_list),
            "amount": "KES1.5"
        }

        request_headers = {"Accept": "application/json"}
        try:
            response = requests.post(
                data["callback_url"],
                data=msg,
                headers=request_headers,
                timeout=5,
            )
        except requests.ReadTimeout:
            pass


@ns.route('/')
@api.response(401, 'user is not authorized')
class SMS(Resource):
    """this class handles the creation of an SMS send request"""
    @api.header('Authorization', 'JWT Token', required=True)
    @api.response(201, 'SMS request sucessfully created')
    @api.expect(sms)
    @api.marshal_with(sms_response)
    def post(self):
        """Handle POST request for this resource. Url ---> /sms/"""
        # Get the access token from the header
        access_token = request.headers.get('Authorization')
        post_data = request.json
        if access_token:
                # Attempt to decode the token and get the User ID
                user_id = User.decode_token(access_token)
                if not isinstance(user_id, str):
                    post_data.update({"id": random.randint(1200, 30000), "status": "created"})
                    send_dlr.apply_async(args=[post_data], countdown=10)
                    return post_data, 201
                abort(401, user_id)


