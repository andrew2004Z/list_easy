def ft_even_index_list(mass):
    a = []
    for i in range(len(mass)):
        if i % 2 == 0:
            a.append(mass[i])
    return a
