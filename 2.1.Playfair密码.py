# -*- coding: utf-8 -*-

# PlayFair密码

# 普通字符串 -> 英文字母
# 由于Playfair密码的二义性，生成的字符串不包含'j'和'x'以避免错误
def str2chr(msg):
    msg = msg.encode('utf-8')
    msg = ''.join(['%02x' % b for b in msg])
    rplist = ["ghitklmnop", "qrstuvwnyz"]
    for i in range(10):
        msg = msg.replace(str(i), rplist[i % 2][i])
    return msg


# 英文字母 -> 普通字符串
def chr2str(msg):
    rplist = ["ghitklmnop", "qrstuvwnyz"]
    for i in range(10):
        msg = msg.replace(rplist[0][i], str(i)).replace(rplist[1][i], str(i))
    msg = bytes.fromhex(msg)
    msg = msg.decode('utf-8')
    return msg


# 字母表
letter_list = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


# 移除字符串中重复的字母
def remove_duplicates(key):
    key = key.upper()  # 转成大写字母组成的字符串
    _key = ''
    for ch in key:
        if ch == 'J':
            ch = 'I'
        if ch in _key:
            continue
        else:
            _key += ch
    return _key


# 根据密钥建立密码表
def create_matrix(key):
    key = remove_duplicates(key)  # 移除密钥中的重复字母
    key = key.replace(' ', '')  # 去除密钥中的空格

    for ch in letter_list:  # 根据密钥获取新组合的字母表
        if ch not in key:
            key += ch
    # 密码表
    keys = [[i for _ in range(5)] for i in range(5)]
    for i in range(len(key)):  # 将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
        keys[i // 5][i % 5] = key[i]
    return keys


# 获取字符在密码表中的位置
def get_matrix_index(ch, keys):
    for i in range(5):
        for j in range(5):
            if ch == keys[i][j]:
                return i, j  # i为行，j为列


def get_ctext(ch1, ch2, keys):
    index1 = get_matrix_index(ch1, keys)
    index2 = get_matrix_index(ch2, keys)
    r1, c1, r2, c2 = index1[0], index1[1], index2[0], index2[1]
    if r1 == r2:
        ch1 = keys[r1][(c1 + 1) % 5]
        ch2 = keys[r2][(c2 + 1) % 5]
    elif c1 == c2:
        ch1 = keys[(r1 + 1) % 5][c1]
        ch2 = keys[(r2 + 1) % 5][c2]
    else:
        ch1 = keys[r1][c2]
        ch2 = keys[r2][c1]
    text = ''
    text += ch1
    text += ch2
    return text


def get_ptext(ch1, ch2, keys):
    index1 = get_matrix_index(ch1, keys)
    index2 = get_matrix_index(ch2, keys)
    r1, c1, r2, c2 = index1[0], index1[1], index2[0], index2[1]
    if r1 == r2:
        ch1 = keys[r1][(c1 - 1) % 5]
        ch2 = keys[r2][(c2 - 1) % 5]
    elif c1 == c2:
        ch1 = keys[(r1 - 1) % 5][c1]
        ch2 = keys[(r2 - 1) % 5][c2]
    else:
        ch1 = keys[r1][c2]
        ch2 = keys[r2][c1]
    text = ''
    text += ch1
    text += ch2
    return text


# Playfair密码加密
def playfair_encode(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J", "I")
    plaintext = list(plaintext)
    plaintext.append('#')
    plaintext.append('#')

    keys = create_matrix(key)
    ciphertext = ''
    i = 0
    while plaintext[i] != '#':
        if plaintext[i] == plaintext[i + 1]:
            plaintext.insert(i + 1, 'X')
        if plaintext[i + 1] == '#':
            plaintext[i + 1] = 'X'
        ciphertext += get_ctext(plaintext[i], plaintext[i + 1], keys)
        i += 2
    return ciphertext


# Playfair密码解密
def playfair_decode(ciphertext, key):
    keys = create_matrix(key)
    i = 0
    plaintext = ''
    while i < len(ciphertext):
        plaintext += get_ptext(ciphertext[i], ciphertext[i + 1], keys)
        i += 2
    _plaintext = ''
    _plaintext += plaintext[0]
    for i in range(1, len(plaintext) - 1):
        if plaintext[i] != 'X':
            _plaintext += plaintext[i]
        elif plaintext[i] == 'X':
            if plaintext[i - 1] != plaintext[i + 1]:
                _plaintext += plaintext[i]
    _plaintext += plaintext[-1]
    _plaintext = _plaintext.lower()
    # 去除后面补位的字符'x'
    if _plaintext[-1] == 'x':
        _plaintext = _plaintext[:-1]
    return _plaintext


if __name__ == '__main__':
    import sys
    # plain = input("请输入明文")
    # ckey = input("请输入密钥")
    plain = "量子通信保密技术的诞生和快速发展主要取决于以下两个因素：a、经典保密通信面临着" \
            "三个难以彻底解决的关键问题，即密钥协商、身份识别和窃听检测，这些问题的有效解决" \
            "需要新技术。b、在对新技术的探索中，人们发现了量子内在的安全特性及其可能的应用。"
    ckey = "abc"
    print("明文：\n", plain)
    print("密钥：\n", ckey)
    # 判断明文是否全为英文字母，若否则进行转换
    if not plain.encode('utf-8').isalpha():
        notAlpha = True
        plain = str2chr(plain)
        print("明文转换为英文字母：\n", plain)
    else:
        notAlpha = False
    # 进行加解密操作
    cipher = playfair_encode(plain, ckey)
    print("加密：\n", cipher)
    plain = playfair_decode(cipher, ckey)
    print("解密：\n", plain)
    # 若原明文不全为英文字母，则进行转换
    if notAlpha:
        plain = chr2str(plain)
        print("英文字母转换为明文：\n", plain)
    # 阻止在Win终端中直接关闭窗口
    if sys.platform == "win32" and sys.stdin.isatty():
        input("\nPress <Enter> to exit.")
