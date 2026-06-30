'''
i = 1
while i<11:
    print(i)
    i+=1

i = 2 
while i < 21:
    print(i)
    i+=2


#String
l = 'python programming'
i = 0
while i < len(l):
    print(l[i])
    i+=1


#Tuple
l = (1,2,4,5,6,7,3,9)
i = 0
while i < len(l):
    print(l[i])
    i+=1



l = [1,2,4,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,3,9,99]

while 0 in l:
    l.remove(0)
print(l)

'''

moves = 10

while moves > 1:
    status = input("[w]in or [c]ontinue: ").upper()
    if status == 'W':
        print("you win the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("Game over")
