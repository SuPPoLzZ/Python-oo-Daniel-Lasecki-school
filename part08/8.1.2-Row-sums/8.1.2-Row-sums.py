def row_sums(matrice):
    for row in matrice:
        summ = sum(row)
        row.append(summ)


matrice = [[1, 2], [3, 4]]
row_sums(matrice)
print(matrice)