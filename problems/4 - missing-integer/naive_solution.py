# it's not a linear time solution
def lowest_positive(arr):
	max_ = max(arr)
	if max_ <= 0:
		return 1

	min_ = min([i for i in arr if i > 0]) - 1

	if min_ > 1:
		return min_ - 1

	i = 2
	while i in arr:
		i += 1

	return i

assert lowest_positive([3, 4, -1, 1]) == 2
assert lowest_positive([1, 2, 0]) == 3
assert lowest_positive([-1,-2,-3]) == 1



