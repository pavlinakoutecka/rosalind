

def compute_multinacci(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return compute_multinacci(n-1, k) + k*compute_multinacci(n-2, k)


n, k = 32, 3
number_of_rabbit_pairs = compute_multinacci(n,k)
print(number_of_rabbit_pairs)
