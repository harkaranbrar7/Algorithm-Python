
def solution(numbers):
    if len(numbers) == 0:
        return 0
    numbers.sort()
    return numbers[-1]


    