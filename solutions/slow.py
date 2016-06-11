def solution(x):
    """
    Implementing O(n^2) solution
    """
    result = 0
    for i in range(x):
        for j in range(i + 1):
            result += 1
    return result
