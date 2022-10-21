fibonnaci = "0 1 1 2 3 5 8 13 21 34 0 1 1 2 3 5 8 13 21 34 0 1 1 2 3 5 8 13 21 34 0 1 1 2 3 5 8 13 21 34".split()

flag = "fmbi~i{v1d`t3ygz~vfbn"

result = ""

for i in range(len(flag)):
	result += chr(ord(flag[i])-int(fibonnaci[i]))

print(result)

# flag{dynam1c_r0t_mirveal}
