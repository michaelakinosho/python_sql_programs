dec_bin_dict = {"Type":0,"Number":0.0}
def dec_bin_conv():
	dec_bin_type()
	dec_bin_num()
	print(dec_bin_dict)

	nType = dec_bin_dict["Type"]
	nNumber = dec_bin_dict["Number"]
	nResult = "0"
	nFinResult = ""
	nPow = 0
	i = 0
	iCount = 0

	#nNumber = int(str(nNumber).split(".")[0])
	nNum_List = str(nNumber).split(".")
	for y in nNum_List:
		iCount += 1
		yNum = int(y)
		#Converting from decimal to binary
		if nType == 1:
			nResult = ""
			while yNum != 0:
				nResult = str(int(yNum % 2)) + nResult
				yNum = (yNum-(yNum % 2))/2
			print(nResult)

		#Converting from binary to decimal
		elif nType == 2:
			
			nPow = len(str(yNum)) -1
			i = 0
			while nPow > -1 :
				print(yNum)
				if str(yNum)[i] == "1":
					#nTemp = (2 ** nPow) + nTemp
					nResult = (2 ** nPow) + int(nResult)
				nPow -= 1
				i += 1
			print(nResult)

		if iCount == 1:
			nFinResult = str(nResult)
		else:
			nFinResult = str(nFinResult) + str(".") + str(nResult)
		print(nFinResult)
		nResult = "0"



def dec_bin_type():
	num_type = 0

	try:
		print("Tell us the type of number you are entering")
		num_type = int(input("Please enter 1 for decimal or enter 2 for binary: "))
		while num_type != 1 and num_type != 2:
			print("Number entered is {} ".format(num_type))
			num_type = int(input("Please enter 1 for decimal or enter 2 for binary: "))
		dec_bin_dict["Type"] = num_type

	except ValueError:
		print("Please try again, something went wrong")
		dec_bin_type()
	except:
		print("Oops something went wrong")

	finally:
		print("Thank you!!")

def dec_bin_num():
	global dec_bin_dict
	num_val = 0.0

	try:
		num_val = float(input("Please enter the number to convert: "))
		if dec_bin_dict["Type"] == 2:
			for n in str(num_val):
				if n != "." and n != "0" and n != "1":
					print("Number {} is not binary".format(num_val))
					num_val = float(input("Please enter the number to convert: "))
					break
		dec_bin_dict["Number"] = num_val
	
	except ValueError:
		print("Please try again, something went wrong")
		dec_bin_num()
	except:
		print("Oops something went wrong")

	finally:
		print("Thank you!!")

dec_bin_conv()