def get_distinct(input_str):
    result = '';
    input_str = input_str.replace(' ', '')

    for char in input_str:
        if char not in result:
            result += char

    return list(result)

def get_chiper(key):
    # 去除重複
    key = get_distinct(key)     

    # 產生沒有 Q、I 的字串陣列
    char_list = [chr(_) for _ in range(97, 123) if _ != 106]

    # 取得沒有 Key 的字元陣列
    other_char = list(set(char_list).difference(set(key)))
    other_char.sort()   

    chiper = key + other_char
    return chiper

def print_chiper(chiper):
    for index, value in enumerate(chiper, start = 1):
        print(value + '\t', end = '')
        if index % 5 == 0:
            print()

def plaintext_process(text):
    text = text.lower().replace(' ', '')
    n = 2
    
    # 兩個數字一組
    group = [text[i:i+n] for i in range(0, len(text), n)]

    for index, item in enumerate(group):
        if len(item) == 1:
            continue
        if item[0] == item[1]:
            text = text[:index*2 + 1] + 'x' + text[index*2 + 1:]

    group = [text[i:i+n] for i in range(0, len(text), n)]

    if len(group[-1]) == 1:
        group[-1] = group[-1] + 'x'

    return group

def same_row(index_1, index_2):
    if index_1 // 5 == index_2 // 5:
        return True
    else:
        return False

def same_column(index_1, index_2):
    if index_1 % 5 == index_2 % 5:
        return True
    else:
        return False
    
def get_chiper_index(char, chiper):
    return chiper.index(char.lower())

def encrypt(plaintext, chiper):
    encryptext = ''
    chiper_len = len(chiper) - 1

    for index, item in enumerate(plaintext):
        index_1 = get_chiper_index(item[0], chiper)
        index_2 = get_chiper_index(item[1], chiper)

        if same_column(index_1, index_2):
            if index_2 + 5 <= chiper_len:
                encryptext += chiper[index_1 + 5] + chiper[index_2 + 5]
            else:
                encryptext += chiper[index_1 - 5] + chiper[index_2 - 5]

        elif same_row(index_1, index_2):
            if (index_2 + 1) // 5 == index_2 // 5:
                encryptext += chiper[index_1 + 1] + chiper[index_2 + 1]
            else:
                encryptext += chiper[index_1 - 1] + chiper[index_2 - 1]

        else:
            d = index_1 % 5 - index_2 % 5
            encryptext += chiper[index_1 - d] + chiper[index_2 + d]

    return encryptext