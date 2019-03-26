inp = [int(i) for i in input().split()]
k = int(input())

def two_sum(arr, k):
	for i in inp:
		for j in inp:
			if i + j == k:
				return True

	return False

print(two_sum(inp, k))