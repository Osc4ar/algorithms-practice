class Solution:
    '''
    1. Iterate chars, keep a count of how many times we have seen the current character
    2. Keep the variables: current character, initial index, count and count size
    3. When we change of character we have to check the count
    4. If the count is one, move the initial index to the next character and do not modify the array
    5. If the count is more than one and less than 10, write the size directly
    6. If the count is more than 10, start writing from left to right by dividing the count by 10^(len - 1)
    7. For every chars, if it is the same that the current character, change it to '*' to clean them later
    8. To adjust the char array at the end, we can have two pointers, one in the left searching for astheriscs
    and another looking for values to be moved to the beginning
    '''
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        current = chars[0]
        initial = 0
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == current:
                count += 1
                chars[i] = ''
            else:
                if count > 1:
                    initial += 1
                    count_size = len(f'{count}')
                    for j in range(count_size):
                        base10 = 10**(count_size-1-j)
                        chars[initial+j] = f'{count // base10}'
                        count = count % base10
                current = chars[i]
                initial = i
                count = 1
        
        if count > 1:
            initial += 1
            count_size = len(f'{count}')
            for j in range(count_size):
                base10 = 10**(count_size-1-j)
                chars[initial+j] = f'{count // base10}'
                count = count % base10

        writer = 0
        while writer < len(chars) and chars[writer] != '':
            writer += 1

        for reader in range(writer, len(chars)):
            if chars[reader] != '':
                chars[writer] = chars[reader]
                chars[reader] = ''
                while writer <= reader and chars[writer] != '':
                    writer += 1
        
        end = len(chars)
        for i in range(len(chars)):
            if chars[i] == '':
                end = i
                break

        for _ in range(end, len(chars)):
            chars.pop()

        return len(chars)
