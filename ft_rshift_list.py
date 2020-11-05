def ft_rshift_list(mass):
    a = []
    p = mass[-1]
    a.append(p)
    for i in range(len(mass) - 1):
        a.append(mass[i])
    return a
