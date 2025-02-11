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


# text = "949334194299888995920657884197254696884441744796"
# print(text)
# text = number_to_boar_emoji(text)
# print(text)
# text = boar_emoji_to_number(text)
# print(text)




