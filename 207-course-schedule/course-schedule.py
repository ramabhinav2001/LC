class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        
        for course, ip in prerequisites:
            pre[course].append(ip)
        taken=set()

        def dfs(course):
            if not pre[course]:
                return True

            if course in taken:
                return False
            taken.add(course)

            for ip in pre[course]:
                if not dfs(ip):
                    return False
            taken.remove(course)
            pre[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True