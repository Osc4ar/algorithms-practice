class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        time_websites_by_user = defaultdict(list)
        count_by_user = defaultdict(int)
        for i in range(len(username)):
            time_websites_by_user[username[i]].append((timestamp[i], website[i]))
            count_by_user[username[i]] += 1

        for user, count in count_by_user.items():
            if count < 3:
                time_websites_by_user.pop(user)

        websites_by_user = defaultdict(list)
        for user, websites in time_websites_by_user.items():
            for _, website in sorted(websites):
                websites_by_user[user].append(website)

        tuples_by_user = defaultdict(set)
        tuples_by_score = Counter()
        for user, websites in websites_by_user.items():
            combs = set(combinations(websites, 3))
            tuples_by_score.update(combs)

        max_tuples = []
        max_score = float('-inf')
        for t, score in tuples_by_score.items():
            if score > max_score:
                max_tuples = [t]
                max_score = score
            elif score == max_score:
                max_tuples.append(t)

        if len(max_tuples) > 1:
            max_tuples.sort()
            return max_tuples[0]
        return max_tuples[0] 
