class Solution(object):
    def longestPalindrome(self, s):

        maxLen = 0
        start = 0
        end = 0

        if (len(s) == 1):
            return s
        
        for i in range(1, len(s)):
            
            length = 1

            j = i - 1
            k = i + 1

            while True:
                if j < 0 or k > len(s) - 1:
                    if (length > maxLen):
                        maxLen = length
                        start = j+1
                        end = k-1
                    break
                if j == 0 and k == len(s) - 1 and s[k] == s[j]:
                    start = 0
                    end = len(s)-1
                    maxLen = len(s)
                    break
                if s[k] != s[j]:
                    if (length > maxLen):
                        maxLen = length
                        start = j+1
                        end = k-1
                    break
                else:
                    length += 2
                    j -= 1
                    k += 1

        for i in range(0, len(s)-1):
            
            if (s[i] == s[i+1]):
                if (maxLen < 2):
                    start = i
                    end = i + 1


                length = 2

                j = i - 1
                k = i + 2

                while True:
                    if j < 0 or k > len(s) - 1:
                        if (length > maxLen):
                            maxLen = length
                            start = j+1
                            end = k-1
                        break
                    if j == 0 and k == len(s) - 1 and s[k] == s[j]:
                        start = 0
                        end = len(s)-1
                        maxLen = len(s)
                        break
                    if s[k] != s[j]:
                        if (length > maxLen):
                            maxLen = length
                            start = j+1
                            end = k-1
                        break
                    else:
                        length += 2
                        j -= 1
                        k += 1

        return s[start:end+1]




sln = Solution()
print(sln.longestPalindrome("adam"))