def solution(ingredient):
    str_ingredient = ''.join(map(str,ingredient))

    count = 0

    while True :
        count += str_ingredient.count('1231')
        tmp = str_ingredient.replace('1231','')
        str_ingredient = ''
        str_ingredient += tmp

        if str_ingredient.count('1231') == 0 :
            break

    return count

print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))

