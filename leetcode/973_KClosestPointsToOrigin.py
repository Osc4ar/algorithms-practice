class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.calculateDistance(point), point) for point in points]

        heapq.heapify(distances)

        result = []
        for i in range(k):
            distance_and_point = heapq.heappop(distances)
            result.append(distance_and_point[1])

        return result

    def calculateDistance(self, point: List[int]) -> float:
        return math.sqrt(point[0]**2 + point[1]**2)