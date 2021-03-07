#!/usr/bin/env python
import os
from app import client, create_app

app = create_app(os.getenv('APP_SETTINGS'))
app.app_context().push()