import string

a = string.ascii_letters
with open("/home/ulmaa/ctf/ctf-night/vol-1/crypto/edenmine/challenge.txt",'w') as f:
    flag = "ccsCTF{I_10v3_fr3qu3ncies_XD}"
    for i in range(29):

        f.write(a[i] * ord(flag[i]))