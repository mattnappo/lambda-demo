import json
import hashlib

from datetime import datetime
from dateutil.relativedelta import relativedelta

MONTHS = 6

def expires_date():
    today = datetime.now()
    expires = today + relativedelta(months=MONTHS)
    return expires.strftime('%m/%d/%y')

def hash_message(message):
    m = hashlib.sha256()
    
    m.update(message.encode('utf-8'))
    
    return str(m.hexdigest())

def lambda_handler(event, context):
    message = event['message'] + str(event['time'])

    response = {
        'generated_token': hash_message(message),
        'expires': expires_date()
    }
    return response
