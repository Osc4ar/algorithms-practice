class Solution:
    '''
    We can see the filesystem as a stack. An empty stack is equal to the root directory.
    Everytime we move to a new directory, we push that directory to the stack. If we pop the
    current directory we move to the previous one which is the second from the top.

    To simplify the path we can read the absolute path, move the directories to the stack and
    then read the stack to form the directory. We would have the following rules:
    1. If we have a '/' we can ignore the character and continue
    2. If we have a single '.' we can ignore the character and continue
    3. If we have a double '.' we pop from the stack if we have directories on it.
    4. If we have something different, we have to first form a 'word' and if it is not a '.' or '..' we add the directory to the start

    Note: We can move the path until we find something different than a '/', then we form a word until we find
    another '/'. Once the word is created we check the rules and execute the operation.
    '''
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            if path[i] != '/':
                j = i
                word = ''
                while j < len(path) and path[j] != '/':
                    word += path[j]
                    j += 1

                if word == '..':
                    if len(stack):
                        stack.pop()
                elif word != '.':
                    stack.append(word)
                i += len(word)
            else:
                i += 1

        if len(stack) == 0:
            return '/'

        simplified = ''
        for d in stack:
            simplified += '/' + d

        return simplified
