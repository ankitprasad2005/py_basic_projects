import math

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

def arrange_numbers(start, end, result):
    if len(result) == end - start + 1:
        return result
    for i in range(start, end + 1):
        if i not in result:
            if len(result) == 0 or is_perfect_square(result[-1] + i):
                result.append(i)
                if arrange_numbers(start, end, result):
                    return result
                result.pop()
    return None
inp1 = int(input())
result = arrange_numbers(1, inp1, [])
print(result)
