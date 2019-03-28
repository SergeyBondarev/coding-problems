inp = [int(i) for i in input().split()]
k = int(input())

def binary_search(sorted_arr, x):
	left, right = -1, len(sorted_arr)

	while right > left + 1:
		mid = (left + right) // 2
		if sorted_arr[mid] > x:
			right = mid
		elif sorted_arr[mid] < x:
			left = mid
		else:
			return mid

	# not found
	return -1

# some tests just to be sure binary search is working
assert binary_search([1,2,3,4,5],3) == 2
assert binary_search([-1,2,5,10,12],10) == 3
assert binary_search([-1,2,5,10,12],-1) == 0
assert binary_search([-1,2,5,10,12],12) == 4
assert binary_search([-1,2,5,10,12],13) == -1

def two_sum(arr, k):
	sorted_arr = list(sorted(arr))

	for i in sorted_arr:
		if binary_search(sorted_arr, k-i) != -1:
			return True
		
	return False


print(two_sum(inp, k))