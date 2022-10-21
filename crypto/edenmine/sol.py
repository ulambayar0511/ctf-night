with open("/home/ulmaa/ctf/ctf-night/vol-1/crypto/edenmine/challenge.txt",'r') as f:
	data = f.read()

u = 'a'
flag = ""
count = 0
for i in data:
	if i == u:
		count += 1
	else:
		u = i
		flag += chr(count + 1)
		count = 0
print(flag)


