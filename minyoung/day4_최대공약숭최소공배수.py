def solution(n, m):
    gcd = 0
    for i in range(1, max(n, m)):
        if n % i == 0 and m % i == 0:
            gcd = i

    return gcd, int(n * m / gcd)
