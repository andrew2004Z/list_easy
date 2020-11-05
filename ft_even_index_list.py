def ft_len(mass):
    n = 0
    for i in mass:
        n += 1
    return n


def ft_even_index_list(mass):
    a = []
    for i in range(ft_len(mass)):
        if i % 2 == 0:
            a += [mass[i]]
    return a
