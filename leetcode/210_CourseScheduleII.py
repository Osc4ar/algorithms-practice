class Solution:
    '''
    1. Build an adjacency list with the course and its prereqs
    2. Using DFS, check if we can finish the course, if we can add it to the result
    3. If we find a cycle and it is not possible to finish the courses, return False from DFS
    4. If we finish all courses, return the list with the order the courses were visited
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        result = []
        visited = set()
        def dfs(course: int, path: set) -> bool:
            prereq = adj[course]
            if len(prereq) == 0:
                if course not in visited:
                    visited.add(course)
                    result.append(course)
                return True

            for next_course in prereq:
                if next_course in path:
                    return False

                path.add(next_course)
                if not dfs(next_course, path):
                    return False
                path.remove(next_course)

            adj[course] = []
            result.append(course)
            visited.add(course)
            return True
            

        for course in range(numCourses):
            if not dfs(course, set()):
                return []
        
        return result
