class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        for course, prereq in prerequisites:
            adjacency[course].append(prereq)

        def dfs(course: int, taken: set) -> bool:
            if course in taken:
                return False

            prereqs = adjacency[course]
            if len(prereqs) == 0:
                return True
            
            taken.add(course)
            for prereq in prereqs:
                if prereq in taken:
                    return False

                if not dfs(prereq, taken):
                    return False
            taken.remove(course)

            adjacency[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True
