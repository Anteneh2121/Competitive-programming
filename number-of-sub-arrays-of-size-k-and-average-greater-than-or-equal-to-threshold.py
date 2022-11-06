class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter, currSum, check = 0, sum(arr[:k -1]), 1
        for i in range(k -1, len(arr)):
            currSum += arr[i]
            
            if check:
                check = 0
            else:
                currSum -= arr[i-k]
                
            if currSum // k >= threshold:
                counter += 1
        return counter
                
