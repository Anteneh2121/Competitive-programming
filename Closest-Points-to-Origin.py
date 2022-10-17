import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        for i in points:
            heapq.heappush(distance,(i[0]**2+i[1]**2,i))
        K_points = []
        for i in range(K):
            K_points.append(heapq.heappop(distance)[1])
        return K_points
