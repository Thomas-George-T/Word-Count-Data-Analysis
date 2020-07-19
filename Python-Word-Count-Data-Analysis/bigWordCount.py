# Author: Thomas George Thomas
# Python program to read a file, compute word count and find execution time.

import time

start = time.time()

# Reading file
file=open("../Input-Files/big.txt","r")
# Initializing Dictionary
dict = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in file.read().split(): 
    dict[word] = dict.get(word, 0) + 1

file.close()

#write the file
fw = open("big-result-python.txt","w")
fw.write(str(dict))
fw.close()

end = time.time()

print("Execution time :", end - start)