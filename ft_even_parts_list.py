def ft_even_parts_list(mass):
    a = []
    for i in mass:
        if i % 2 == 0:
            a.append(i)
    return a
