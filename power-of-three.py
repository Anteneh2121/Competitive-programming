class Solution:
	def isPowerOfThree(self, n: int) -> bool:

		power = 0
		number = 3
		
		while True:
			num = number**power
			if num == n:
				return True
			if num > n:
				return False
			else:
				power = power + 1
		return False
