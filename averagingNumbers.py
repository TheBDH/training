def myAvg(l):
	s = 0
	for i in l:
		s += i
	return s / len(l)
nums = [1, 2, 3, 4, 5]
print myAvg(nums)