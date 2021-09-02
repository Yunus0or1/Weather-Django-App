import json
from django.db import connection
from django.http import JsonResponse
from django.core.cache import cache


def server(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT count(*)  FROM airports")
        result = cursor.fetchall()
        connection.close()

        redisCheck = cache.keys('*')

        if result and len(redisCheck) >= 0:
            return JsonResponse({
                'databaseMessage': "DATABASE RUNNING",
                'redisMessage': redisCheck,
                'message': "SERVER RUNNING",
                'status': True,
                'responseMessage': 200
            })

        return JsonResponse({
            'databaseMessage': "DATABASE STOPPED",
            'redisMessage': "REDIS STOPPED",
            'message': "SERVER RUNNING",
            'status': False,
            'responseMessage': 200
        })

    except Exception as e:
        return JsonResponse({
            'databaseMessage': "DATABASE STOPPED",
            'redisMessage': "REDIS STOPPED",
            'message': "SERVER STOPPED",
            'status': False,
            'responseMessage': 200
        })


def loadTestServer(request):
    try:
        key = "load_test_server"
        data = json.dumps({"Latiude": "59.99", "Longitude": "61.88"})

        cache.set(key, data, timeout=302400)
        fetchedData = cache.get(key)

        return JsonResponse({
            'data': json.loads(fetchedData),
            'status': True,
            'responseMessage': 200
        })

    except Exception as e:
        print("ERROR IN loadTestServer() method in user/views.py")
        print(e)
        return JsonResponse({
            'status': False,
            'responseMessage': 200
        })


def testCall(request):
    print(request)
    value = cache.keys('*')
    return JsonResponse({
        'data': len(value),
        'data': value,
        'status': True,
        'responseMessage': 200
    })
