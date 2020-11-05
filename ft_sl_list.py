def ft_sl_list(mass):
    n = 0
    for i in range(1, len(mass)):
        if mass[i - 1] < mass[i]:
            n += 1
    return n
