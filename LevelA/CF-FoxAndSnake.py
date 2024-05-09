
row, col = map(int, input().split())

# print(row, col)
drawing = []
flag = True 

for ri in range(row):
    # print(ri % 2)
    if ri % 2 == 0:
        curr_row = ["#"] * col
    elif flag is True:
        curr_row = ["."] * col
        curr_row[col - 1] = "#" 
        flag = False
    else:
        curr_row = ["."] * col
        curr_row[0] = "#" 
        flag = True
    drawing.append(curr_row)

for i in drawing:
    for j in i:
        print(j, end="")
    print("")
    