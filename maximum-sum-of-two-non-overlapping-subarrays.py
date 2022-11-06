class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefixSum = [0]
        leng = len(nums)
        for n in nums:
            prefixSum.append(prefixSum[-1]+n)
		# maxF[i] means the max subarray sum whose array length is firstLen in the [0, i-1] (closed interval) for nums
		# maxS[i] means the max subarray sum whose array length is secondLen in the [0, i-1] (closed interval) for nums
        maxF, maxS = [0] * (leng+1), [0] * (leng+1)
        ans = [0] * (leng+1)
        ans[firstLen+secondLen] = prefixSum[firstLen+secondLen]
        for i in range(firstLen, leng+1):
            maxF[i] = max(maxF[i-1], prefixSum[i]-prefixSum[i-firstLen])
        for i in range(secondLen, leng+1):
            maxS[i] = max(maxS[i-1], prefixSum[i]-prefixSum[i-secondLen])
        for i in range(firstLen+secondLen+1, leng+1):
            ans[i] = max(ans[i-1], prefixSum[i]-prefixSum[i-firstLen]+maxS[i-firstLen], \
                         prefixSum[i]-prefixSum[i-secondLen]+maxF[i-secondLen])
        return ans[-1]
