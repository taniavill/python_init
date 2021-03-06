def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def sum_all(*arr):
    if len(arr) == 0:
        return 0

    nums = arr[0] if isinstance(arr[0], list) else arr
    return sum(nums)

def most_popular(arr):
    repetitions = {}
    max_repetition = 0
    popular = None
    for numb in arr:
        if numb not in repetitions:
            repetitions[numb] = 1
        else:
            repetitions[numb] += 1
        if repetitions[numb] > max_repetition:
            max_repetition = repetitions[numb]
            popular = numb
        if repetitions[numb] == max_repetition:
            popular = numb if numb < popular else popular
    return popular

    
def is_prime(n):
    pass