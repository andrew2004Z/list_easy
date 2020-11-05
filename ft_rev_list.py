def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_rev_list(num):
    n = ft_len(num) // 2
    for i in range(0, n):
        a = -1 * (i + 1)
        t = num[i]
        num[i] = num[a]
        num[a] = t
    return num
