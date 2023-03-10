import random, time
numberPool, winningNumbers, allTickets = [], [], []
for i in range(1, 60):
    numberPool.append(i)

for i in range(2500):
    oneTicket = []
    for i in range(6):    
        oneNumber = random.choice(numberPool)
        oneTicket.append(oneNumber)
        numberPool.remove(oneNumber)
    oneTicket.sort()
    #print (oneTicket)
    allTickets.append(oneTicket)
    numberPool = []
    for i in range(1, 60):
        numberPool.append(i)

for i in range(6):
    oneNumber = random.choice(numberPool)
    winningNumbers.append(oneNumber)
    numberPool.remove(oneNumber)
winningNumbers.sort()

print ("Tonights winning numbers are...", winningNumbers)
for i in range(25):
    numbersMatched = len(set(allTickets[i]) & set(winningNumbers))#new
    if numbersMatched == 0 or numbersMatched == 1:
        print ("You win £0 with",allTickets[i] )
    if numbersMatched == 2:
        print ("You win a free ticket with",allTickets[i])
    if numbersMatched == 3:
        print ("You win £30 with",allTickets[i])
    if numbersMatched == 4:
        print ("You win £140 with",allTickets[i])
    if numbersMatched == 5:
        print ("You win £7500 with",allTickets[i])
    if numbersMatched == 6:
        print ("You win £1000000 with",allTickets[i])
    time.sleep(0.25)

