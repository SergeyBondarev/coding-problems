import sys

if sys.version_info >= (3,8):
	from math import prod
else:
	from functools import reduce
	import operator

	def prod(arr):
		return reduce(operator.mul, arr, 1)


def product_array(arr):
	prod_all = prod(arr)
	return [prod_all // i for i in arr]

assert product_array([1,2,3]) == [6,3,2]
assert product_array([1,2,3,4,5]) == [120,60,40,30,24]
