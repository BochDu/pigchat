boar_emoji_dict = {
    '0': '🐗',
    '1': '🌿',
    '2': '🌳',
    '3': '🍎',
    '4': '🐽',
    '5': '💩',
    '6': '🍄',
    '7': '🐖',
    '8': '🌾',
    '9': '🍃'
}

def is_only_boar_emoji(input_str):
    for char in input_str:
        if char not in boar_emoji_dict.values():
            return False
    return True

def number_to_boar_emoji(number_str):
    result = ""
    for digit in number_str:
        if digit in boar_emoji_dict:
            result += boar_emoji_dict[digit]
        else:
            result += digit
    return result

def boar_emoji_to_number(emoji_str):
    result = ""
    for emoji in emoji_str:
        found = False
        for key, value in boar_emoji_dict.items():
            if value == emoji:
                result += key
                found = True
        if not found:
            result += emoji
    return result




