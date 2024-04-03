import random

players = ['Martin', 'Craig', 'Sue', 'Claire', 'Dave', 'Alice',
           'Luciana', 'Harry', 'Jack', 'Rose', 'Lexi', 'Maria',
           'Thomas', 'James', 'William', 'Ada', 'Grace', 'Jean',
           'Marissa', 'Alan']

print('Welcome to Team Allocator!')

while True: 

    random.shuffle(players)

    response = input('Is it a team or individual sport? \
                     \nType team or individual: ')

    if response == 'team':

        team1 = players[:len(players)//2]

        print('Team 1 captain: ' + random.choice(team1))
        print('Team 1: ')
        for player in team1:
            print(player)

        team2 = players[len(players)//2:]

        print('\nTeam 2 captain: ' + random.choice(team2))
        print('Team 2: ')
        for player in team2:
            print(player)

    else:
        for i in range(0, 20, 2):
            print(players[i] + ' vs ' + players[i+1])

            start = random.randrange(i, i+2)

            print(players[start] + ' starts')
                
        response = input('Pick team again? Type y or n: ')
        if response == 'n':
            break
