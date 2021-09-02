import json
import random
from datetime import datetime, timezone, timedelta
import time
from django.db import connection
from django.http import JsonResponse
import jwt
from django.conf import settings
from pyfcm import FCMNotification
import uuid
import ast
from models.constants import ServerEnum




def sendConnectionErrorResponse():
    return JsonResponse({
            'status': False,
            'responseMessage': ServerEnum.RESPONSE_CONNECTION_ERROR
        })


def sendDatabaseConnectionErrorResponse():
    return JsonResponse({
        'status': False,
        'responseMessage': ServerEnum.RESPONSE_DATABASE_CONNECTION_ERROR
    })

def decodeJson(requestBody):
    bodyUnicode = requestBody.decode('utf-8')
    body = json.loads(bodyUnicode)
    return body


def naValue(data):
    if data:
        return data
    return "N/A"

def checkKey(key, jsonData):
    if key in jsonData:
        return jsonData[key]
    return None


def convertCurrentLocalTimeToUTCTimestamp(timeDelta):
    timeDeltaHour = int(timeDelta.split(":")[0])
    timeDeltaMinute = int(timeDelta.split(":")[1])
    current_time = datetime.now(timezone.utc)
    current_local_time_in_utc = current_time + timedelta(hours=timeDeltaHour) + timedelta(hours=timeDeltaMinute)
    current_local_time_in_utc_timestamp = int(current_local_time_in_utc.timestamp())

    return current_local_time_in_utc_timestamp


def convertTo12HourFormatTime(time):
    return datetime.fromtimestamp(time, tz=timezone.utc).strftime('%Y-%m-%d %I:%M %p')


def utcTimeStamp():
    from datetime import timezone
    import datetime

    dt = datetime.datetime.now()

    utc_time = dt.replace(tzinfo = timezone.utc)
    utc_timestamp = utc_time.timestamp()

    return int(utc_timestamp)

