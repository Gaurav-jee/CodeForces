if __name__ == "__main__":
    matrix  = []
    i = -1
    j = -1

    for _ in range(5):
        #row = list(map(int, input().split()))
        row = list(map(int, input().split()))
        # print(list(x for x in row))
        matrix.append(row)

    for row in matrix:
        if 1 in row:
            i = row.index(1)
        

    for col in list(zip(*matrix)):
        if 1 in col:
            j = col.index(1)


    # if i == 2 and j == 2:
    #     print(0)
    print(abs(i-2) + abs(j-2))


