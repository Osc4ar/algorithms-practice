class Solution:
    '''
    We can read the arrays and build a list of the websites visited by each user:

    {
        'joe': ['home', 'about', 'career'],
        'james': ['home', 'cart', 'maps', 'home'],
        'mary': ['home', 'about', 'career']
    }

    We can discard any user with less than 3 websites visited. For the others:
    1. Make tuples of tree elements with the websites visited
    2. Check any combination of them, register them in a score dictionary where the key is the tuple
    and the value the scores
    3. Get the tuple with the highest score, if there are more than one return the lexicographically smallest

        *       *              *
    ['home', 'cart', 'maps', 'home']
    [0, 1, 2]
    [0, 1, 3]
    [0, 2, 3]
    [1, 2, 3]
    '''
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
        tuples_by_score = defaultdict(int)
        for user, websites in websites_by_user.items():
            for i in range(len(websites) - 2):
                for j in range(i + 1, len(websites) - 1):
                    for k in range(j + 1, len(websites)):
                        t = (websites[i], websites[j], websites[k])
                        if t not in tuples_by_user[user]:
                            tuples_by_user[user].add(t)
                            tuples_by_score[t] += 1

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
