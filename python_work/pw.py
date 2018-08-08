# pw.py
# password encoder/manager
import requests
help(requests)

#def vig(txt='', key='', typ='d'):
#    if not txt:
#        print('Needs text')
#        return
#    if not key:
#        print('Needs key')
#        return
#    if typ not in ('d', 'e'):
#        print('Type must be "d" or "e"')
#        return
#
#    k_len = len(key)
#    k_ints = [ord(i) for i in key]
#    txt_ints = [ord(i) for i in txt]
#    ret_txt = ''
#    for i in range(len(txt_ints)):
#        adder = k_ints[i % k_len]
#        if typ == 'd':
#            adder *= -1
#
#        v = (txt_ints[i] - 32 + adder) % 95
#
#        ret_txt += chr(v + 32)
#
#    print(ret_txt)
#    return ret_txt
#
#
#site = input("Enter the site you want the password for: ").lower()
#key = input("Enter a key for encoding/decoding: ")
#typ = input("Enter 'e' or 'd' to encode or decode, respectively: ")
#
#
#PASSWORDS = {"github":"*&fb3iu39das2edjofniun","facebook":"&*fbi363b^*bfhedbduji",\
#             "twitter":"#GyU*hs_@37hujdfbjO","d2l":"!uhdf#_fdjiuUygfs"}
#
#
#
#
#output = vig(PASSWORDS[site],key,typ)
#pyperclip.copy(output)
#
#



