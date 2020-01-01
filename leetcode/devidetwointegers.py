def divide(x, y):
    sign = 1
    if x<0 or y<0:
        sign = -1
        

    count = 0
    while ( x >= y):
        x -= y
        count+=1
    return sign * count


print(divide(12, 3))

