class Solution:
    '''
    1: {0},
    2: {0},
    3: {1, 2}

    1. Create an adjacency list of the course and its required courses. Also save a set with the courses without
       prerequesites.
    2. We can save a set of "taken" courses, the initial values are the courses with no prerequesites.
    3. While the taken courses are less than the numCourses check which courses we can take.
    4. If we can take a course, we add the course to the taken set and remove it from the HashMap
    5. If we did not added a new course, it means we cannot complete the courses
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prequisites_by_course = defaultdict(set)
        taken_courses = set(range(numCourses))

        for course, prerequisite in prerequisites:
            prequisites_by_course[course].add(prerequisite)
            taken_courses.discard(course)

        last_size = None
        current_size = len(taken_courses)
        result = list(taken_courses)
        while current_size < numCourses:
            if last_size == current_size:
                return []

            courses_to_remove = set()
            for course, prerequisite in prequisites_by_course.items():
                if prerequisite.issubset(taken_courses):
                    result.append(course)
                    taken_courses.add(course)
                    courses_to_remove.add(course)

            for course in courses_to_remove:
                prequisites_by_course.pop(course)

            last_size = current_size
            current_size = len(taken_courses)

        return result
