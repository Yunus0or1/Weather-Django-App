from datetime import datetime, timezone, timedelta

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

