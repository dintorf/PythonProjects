def answer(population, x, y, strength):
    # your code here
    rows = len(population)
    cols = len(population[0])

    patients_unchecked = [(x,y)]
    patients_checked = []

    # function to loop through unchecked patients
    def next():
        for patient in patients_unchecked:
            yield patient

    for x, y in next():
        patient_z = population[y][x]

        if patient_z <= strength:
            # append patient location to unchecked patients
            patients_checked.append((x,y))
            # infect patient in population
            population[y][x] = -1

            # check bounds of adjacent patients
            # if in bounds, add patient location to unchecked patients
            if x-1 >= 0 and (x-1, y) not in patients_checked:
                patients_unchecked.append((x-1, y))
            if x+1 < cols and (x+1, y) not in patients_checked:
                patients_unchecked.append((x+1, y,))
            if y-1 >= 0 and (x, y-1) not in patients_checked:
                patients_unchecked.append((x, y-1))
            if y+1 < rows and (x, y+1) not in patients_checked:
                patients_unchecked.append((x, y+1))

    return population
