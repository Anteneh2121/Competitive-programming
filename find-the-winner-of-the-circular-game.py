class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = list(range(n, 0, -1))    #Creates list of n to 1
        cur_k = k - 1
        while len(queue) != 1:
            while cur_k != 0:
                queue.insert(0, queue.pop())    #Popping front element and pushing it to the end of queue
                cur_k -= 1
            queue.pop()      #Popping the friend that looses
            cur_k = k - 1    #Resetting
        
        return queue.pop()   #Winner
