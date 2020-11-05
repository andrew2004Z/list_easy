def ft_len(mass):
    l = 0
    for i in mass:
        l += 1
    return l

def ft_rev_par_list(mass):
    a = []
    if ft_len(mass) % 2 == 0:
        for i in range(1, ft_len(mass), 2):
            a.append(mass[i])
            a.append(mass[i - 1])
    elif ft_len(mass) % 2 == 1:
        for i in range(1, ft_len(mass) - 1, 2):
            a.append(mass[i])
            a.append(mass[i - 1])
        a.append(mass[-1])
    return a
