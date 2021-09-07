from datetime import datetime, timezone, timedelta

from django.http import JsonResponse


def convertTimestampToDate(timestamp):
    return datetime.fromtimestamp(timestamp).date()


def convertToDate(stringDate):
    try:
        # Means this is a ISO format date
        if 'T' in stringDate:
            stringDate = stringDate.replace(' ', '+')
            finalDate = datetime.strptime(stringDate, '%Y-%m-%dT%H:%M:%S%z')

        if 'T' not in stringDate:
            finalDate = datetime.strptime(stringDate, '%Y-%m-%d').replace(tzinfo=timezone.utc)

        currentDate = datetime.now(timezone.utc)
        difference = finalDate - currentDate

        # If today process the date
        if str(finalDate.date()) == str(currentDate.date()):
            return JsonResponse({
                "date": finalDate.date(),
            }, status=200)

        # Means Invalid Past date
        if difference.days < 0:
            return JsonResponse({
                "error": "Date is in the past",
                "error_code": "invalid date"
            }, status=400)

        # Means Future date which API does not allow us
        if difference.days > 7:
            return JsonResponse({
                "error": "You can only request up to 7 days forecast from today",
                "error_code": "future_forecast_limitation"
            }, status=400)

        # Date Process success. send the date back
        return JsonResponse({
            "date": finalDate.date(),
        }, status=200)


    except Exception as e:
        # If any error happens in parsing, this response will be sent
        return JsonResponse({
            "error": "Invalid Date Format. Please use date and datetime stamps in the ISO 8601 format",
            "error_code": "invalid_date_format"
        }, status=404)
