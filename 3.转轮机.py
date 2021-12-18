# -*- coding: utf-8 -*-

# 转轮机

# 转轮个数
wheel_total = 2
# 转轮数据
wheel_list = [[[24, 25, 26, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
               [21, 3, 15, 1, 19, 10, 14, 26, 20, 8, 16, 7, 22, 4, 11, 5, 17, 9, 12, 23, 18, 2, 25, 6, 24, 13]],
              [[26, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
               [20, 1, 6, 4, 15, 3, 14, 12, 23, 5, 16, 2, 22, 19, 11, 18, 25, 24, 13, 7, 10, 8, 21, 9, 26, 17]],
              [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
               [8, 18, 26, 17, 20, 22, 10, 3, 13, 11, 4, 23, 5, 24, 9, 12, 25, 16, 19, 6, 15, 21, 2, 7, 1, 14]]]


# 从某一方向通过转轮位置pos1得到对应位置pos2
def find_match(wheel, pos1, direc=0):
    pos2 = 0
    num = wheel[direc][pos1]
    for i in wheel[(direc+1) % 2]:
        if i == num:
            return pos2
        else:
            pos2 += 1


# 转动转轮
def turn_wheel(wheel):
    wheel[0] = [wheel[0][-1]] + wheel[0][:-1]
    wheel[1] = [wheel[1][-1]] + wheel[1][:-1]


# 转轮机加密
def wheel_encrypt(msg):
    wheel = copy.deepcopy(wheel_list)
    msg = msg.upper()
    count = 0
    res = ""
    for i in msg:
        count += 1
        pos = ord(i) - 65
        # 从左到右每个转轮进行匹配,并同时转动该转轮
        for j in range(0, wheel_total):
            # 匹配
            pos = find_match(wheel[j], pos)
            # 判断是否该转动转轮，若是则转动
            if count % pow(26, wheel_total - j - 1) == 0:
                turn_wheel(wheel[j])
        res += chr(pos + 65)
    return res


# 转轮机解密
def wheel_decrypt(msg):
    wheel = copy.deepcopy(wheel_list)
    msg = msg.upper()
    count = 0
    res = ""
    for i in msg:
        count += 1
        pos = ord(i) - 65
        # 从左到右每个转轮进行匹配,并同时转动该转轮
        for j in range(wheel_total - 1, -1, -1):
            # 匹配
            pos = find_match(wheel[j], pos, 1)
            # 判断是否该转动转轮，若是则转动
            if count % pow(26, wheel_total - j - 1) == 0:
                turn_wheel(wheel[j])
        res += chr(pos + 65)
    return res


if __name__ == '__main__':
    import copy
    import sys
    plain = input("请输入明文：")
    encrypted = wheel_encrypt(plain)
    print("加密", encrypted)
    decrypted = wheel_decrypt(encrypted)
    print("解密", decrypted)
    # 阻止在Win终端中直接关闭窗口
    if sys.platform == "win32" and sys.stdin.isatty():
        input("\nPress <Enter> to exit.")
