import pigtime
import pigchat

#联网获取日期
timestamp = pigtime.get_pig_timestamp()

input_str = "忠诚"

# 数字加密
pignum = pigchat.pigchat_num_encrypt(timestamp,input_str)
print(pignum)
# 数字解密
result = pigchat.pigchat_num_decrypt(timestamp,pignum)
print(result)




