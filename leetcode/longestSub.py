def lengthOfLongestSubstring(s) -> int:
    a = 0
    b = 0
    maxLen = 0
    lst = []

    while (b < len(s)):
        if not(s[b] in lst):
            lst.append(s[b])
            b+=1
            maxLen = max(len(lst), maxLen)
        else:
            lst.remove(s[a])
            a+=1

    return maxLen

print(lengthOfLongestSubstring("hello"))
