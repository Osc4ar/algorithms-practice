class Solution:
    '''
    1. Build adjacency list of the course and its dependencies
    2. Iterate all courses from 0 to numCourses - 1
    3. For every course, using DFS check if we can complete the course, by following all prerequisites
    4. A course is possible to complete if it does not have a prerequesite or there is no cycle on it
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        completed = set()

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course: int, path: set):
            if course in completed:
                return True

            if course in path:
                return False

            path.add(course)
            for prereq in adj[course]:
                if not dfs(prereq, path):
                    return False

            path.remove(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True
