# -*- coding: utf-8 -*-

# 单表代换分析

StdSortByFreq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"  # 字母出现频率排序
data = [[] for i in range(26)]  # 存储字符出现频数
length = 0  # 存储密文长度
c = 0

msg_data = \
    [["UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOW"
      "SFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ",
      "BF\\NRVYCUG\\\\O\\SEW\\AMIDHLPT"],
     ["JXQCEFMPJASOQMDPQABCSTYSMGRQBTQOASKQAOUWCPQBDPMEEASIVMWPOQVJ"
      "XQVQCSORWBQKMMYVJQAOXQPVASBFPAOJCOARQHFQPCQSOQASBQAOXXAVCJVM"
      "GSABZASJATQVJXQYSMGRQBTQGQTACSDPMEKMMYVASBDMPEARQBWOAJCMSQSA"
      "KRQVWVJMRQAPSAKMWJJXCSTVXAJGQXAZQSMMFFMPJWSCJIJMQHFQPCQSOQCS"
      "BACRIRCDQGOOASVJWBIARRJXQFRAOQVCSJXQGMPRBASBRQAPSDPMEFQMFRQG"
      "QGCRRSQZQPEQQJCSMWRCDQJCEQLWVJKIPQABCSTJXQCPKMMYVGQOASARVMBQ"
      "ZQRMFMWPASARIJCOARVYCRRVASBRQAPSXMGJMZCQGASBCSJQPFPQJJXQGMPR"
      "BAPMWSBWVCSBCDDQPQSJGAIVGQOASRQAPSJXQFAVJKIPQABCSTKMMYVCSJXC"
      "VGAIGQGMSJPQFQAJJXQECVJAYQVMMJXQPVASBOASKWCRBMSJXQCPAOXCQZQEQSJV",
      "ADIFMPWXYTBJOZCRELNGQSUHKV"]]

while c != 1 and c != 2:
    print("请选择密文1或密文2（输入数字）：")
    c = int(input())  # 选择密文
msg = msg_data[c - 1][0]
outtab = msg_data[c - 1][1]

# 得到各字母的频率
for i in range(26):
    chrcnt = msg.count(chr(i + 65))
    length += chrcnt
    data[i] = [chr(i + 65), chrcnt]

# 按频率降序输出
print()  # 输出一个空行进行换行
print("字母频率\t--> 对应顺序明文字母")
data.sort(key=lambda x: x[1], reverse=True)
for i in range(26):
    print(data[i][0], ':', round(data[i][1] / length * 100, 2), "%\t-->\t", StdSortByFreq[i])

# 输出对应关系
print()  # 输出一个空行进行换行
print("对应关系：")
print("密文：", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("明文：", outtab)

# 得到明文
intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
trantab = msg.maketrans(intab, outtab)
translated = msg.translate(trantab).lower()
print()  # 输出一个空行进行换行
print("明文：")
cnt = 0
while cnt < length:
    print(translated[cnt:cnt + 60])
    cnt += 60

# 阻止在Win终端中直接关闭窗口
import sys
if sys.platform == "win32" and sys.stdin.isatty():
    input("\nPress <Enter> to exit.")
