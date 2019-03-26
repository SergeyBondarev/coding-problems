inp = [int(i) for i in input().split()]
k = int(input())

def two_sum(arr, k):
	for i in arr:
		for j in arr:
			if i + j == k:
				return True

	return False

print(two_sum(inp, k))