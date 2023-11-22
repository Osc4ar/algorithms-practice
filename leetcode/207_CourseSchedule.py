class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_and_prerequesites = {}

        for course, prerequesite in prerequisites:
            if course not in course_and_prerequesites:
                course_and_prerequesites[course] = [prerequesite]
            else:
                course_and_prerequesites[course].append(prerequesite)

            if prerequesite not in course_and_prerequesites:
                course_and_prerequesites[prerequesite] = []
            elif self.checkInvalidLoop(prerequesite, course, course_and_prerequesites):
                return False

        return self.validateCourses(course_and_prerequesites)


    def checkInvalidLoop(self, prerequesite: int, course: int, course_and_prerequesites: dict[int, list[int]]) -> bool:
        prerequesites_of_prerequesite = course_and_prerequesites[prerequesite]

        return course in prerequesites_of_prerequesite

    def validateCourses(self, course_and_prerequesites: dict[int, list[int]]) -> bool:
        if len(course_and_prerequesites) == 0:
            return True

        for course in course_and_prerequesites:
            if self.invalidCycle(course, course_and_prerequesites):
                return False

        return True
                
    def invalidCycle(self, course: int, course_and_prerequesites: dict[int, list[int]]) -> bool:
        visited = set()
        next_courses = deque()

        visited.add(course)
        next_courses.append(course)
        while next_courses:
            for _ in range(len(next_courses)):
                current_course = next_courses.popleft()

                if current_course not in course_and_prerequesites:
                    continue

                for prerequesite in course_and_prerequesites[current_course]:
                    if course == prerequesite:
                        return True

                    if prerequesite not in visited:
                        next_courses.append(prerequesite)
                        visited.add(prerequesite)

        return False