bin_amout = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]


playing = True

player_1 = True

messageCode = 0

giveawayPile = -1

lastrecipient = -1

chosenBin = -1

while (playing):

    message = ''
    if player_1 and messageCode == 0:
        message = "Player One's turn..."
    elif not(player_1) and messageCode == 0:
        message = "Player Two's turn..."
    elif player_1 and messageCode == -2:
        message = 'Invalid input. Try again, Player One'
    elif not(player_1) and messageCode == -2:
        message = 'Invalid input. Try again, Player Two'
    elif player_1 and messageCode == -1:
        message = "You must choose a non-empty bin, Player One."
    elif not(player_1) and messageCode == -1:
        message = "You must choose a non-empty bin, Player Two."
    print()
    print(message)
    print()
    messageCode = 0

    i = 0
    for element in bin_amout:
        bin_amout[i] = int(bin_amout[i])
        if int(bin_amout[i]) < 10:
            bin_amout[i] = ' ' + str(bin_amout[i])
        else:
            bin_amout[i] = str(bin_amout[i])
        i += 1
    #end of the  for loop

    if not(player_1):
        print('        a    b    c    d    e    f')
    print('+----+----+----+----+----+----+----+----+')
    print('|    | '+ bin_amout[12]+ ' | '+ bin_amout[11]+ ' | '+ bin_amout[10]+ ' | '+ bin_amout[9]+ ' | '+ bin_amout[8]+ ' | '+ bin_amout[7]+ ' |    |')
    print('| '+ bin_amout[13]  +' |----+----+----+----+----+----| '+ bin_amout[6]  +' |')  
    print('|    | '+ bin_amout[0]+ ' | '+ bin_amout[1]+ ' | '+ bin_amout[2]+ ' | '+ bin_amout[3]+ ' | '+ bin_amout[4]+ ' | '+ bin_amout[5]+ ' |    |')
    print('+----+----+----+----+----+----+----+----+')
    if player_1:
        print('        f    e    d    c    b    a')
    print()

    userinput = input("Enter the letter to choose a bin or enter 'q' to QUIT the game: ")


    if userinput == 'q':
        break
    elif player_1 and userinput == 'a':
        chosenBin = 5
    elif player_1 and userinput == 'b':
        chosenBin = 4
    elif player_1 and userinput == 'c':
        chosenBin = 3
    elif player_1 and userinput == 'd':
        chosenBin = 2
    elif player_1 and userinput == 'e':
        chosenBin = 1
    elif player_1 and userinput == 'f':
        chosenBin = 0
    elif not(player_1) and userinput == 'a':
        chosenBin = 12
    elif not(player_1) and userinput == 'b':
        chosenBin = 11
    elif not(player_1) and userinput == 'c':
        chosenBin = 10
    elif not(player_1) and userinput == 'd':
        chosenBin = 9
    elif not(player_1) and userinput == 'e':
        chosenBin = 8
    elif not(player_1) and userinput == 'f':
        chosenBin = 7
    else:
        chosenBin = -2
        messageCode = -2 #invalid input
    
    if int(chosenBin) >= 0:
        giveawayPile = bin_amout[chosenBin]
        bin_amout[chosenBin] = 0
        if int(giveawayPile) <= 0:
            messageCode = -1 #empty bin was chosen
    
    recipient = chosenBin + 1
    while (int(giveawayPile) > 0):
        if player_1 and int(recipient) == 13:
            recipient = 0
        if not(player_1) and int(recipient) == 6:
            recipient = 7
        
        bin_amout[recipient] = int(bin_amout[recipient]) + 1
        giveawayPile = int(giveawayPile) -1

        if int(giveawayPile) == 0:
            lastrecipient = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0

    if player_1 and int(lastrecipient) == 6:
        player_1 = True
    elif player_1 and int(bin_amout[lastrecipient]) == 1 and int(lastrecipient) < 6:
        bin_amout[6] = int(bin_amout[6]) + int(bin_amout[lastrecipient]) + int(bin_amout[12 - int(lastrecipient)])
        bin_amout[lastrecipient] = 0
        bin_amout[12 - int(lastrecipient)] = 0
        player_1 = not(player_1)
    elif not(player_1) and int(lastrecipient) == 13:
        player_1 = False
    elif not(player_1) and int(bin_amout[lastrecipient]) == 1 and int(lastrecipient) > 6:
        bin_amout[13] = int(bin_amout[13]) + int(bin_amout[lastrecipient]) + int(bin_amout[12 - int(lastrecipient)])
        bin_amout[lastrecipient] = 0
        bin_amout[12 - int(lastrecipient)] = 0
        player_1 = not(player_1)
    elif int(messageCode) >= 0:
        player_1 = not(player_1)
    
    # check for end of the game
    sideone = 0
    sidetwo = 0
    for j in range(6):
        sideone = int(sideone) + int(bin_amout[j])
        sidetwo = int(sidetwo) + int(bin_amout[j+7])

    if int(sideone) == 0 or int(sidetwo) == 0:
        playing = False
        bin_amout[6] = int(bin_amout[6]) + int(sideone)
        bin_amout[13] = int(bin_amout[13]) + int(sidetwo)
        for k in range(6):
            bin_amout[k] = 0
            bin_amout[k+7] = 0


#end of while loop
print()
print("That's enough!")
if int(bin_amout[13]) < int(bin_amout[6]):
    print('We have a winner!')
    print('Player One victory')
elif int(bin_amout[13]) > int(bin_amout[6]):
    print('We have a winner!')
    print('Player Two victory')
else:
    print('Tie')

i = 0
for element in bin_amout:
    bin_amout[i] = int(bin_amout[i])
    if int(bin_amout[i]) < 10:
        bin_amout[i] = ' ' + str(bin_amout[i])
    else:
        bin_amout[i] = str(bin_amout[i])
    i += 1
    #end of the  for loop

print()
print('+----+----+----+----+----+----+----+----+')
print('|    | '+ bin_amout[12]+ ' | '+ bin_amout[11]+ ' | '+ bin_amout[10]+ ' | '+ bin_amout[9]+ ' | '+ bin_amout[8]+ ' | '+ bin_amout[7]+ ' |    |')
print('| '+ bin_amout[13]  +' |----+----+----+----+----+----| '+ bin_amout[6]  +' |')  
print('|    | '+ bin_amout[0]+ ' | '+ bin_amout[1]+ ' | '+ bin_amout[2]+ ' | '+ bin_amout[3]+ ' | '+ bin_amout[4]+ ' | '+ bin_amout[5]+ ' |    |')
print('+----+----+----+----+----+----+----+----+')