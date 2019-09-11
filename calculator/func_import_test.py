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