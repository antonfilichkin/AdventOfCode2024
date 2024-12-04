def replace_char_at_index(string, index, new_char):
    chars = list(string)
#     chars[index] = str(new_char)
    return str(chars[:index] + new_char + chars[index + 1:])
