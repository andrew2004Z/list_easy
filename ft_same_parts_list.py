def ft_same_parts_list(mass):
    for i in range(len(mass) - 1):
        if mass[i] < 0 and mass[i + 1] < 0:
            return True
        elif mass[i] > 0 and mass[i + 1] > 0:
            return True
        else:
            return False
