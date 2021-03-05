# app/__init__.py
import os
from .restplus import api
from flask import Flask, Blueprint
from flask_restplus import Api
from celery import Celery


# local import
from instance.config import app_config
from .blueprints.auth import ns  as auth_namespace 
from .models import db


cnfg_name=os.getenv('APP_SETTINGS')

client = Celery(__name__, broker=app_config[cnfg_name].CELERY_BROKER_URL)

def create_app(config_name):
	from .blueprints.sms import ns as sms_namespace

	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	api.add_namespace(auth_namespace)
	api.add_namespace(sms_namespace)
	api.init_app(app)

	client.conf.update(app.config)

	return app

