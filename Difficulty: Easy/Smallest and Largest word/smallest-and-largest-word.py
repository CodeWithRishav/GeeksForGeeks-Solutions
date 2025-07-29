class Solution:

    def smallerAndLarge(self, s: str):
        size = len(s)
        end = 0
        temp = []
        smaller = ""
        large = ""
        min_length = float('inf')
        max_length = 0

        while end < size:
            if s[end] == ' ':
                if temp:
                    word = ''.join(temp)
                    if len(word) < min_length:
                        min_length = len(word)
                        smaller = word
                    if len(word) > max_length:
                        max_length = len(word)
                        large = word
                    elif len(word) == max_length:
                        large = word
                    temp = []
            else:
                temp.append(s[end])
            end += 1

        if temp:
            word = ''.join(temp)
            if len(word) < min_length:
                min_length = len(word)
                smaller = word
            if len(word) > max_length:
                max_length = len(word)
                large = word
            elif len(word) == max_length:
                large = word

        return [smaller, large]