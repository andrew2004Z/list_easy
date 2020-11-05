def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_rshift_list(mass):
    n = ft_len(mass)
    p = mass[n - 1]
    for i in range(0, n):
        x = n - i - 1
        mass[x] = mass[x - 1]
    mass[0] = p
    return mass
