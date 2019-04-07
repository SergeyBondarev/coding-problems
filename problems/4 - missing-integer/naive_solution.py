# it's not a linear time solution
def lowest_positive(arr):
	min_ = min([i for i in arr if i > 0]) - 1

	if min_ > 1:
		return min_ - 1

	i = 2
	while i in arr:
		i += 1

	return i

assert lowest_positive([3, 4, -1, 1]) == 2
assert lowest_positive([1, 2, 0]) == 3



