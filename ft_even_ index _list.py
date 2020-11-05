def ft_even_index_list(mass):
    a = []
    l = 0
    for i in mass:
        l += 1
    for i in range(l):
        if i % 2 == 0:
            a.append(mass[i])
    return a
