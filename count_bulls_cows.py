def count_bulls_cows(answer, user_input):


    bulls = 0
    cows = 0

    for i in range(4):
        if answer[i] == user_input[i]:
            bulls += 1

    print(bulls)
    print(cows)
            
    return bulls, cows


## main
count_bulls_cows('1564', '1634')