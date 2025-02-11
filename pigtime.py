import requests
from datetime import datetime, timezone, timedelta

# 生成野猪时间戳，若有传参采用传参，没有传参自动获取
def get_pig_timestamp(year=None, month=None, day=None):
    if year and month and day:
        print("传入日期:",year,"年",month,"月", day,"日")
        hour = year % 10
        minute = month
        second = day
        beijing_time = datetime(year, month, day, hour, minute, second)
    else:
        response = requests.get("http://worldclockapi.com/api/json/utc/now")

        if response.status_code == 200:
            data = response.json()
            current_date = data.get('currentDateTime', '').split('T')[0]
            
            if current_date:
                year, month, day = map(int, current_date.split('-'))
                print("在线日期:",year,"年",month,"月", day,"日")
                hour = year % 10
                minute = month
                second = day
                beijing_time = datetime(year, month, day, hour, minute, second)
            else:
                print("无法解析当前日期时间")
        else:
            print("无法获取当前日期")
    
    beijing_timezone = timezone(timedelta(hours=8))
    beijing_time = beijing_time.replace(tzinfo=beijing_timezone)
    utc_timestamp = beijing_time.timestamp()

    # if utc_timestamp:
    #     print("野猪时间戳:", utc_timestamp)

    return utc_timestamp