from time import sleep
def timeGame():
    points=0
    attempt=1
    scoreboard={}
    print("Press 'enter' to start and 'ctrl+c' to stop the second hand")
    name=input('Enter the name of the player : ')
    while True:
        try:
            for digit in range(1,13):
                print(digit)
                sleep(0.2)
        except KeyboardInterrupt:
            print(f'Second hand stopped at {digit}')
            print('Calculating points...')
            sleep(2)
            if digit in [1,5,9,11]:
                points+=10
            elif digit in [4,7,8,10]:
                points+=20
            elif digit in [3,2,6,12]:
                points+=30
            attempt+=1
            if attempt==4:
                print(f'{name} has earned {points} points')
                scoreboard[name]=points
                nxt=input('Is there any other player : y/n').lower()
                if nxt=='y':
                    name=input('Enter the name of the player : ')
                    points=0
                    attempt=1
                else:
                    print('Final Scores-> ',scoreboard)
                    return
print(timeGame())