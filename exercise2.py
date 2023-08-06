import heapq

k = [1,2,3,4,5,6,7]

y = list(map(lambda x: x+1, k ))

print(y)

while k :
    y.append(k)

print(y)

def solution(numbers) :
    heapq.heapify(numbers)
