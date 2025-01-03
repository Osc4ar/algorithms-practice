class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        frequencies = Counter(tasks)

        for task, f in frequencies.items():
            heapq.heappush(heap, (-1*f, task))

        queue = deque()
        count = 0
        while heap or queue:
            count += 1
            if heap:
                f, task = heapq.heappop(heap)
                f += 1
                if f < 0:
                    queue.append((count + n, (f, task)))

            if queue and queue[0][0] <= count:
                _, task_freq = queue.popleft()
                heapq.heappush(heap, task_freq)

        return count
