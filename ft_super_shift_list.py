def ft_super_shift_list(mass, n):
    if n > 0:
        mass1 = mass
        for i in range(n):
            a = []
            p = mass1[-1]
            a.append(p)
            for i in range(len(mass1) - 1):
                a.append(mass1[i])
            mass1 = a
        return mass1
    elif n == 0:
        return mass
    elif n < 0:
        mass1 = mass
        n = n * -1
        for i in range(n):
            a = []
            p = mass1[0]
            for i in range(1, len(mass1)):
                a.append(mass1[i])
            mass1 = a
            mass1.append(p)
        return mass1
