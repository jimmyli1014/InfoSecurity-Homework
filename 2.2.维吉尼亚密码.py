# -*- coding: utf-8 -*-

# 维吉尼亚密码

# 普通字符串 -> 英文字母
def str2chr(msg):
    msg = msg.encode('utf-8')
    msg = ''.join(['%02x' % b for b in msg])
    rplist = ["ghijklmnop", "qrstuvwxyz"]
    for i in range(10):
        msg = msg.replace(str(i), rplist[i % 2][i])
    return msg


# 英文字母 -> 普通字符串
def chr2str(msg):
    rplist = ["ghijklmnop", "qrstuvwxyz"]
    for i in range(10):
        msg = msg.replace(rplist[0][i], str(i)).replace(rplist[1][i], str(i))
    msg = bytes.fromhex(msg)
    msg = msg.decode('utf-8')
    return msg


# 获得密钥，并确保都是英文
def get_key(msg):
    tmp = []
    if msg.encode('utf-8').isalpha():
        for i in msg:
            tmp.append(ord(i.upper()) - 65)
        return tmp
    else:
        print("请输入英文密钥")
        import sys
        if sys.platform == "win32" and sys.stdin.isatty():
            input("\nPress <Enter> to exit.")
        sys.exit()


# 维吉尼亚密码加密
def vigenenre_encrypt(message, key_list):
    ciphertext = ""
    flag = 0
    for plain in message:
        if flag % len(key_list) == 0:
            flag = 0
        if plain.isalpha():  # 判断是否为英文
            if plain.isupper():  # 大写字母
                ciphertext += chr(65 + (ord(plain) - 65 + key_list[flag]) % 26)  # 行偏移加上列偏移
                flag += 1
            if plain.islower():  # 小写字母
                ciphertext += chr(97 + (ord(plain) - 97 + key_list[flag]) % 26)
                flag += 1
        else:  # 不是英文不加密
            ciphertext += plain

    return ciphertext


# 维吉尼亚密码解密
def vigenenre_decrypt(message, key_list):
    plaintext = ""
    flag = 0
    for cipher in message:
        if flag % len(key_list) == 0:
            flag = 0
        if cipher.isalpha():
            if cipher.isupper():
                plaintext += chr(65 + (ord(cipher) - 65 - key_list[flag]) % 26)
                flag += 1
            if cipher.islower():
                plaintext += chr(97 + (ord(cipher) - 97 - key_list[flag]) % 26)
                flag += 1
        else:
            plaintext += cipher
    return plaintext


if __name__ == '__main__':
    import sys
    # plain_str = input("请输入明文：")
    # key = input("请输入密钥：")
    plain_str = "量子通信保密技术的诞生和快速发展主要取决于以下两个因素：a、经典保密通信面临着" \
                "三个难以彻底解决的关键问题，即密钥协商、身份识别和窃听检测，这些问题的有效解决" \
                "需要新技术。b、在对新技术的探索中，人们发现了量子内在的安全特性及其可能的应用。"
    key = "abc"
    print("明文：\n", plain_str)
    print("密钥：\n", key)
    key = get_key(key)
    # 判断明文是否全为英文字母，若否则进行转换
    if not plain_str.encode('utf-8').isalpha():
        notAlpha = True
        plain_str = str2chr(plain_str)
        print("明文转换为英文字母：\n", plain_str)
    else:
        notAlpha = False
    encrypted = vigenenre_encrypt(plain_str, key)
    print("加密：\n", encrypted)
    decrypted = vigenenre_decrypt(encrypted, key)
    print("解密：\n", decrypted)
    # 若原明文不全为英文字母，则进行转换
    if notAlpha:
        decrypted = chr2str(decrypted)
        print("英文字母转换为明文：\n", decrypted)
    # 阻止在Win终端中直接关闭窗口
    if sys.platform == "win32" and sys.stdin.isatty():
        input("\nPress <Enter> to exit.")
