import math
import concurrent.futures

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

def arrange_numbers(numbers, chosen, result):
    if len(chosen) == len(numbers):
        result.append(chosen.copy())
    else:
        for n in numbers:
            if n not in chosen and (len(chosen) == 0 or is_perfect_square(chosen[-1] + n)):
                chosen.append(n)
                arrange_numbers(numbers, chosen, result)
                chosen.pop()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for i in range(5):
        future = executor.submit(arrange_numbers, list(range(1, 11)), [], [])
        futures.append(future)

results = []
for future in concurrent.futures.as_completed(futures):
    results += future.result()

print(results)