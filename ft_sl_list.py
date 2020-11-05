def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l


def ft_sl_list(mass):
    n = 0
    for i in range(1, ft_len(mass)):
        if mass[i - 1] < mass[i]:
            n += 1
    return n
