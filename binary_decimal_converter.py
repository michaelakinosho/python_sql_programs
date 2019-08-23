dec_bin_dict = 
#def dec_bin_conv():



def dec_bin_type():
	num_type = 0

	try:
		print("Tell us the type of number you are entering")
		num_type = int(input("Please enter 1 for decimal or enter 2 for binary: "))
		while num_type != 1 and num_type != 2:
			print("Number entered is {} ".format(num_type))
			num_type = int(input("Please enter 1 for decimal or enter 2 for binary: "))

	except ValueError:
		print("Please try again, something went wrong")
		dec_bin_type()
	except:
		print("Oops something went wrong")

	finally:
		print("Thank you!!")

def dec_bin_num():
	num_val = 0.0

	try:
		num_val = float(input("Please enter the number to convert: "))
