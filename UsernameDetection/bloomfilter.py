import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):
	def __init__(self, items_count, fp_prob):
		# False possible probability in decimal
		self.fp_prob = fp_prob
		# Size of bit array to use
		self.size = self.get_size(items_count, fp_prob)
		# print(self.size)
		# number of hash functions to use
		self.hash_count = self.get_hash_count(self.size, items_count)

		# Bit array of given size
		self.bit_array = bitarray(self.size)
		# initialize all bits as 0
		self.bit_array.setall(0)

	def add(self, item):
		digests = []
		for i in range(self.hash_count):
			digest = mmh3.hash(item, i) % self.size
			digests.append(digest)

			# set the bit True in bit_array
			self.bit_array[digest] = True
			# print(digest)
		# print(self.bit_array)

	def check(self, item):
		# print(self.bit_array)
		#Check for existence of an item in filter
		for i in range(self.hash_count):
			digest = mmh3.hash(item, i) % self.size
			
			if self.bit_array[digest] == False:
				return False
		return True

	@classmethod
	def get_size(self, n, p):
		m = -(n * math.log(p))/(math.log(2)**2)
		print(m)
		return int(m)

	@classmethod
	def get_hash_count(self, m, n):
		k = (m/n) * math.log(2)
		print(k)
		return int(k)
