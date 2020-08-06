# A function that adds alternates to a Babylon source file (.gls or .txt)
# before running the code, if your source file hase no header, you must put
# the 'header' in the first line!

import pandas as pd

def add_alternate(file, header='header'):
	df = pd.read_table(file, skip_blank_lines=False)
	# n = df[header].loc[2] # this would be the third line in your file. it should return an empty value
	evens = df[header].iloc[::3]    
	evens[:] = evens + '|' + evens.str.replace('\s+', '|')
	df.columns = df.columns.str.strip()
	df.to_csv('result.txt', index=False, header=False, sep='\t')
	f = open('result.txt','r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace("\"\"",'')
	f = open('result.txt','w')
	f.write(newdata)
	f.close()

if __name__ == '__main__':
	add_alternate('test.txt') # put your source file here (this could be .gls or .txt file)
                                  # the first line in your file must have a header (default='header')
                                  # the second line in your file must be the first enrty of your dictionary.
                                  # check out the example file (test.txt) in the directory .

