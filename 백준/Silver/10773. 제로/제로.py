capacity = int(input())
array = [None] * capacity
top, res = -1, 0

for _ in range(capacity):
    n = int(input())
    if n == 0: top -= 1
    else:
        top += 1
        array[top] = n
print(sum(array[0:top+1]))