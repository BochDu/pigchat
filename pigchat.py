import random
import pigemoji


def square_digits_in_timestamp(timestamp):
    squared_digits = [int(digit)**2 for digit in str(int(timestamp))]
    result = int(''.join(map(str, squared_digits)))
    return result

def extract_chars(input_str):
    result = ""
    for i in range(0, len(input_str), 3):
        result += input_str[i:i+2]
    return result

def extract_three_chars_from_right(input_str):
    unique_chars = []
    for char in input_str[::-1]:  # 从右到左遍历字符串
        if char not in unique_chars:
            unique_chars.append(char)
        
        if len(unique_chars) == 3:
            break
    
    return ''.join(unique_chars)

def pigchat_one_init(timestamp):
    pigchat_one = square_digits_in_timestamp(timestamp)
    # print(pigchat_one)
    pigchat_one = extract_chars(str(pigchat_one))
    # print(pigchat_one)
    pigchat_one = extract_three_chars_from_right(pigchat_one)
    # print(pigchat_one)
    
    return pigchat_one

def utf8_to_binary(input_str):
    # 将字符串转换为UTF-8编码
    utf8_bytes = input_str.encode('utf-8')

    # 将UTF-8编码转换为二进制表示
    utf8_binary = ''.join([f'{byte:08b}' for byte in utf8_bytes])

    return utf8_binary

def binary_to_utf8(binary_str):
    try:
        bytes_list = [int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8)]
        utf8_bytes = bytes(bytes_list)

        utf8_str = utf8_bytes.decode('utf-8')
    except UnicodeDecodeError as e:
        print("decode utf-8 error")
        utf8_str = ""

    return utf8_str


def pigchat_num_encrypt(timestamp, input_str):
    text = utf8_to_binary(input_str)
    pigchat_one = pigchat_one_init(timestamp)

    one_numbers = [int(num) for num in pigchat_one]
    # print(one_numbers)
    zero_numbers = [num for num in range(10) if num not in one_numbers]
    # print(zero_numbers)
    
    encrypted_data = ""
    for char in text:
        if char == '1':
            encrypted_data += str(random.choice(one_numbers))
        elif char == '0':
            encrypted_data += str(random.choice(zero_numbers))
        else:
            encrypted_data += char

    return encrypted_data

def pigchat_num_decrypt(timestamp, text):
    pigchat_one = pigchat_one_init(timestamp)
    
    one_numbers = [int(num) for num in pigchat_one]
    # print(one_numbers)
    zero_numbers = [num for num in range(10) if num not in one_numbers]
    # print(zero_numbers)

    decrypted_data = ""
    for char in text:
        if char.isdigit() and int(char) in one_numbers:
            decrypted_data += '1'
        else:
            decrypted_data += '0'

    decrypted_data = binary_to_utf8(decrypted_data)

    return decrypted_data

def pigchat_emoji_encrypt(timestamp, input_str):
    try:
        input_str.encode('utf-8')
    except UnicodeEncodeError:
        return input_str

    pignum = pigchat_num_encrypt(timestamp, input_str)
    encrypted_data = pigemoji.number_to_boar_emoji(pignum)
    return encrypted_data


def pigchat_emoji_decrypt(timestamp, input_str):
    if pigemoji.is_only_boar_emoji(input_str):
        pignum = pigemoji.boar_emoji_to_number(input_str)
        decrypted_data = pigchat_num_decrypt(timestamp,pignum)
        return decrypted_data
    else:
        return input_str

















