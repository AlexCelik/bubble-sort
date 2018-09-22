number = [10,3,5,1,6,7,8,4,2,9]
for loopAgain in range(len(number)-1):
    for counter in range(len(number)-1):
        if number[counter+1] < number[counter]:
            temp = number[counter]
            number[counter] = number[counter+1]
            number[counter+1] = temp
        print(number)
        print(counter)
        print(loopAgain)