import pytz
import hashlib
from datetime import datetime, timezone, timedelta

def get_pig_timestamp(year=None, month=None, day=None, password=None):
    if year and month and day:
        print("传入日期:", year, "年", month, "月", day, "日")
    else:
        current_date = datetime.now()
        # 将当前时间转换为北京时区
        target_timezone = pytz.timezone('Asia/Shanghai')
        current_date_beijing = current_date.astimezone(target_timezone)
        year, month, day = current_date_beijing.year, current_date_beijing.month, current_date_beijing.day
        print("本地日期:", year, "年", month, "月", day, "日")
        
    hour = year % 10
    minute = month
    second = day
    beijing_time = datetime(year, month, day, hour, minute, second)
    
    beijing_timezone = timezone(timedelta(hours=8))
    beijing_time = beijing_time.replace(tzinfo=beijing_timezone)
    
    if password:
        hash_object = hashlib.sha256(password.encode())
        hash_hex = hash_object.hexdigest()
        hash_int = int(hash_hex, 16)
        
        # 将偏移量加到时间上
        offset = hash_int % 10000
        beijing_time = beijing_time + timedelta(seconds=offset)
    
    pig_timestamp = beijing_time.timestamp()

    return pig_timestamp
