import pigtime
import pigchat

#获取本地日期
timestamp = pigtime.get_pig_timestamp()

#设置指定日期
# timestamp = pigtime.get_pig_timestamp(2024,1,1)

input_str = "忠诚"

# 数字加密
pignum = pigchat.pigchat_num_encrypt(timestamp,input_str)
print(pignum)

# 数字解密
result = pigchat.pigchat_num_decrypt(timestamp,pignum)
print(result)




