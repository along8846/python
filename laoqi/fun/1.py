def fibs(n):
    """
    This is a Fibonacci sequence.
    """
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result
fibs.__doc__

if __name__ == "__main__":
    lst = fibs(3)
    print(lst)
    fibs.__doc__