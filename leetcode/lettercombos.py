def letterCombinations(digits):
    lst = [['a','b','c'],
           ['d','e','f'],
           ['g','h','i'],
           ['j','k','l'],
           ['m','n','o'],
           ['p','q','r', 's'],
           ['t','u','v'],
           ['w','x','y','z']]
    sub=[]
    s = ''
    if len(digits) == 1:
        return lst[int(digits[0])-2]

    n = 1
    current = lst[int(digits[0])-2]
    mergeW = []
    n = 0
    while n < len(digits) - 1:
        n+=1
        mergeW = lst[int(digits[n])-2]
        current = combiner(current, mergeW)
        sub = current
        
    return current


def combiner(x,y):
    lst = []
    s = ''
    for i in x:
        for j in y:
            s = s.join([i,j])
            lst.append(s)
            s = ''
    return lst


print(letterCombinations("23456"))
            
