from datetime import datetime, timezone, timedelta

# 生成野猪时间戳，若有传参采用传参，没有传参自动获取
def get_pig_timestamp(year=None, month=None, day=None):
    if year and month and day:
        print("传入日期:", year, "年", month, "月", day, "日")
        hour = year % 10
        minute = month
        second = day
        beijing_time = datetime(year, month, day, hour, minute, second)
    else:
        current_date = datetime.now()
        year, month, day = current_date.year, current_date.month, current_date.day
        print("本地日期:", year, "年", month, "月", day, "日")
        hour = year % 10
        minute = month
        second = day
        beijing_time = datetime(year, month, day, hour, minute, second)
    
    beijing_timezone = timezone(timedelta(hours=8))
    beijing_time = beijing_time.replace(tzinfo=beijing_timezone)
    utc_timestamp = beijing_time.timestamp()

    return utc_timestamp
