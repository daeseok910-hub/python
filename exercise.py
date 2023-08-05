Column_num1 = []
Column_num2 = []
Column_num3 = []

def move(a,b) :

    x = a[len(a)-1]
    b.append(x)
    a.pop()



def solution(n):

    for num in range(0, n):
        Column_num1.append(num)
    Column_num1.reverse()

    answer = [[]]

    return Column_num1

solution(10)
move(Column_num1,Column_num2)
print(Column_num1)
print(Column_num2)