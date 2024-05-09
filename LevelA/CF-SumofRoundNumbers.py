def find_sum(num):
    count_ = 0
    num_length = len(str(num)) - 1
    res_list = []
    for ind, digits in enumerate(str(num)):
        # print(ind)
        if digits != "0":
            count_ += 1
            place_value = 10**(num_length - ind)
            res_list.append(int(digits) * place_value)
    print(count_)
    # print(res_list)
    for res in res_list:
        print(res, end=" ")

        
        

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        number = int(input())
        find_sum(number)
        

