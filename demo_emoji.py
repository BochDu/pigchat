import pigtime
import pigchat

#获取本地日期
timestamp = pigtime.get_pig_timestamp()

#设置指定日期
# timestamp = pigtime.get_pig_timestamp(2024,1,1)

input_str = "将军"

# 野猪加密
pigtext = pigchat.pigchat_emoji_encrypt(timestamp,input_str)
print(pigtext)

# 野猪解密
pigtext = pigchat.pigchat_emoji_decrypt(timestamp,pigtext)
print(pigtext)