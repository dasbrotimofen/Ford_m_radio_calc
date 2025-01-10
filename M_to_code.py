lookup_table = [
    [9, 5, 3, 4, 8, 7, 2, 6, 1, 0],
    [2, 1, 5, 6, 9, 3, 7, 0, 4, 8],
    [0, 4, 7, 3, 1, 9, 6, 5, 8, 2],
    [5, 6, 4, 1, 2, 8, 0, 9, 3, 7],
    [6, 3, 1, 2, 0, 5, 4, 8, 7, 9],
    [4, 0, 8, 7, 6, 1, 9, 3, 2, 5],
    [7, 8, 0, 5, 3, 2, 1, 4, 9, 6],
    [1, 9, 6, 8, 7, 4, 5, 2, 0, 3],
    [3, 2, 9, 0, 4, 6, 8, 7, 5, 1],
    [8, 7, 2, 9, 5, 0, 3, 1, 6, 4]
]

def calculate_r_values(serial):
    n_values = [int(digit) for digit in serial[1:]]
    r_values = []
    indices = [
        n_values[5] * 10 + 5,
        n_values[4] * 10 + 3,
        n_values[3] * 10 + 8,
        n_values[2] * 10 + 2,
        n_values[1] * 10 + 1,
        n_values[0] * 10 + 6,
        0 * 10 + 9
    ]
    for idx in indices:
        if idx < 0 or idx >= 100:
            raise IndexError(f"Index {idx} out of range for lookup_table.")
        r_values.append(lookup_table[idx // 10][idx % 10])
    return r_values

def calculate_res_values(r):
    def lsd(value):
        return value % 10

    res1 = lsd((lookup_table[r[1]][r[0]] + 1) * (lookup_table[r[5]][r[1]] + 1) +
               (lookup_table[r[3]][r[2]] + 1) * (lookup_table[r[6]][r[4]] + 1) +
               lookup_table[r[0]][r[3]])
    res2 = lsd((lookup_table[r[1]][r[0]] + 1) * (lookup_table[r[4]][r[3]] + 1) +
               (lookup_table[r[4]][r[1]] + 1) * (lookup_table[r[6]][r[2]] + 1) +
               lookup_table[r[0]][r[5]])
    res3 = lsd((lookup_table[r[1]][r[0]] + 1) * (lookup_table[r[3]][r[1]] + 1) +
               (lookup_table[r[2]][r[5]] + 1) * (lookup_table[r[6]][r[3]] + 1) +
               lookup_table[r[0]][r[4]])
    res4 = lsd((lookup_table[r[1]][r[0]] + 1) * (lookup_table[r[5]][r[2]] + 1) +
               (lookup_table[r[2]][r[6]] + 1) * (lookup_table[r[1]][r[4]] + 1) +
               lookup_table[r[3]][r[0]])
    return res1, res2, res3, res4

def calculate_xres_values(res, r):
    xres1 = (lookup_table[res[0]][5] + 1) * (lookup_table[res[1]][1] + 1) + 105
    xres2 = (lookup_table[res[1]][1] + 1) * (lookup_table[res[3]][0] + 1) + 102
    xres3 = (lookup_table[res[0]][5] + 1) * (lookup_table[res[2]][8] + 1) + 103
    xres4 = (lookup_table[res[2]][8] + 1) * (lookup_table[res[3]][0] + 1) + 108
    return xres1, xres2, xres3, xres4

def calculate_code(xres, r):
    def lsd(value):
        return value % 10

    code = [
        lsd((xres[3] // 10) + (xres[3] % 10) + r[0]),
        lsd((xres[2] // 10) + (xres[2] % 10) + r[0]),
        lsd((xres[1] // 10) + (xres[1] % 10) + r[0]),
        lsd((xres[0] // 10) + (xres[0] % 10) + r[0])
    ]
    return ''.join(map(str, code))

def main():
    serial = "M151704"
    r_values = calculate_r_values(serial)
    res_values = calculate_res_values(r_values)
    xres_values = calculate_xres_values(res_values, r_values)
    code = calculate_code(xres_values, r_values)
    print("Code:", code)

if __name__ == "__main__":
    main()
