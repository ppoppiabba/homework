from collections import deque
def solution(prices):
    result = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1 
                break
            count += 1
        result.append(count)
    return result
prices = [1, 2, 3, 2, 3]
result = solution(prices)
print(result)
