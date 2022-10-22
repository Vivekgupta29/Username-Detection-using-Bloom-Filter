from bloomfilter import BloomFilter
from random import shuffle
from pandas import *

data = read_csv("usernames.csv")
username = data['username'].tolist()
word_present = username

word = str(input("Enter the Username You want to Choose : "))

n = len(word_present) #no of items to add
p = 0.05 #false positive probability

bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp_prob))
print("Number of hash functions:{}".format(bloomf.hash_count))

for item in word_present:
	bloomf.add(item)

if bloomf.check(word):
		print("'{}' Username Already Exists!".format(word))
else:
	print("'{}' is Available!".format(word))
