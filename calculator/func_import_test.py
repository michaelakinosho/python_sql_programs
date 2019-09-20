import sys
#import argparse
import pandas as pd

fname = "functions_file.csv"
#fname = "all_day.csv"

df = pd.read_csv(fname)
print(df)
num_rows = df.shape[0]
i = 0
while i < num_rows:
	if df.name[i] == "nine":
		print(df.name[i])
	i += 1
print(i)

brac_list = ["(","(","(",")","("]
#brac_list = []
print(len(brac_list))
brac_count = len(brac_list)
for op in brac_list:
	if op == "(":
		brac_count += 1
	elif op == ")":
		brac_count -= 1
		brac_list.pop() * 2
if brac_count < 1:
	brac_list.append(")")
	print("Unable to closing brackets")
else:
	brac_list.append("(")
	print("Able to add closing brackets")
print(brac_count)
print(brac_list)