def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_rshift_list(mass):
    a = []
    p = mass[-1]
    a.append(p)
    for i in range(ft_len(mass) - 1):
        a.append(mass[i])
    return a
