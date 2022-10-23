#User function Template for python3
#!/bin/python3

"""
Selection Sort: https://practice.geeksforgeeks.org/problems/selection-sort/1
"""
class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min_index = i
            
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
