# -*- coding: utf-8 -*-

# DES密码
# 加密模式：ECB
# 填充方式：ZeroPadding
# 编码方式：UTF-8

# 初始置换 - IP盒
IP_table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

# 逆初始置换 - IP逆盒
IP_re_table = [40, 8, 48, 16, 56, 24, 64, 32, 39,
               7, 47, 15, 55, 23, 63, 31, 38, 6,
               46, 14, 54, 22, 62, 30, 37, 5, 45,
               13, 53, 21, 61, 29, 36, 4, 44, 12,
               52, 20, 60, 28, 35, 3, 43, 11, 51,
               19, 59, 27, 34, 2, 42, 10, 50, 18,
               58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# 扩展置换 - E盒
E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

# 置换函数 - P盒
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# S盒
S = [
    # S1盒
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    # S2盒
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    # S3盒
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    # S4盒
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    # S5盒
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    # S6盒
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    # S7盒
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    # S8盒
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]

# 置换选择1 - PC1盒
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# 置换选择2 - PC2盒
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# 密钥每轮左移次数
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# 二进制转化为十六进制
def bin2hex(msg):
    res = ""
    for i in range(int(len(msg) / 4)):
        tmp = msg[i * 4:(i + 1) * 4]
        res += hex(int(tmp, 2))[2:]
    return res


# 十六进制转化为二进制
def hex2bin(msg):
    res = ""
    for i in range(len(msg)):
        tmp = msg[i]
        tmp = bin(int(tmp, 16))[2:]
        tmp = '0' * (4 - len(tmp)) + tmp
        res += tmp
    return res


# 字符串转化为十六进制
def str2hex(msg):
    return msg.encode().hex()


# 十六进制转化为字符串
def hex2str(msg):
    return bytes.fromhex(msg).decode()


# 字符串转化为二进制
def str2bin(msg):
    return hex2bin(str2hex(msg))


# 十六进制转ascii
def hex2ascii(msg):
    bin_str = hex2bin(msg)
    res = ""
    for i in range(int(len(bin_str) / 8)):
        tmp = bin_str[i * 8:(i + 1) * 8]
        res += chr(int(tmp, 2))
    return res


# 由十六进制得到base64
def hex2b64(msg):
    import base64
    return str(base64.b64encode(hex2ascii(msg).encode('raw-unicode-escape')))[2:-1]


# =========================================================== #

# 置换
def change(msg, table):
    res = ""
    for i in table:
        res += msg[i - 1]  # 数组下标i-1
    return res


# 字符串异或操作
def str_xor(msg1, msg2):
    res = ""
    for i in range(0, len(msg1)):
        xor_res = int(msg1[i], 10) ^ int(msg2[i], 10)  # 变成10进制是转化成字符串 2进制与10进制异或结果一样，都是1,0
        if xor_res == 1:
            res += '1'
        if xor_res == 0:
            res += '0'
    return res


# 循环左移操作
def left_turn(msg, num):
    return msg[num:] + msg[0:num]


# S盒过程
def s_box(msg):
    res = ""
    c = 0
    for i in range(0, len(msg), 6):
        now_str = msg[i:i + 6]
        row = int(now_str[0] + now_str[5], 2)
        col = int(now_str[1:5], 2)
        num = bin(S[c][row * 16 + col])[2:]  # 利用了bin输出有可能不是4位str类型的值，所以才有下面的循环并且加上字符0
        for gz in range(0, 4 - len(num)):
            num = '0' + num
        res += num
        c += 1
    return res


# F函数的实现
def fun_f(msg, key):
    first_output = change(msg, E)
    second_output = str_xor(first_output, key)
    third_output = s_box(second_output)
    last_output = change(third_output, P)
    return last_output


# 生成DES子密钥
def gen_key(key):
    key_list = []
    divide_output = change(key, PC_1)
    key_c = divide_output[0:28]
    key_d = divide_output[28:]
    for i in SHIFT:
        key_c = left_turn(key_c, i)
        key_d = left_turn(key_d, i)
        key_output = change(key_c + key_d, PC_2)
        key_list.append(key_output)
    return key_list


# 对一组明文进行加密
def des_encrypt_one(bin_msg, bin_key):
    msg_ip_bin = change(bin_msg, IP_table)
    key_lst = gen_key(bin_key)
    msg_left = msg_ip_bin[0:32]
    msg_right = msg_ip_bin[32:]
    for i in range(0, 15):
        msg_tmp = msg_right
        f_result = fun_f(msg_tmp, key_lst[i])
        msg_right = str_xor(f_result, msg_left)
        msg_left = msg_tmp
    f_result = fun_f(msg_right, key_lst[15])
    msg_fin_left = str_xor(msg_left, f_result)
    msg_fin_right = msg_right
    fin_msg = change(msg_fin_left + msg_fin_right, IP_re_table)
    return fin_msg


# 对一组密文进行解密
def des_decrypt_one(bin_msg, bin_key):
    msg_ip_bin = change(bin_msg, IP_table)
    key_lst = gen_key(bin_key)
    lst = range(1, 16)
    cipher_left = msg_ip_bin[0:32]
    cipher_right = msg_ip_bin[32:]
    for i in lst[::-1]:
        msg_tmp = cipher_right
        cipher_right = str_xor(cipher_left, fun_f(cipher_right, key_lst[i]))
        cipher_left = msg_tmp
    fin_left = str_xor(cipher_left, fun_f(cipher_right, key_lst[0]))
    fin_right = cipher_right
    fin_output = fin_left + fin_right
    bin_plain = change(fin_output, IP_re_table)
    res = bin2hex(bin_plain)
    return res


# 对二进制流进行填充补位（填充方式：ZeroPadding）
def msg_padding(bin_msg):
    ans = len(bin_msg)
    for i in range(64 - (ans % 64)):  # 不够64位补充0
        bin_msg += '0'
    return bin_msg


# 去除填充内容（填充方式：ZeroPadding）
def msg_re_padding(bin_msg):
    return bin_msg.replace('\0', '')


# 对密钥进行处理，判断是否为64位（8字节），不足补0
def key_process(bin_key):
    ans = len(bin_key)
    if len(bin_key) < 64:
        if ans % 64 != 0:
            for i in range(64 - (ans % 64)):  # 不够64位补0
                bin_key += '0'
    else:
        bin_key = bin_key[0:64]  # 超过64位的进行截断
    return bin_key


# 对完整明文进行加密（ECB模式）
def des_encrypt(msg, key):
    bin_msg = msg_padding(str2bin(msg))
    bin_key = key_process(str2bin(key))
    res = ""
    for i in range(int(len(bin_msg) / 64)):
        tmp = bin_msg[64 * i:64 * (i + 1)]
        res += des_encrypt_one(tmp, bin_key)
    res = bin2hex(res)
    return res


# 对完整密文进行解密
def des_decrypt(msg, key):
    bin_msg = hex2bin(msg)
    bin_key = key_process(str2bin(key))
    res = ""
    for i in range(int(len(bin_msg) / 64)):
        tmp = bin_msg[64 * i:64 * (i + 1)]
        res += des_decrypt_one(tmp, bin_key)
    res = hex2str(res)
    res = msg_re_padding(res)
    return res


if __name__ == '__main__':
    import sys
    # 输入明文和密钥
    plain_str = input("请输入明文：")
    key_str = input("请输入密钥：")
    # 进行加解密操作
    encrypted = des_encrypt(plain_str, key_str)
    decrypted = des_decrypt(encrypted, key_str)
    encrypted_ascii = hex2ascii(encrypted)
    encrypted_b64 = hex2b64(encrypted)
    # 输出结果
    print("加密：", encrypted_ascii)
    print("（Base64编码）", encrypted_b64)
    print("（Hex编码）", encrypted)
    print("解密：", decrypted)
    # 阻止在Win终端中直接关闭窗口
    if sys.platform == "win32" and sys.stdin.isatty():
        input("\nPress <Enter> to exit.")
