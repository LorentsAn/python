f = [int(i) for i in open('file.txt').read().split()]
for i in range(len(f)):
	if 16**3<= f[i]< 16**4:
		if ((f[i] % 16) >=10 or (f[i] // 16 % 16) >= 10 or (f[i] // 16 // 16 % 16) >= 10 or (f[i] // 16 // 16 // 16) >= 10) and\
		(f[i] % 16) + (f[i] // 16 // 16 % 16) == (f[i] // 16 % 16) + (f[i] // 16 // 16 // 16):
			print(f[i], str(f[i] % 16) + str(f[i] // 16 % 16) + str(f[i] // 16 // 16 % 16) + str(f[i] // 16 // 16 // 16)) 
