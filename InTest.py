tStr = 101101

for n in str(tStr):
	print(n)
	if n != "." and n != "0" and n != "1":
		print("This value {} is greater than 1\n".format(n))
		break