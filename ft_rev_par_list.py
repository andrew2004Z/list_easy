def ft_rev_par_list(mass):
    a = []
    if len(mass) % 2 == 0:
        for i in range(1, len(mass), 2):
            a.append(mass[i])
            a.append(mass[i - 1])
    elif len(mass) % 2 == 1:
        for i in range(1, len(mass) - 1, 2):
            a.append(mass[i])
            a.append(mass[i - 1])
        a.append(mass[-1])
    return a
