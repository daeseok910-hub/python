def solution(ingredient):
    count = 0
    i = 0
    while i < len(ingredient)-3:
        if ingredient[i:i+4] == [1,2,3,1]:
            count +=1
            del ingredient[i:i+4]
            if i < 4:
                i = 0
            else:
                i -= 3
        else:
            i += 1

    return count