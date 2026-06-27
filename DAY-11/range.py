#basic range operation
# range (start,stop+1,step)

'''
for i in range(1,11):
 print(i)

for i in range(2,51,2):
  print(i)
  

for i in range(5,101,5):
    print(i)

    
for i in range(20,0,-1):
    print(i)

    
for i in range(30,3,-3):
    print(i)


l = [7,2,45,6,54,3,2,4,5]
for i in range(len(l)):
 print(i,l[i])

print("SEPARATED")

t = (7,2,45,6,54,3,2,4,5)
for i in range(len(t)):
 print(i,t[i])

k = [7,2,45,6,54,3,2,4,5]
for i in enumerate(k):
 print(i)


for i in range(10):
    pass

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)
   

L = [56,76,32,3,34,2,3,5,97,45,13,23,45,23,98,76,32]

for i in L:
    if i % 2 == 0:
        print(i)
 

d = {'laptop':0,'mouse':5,'tab':0,'keyboard':10,'phone':12}

for i in d:
    if d[i]:
        print(i)


t = (9,2,13,4,5,6)

for i in range(len(t)):
    j = t[i]*i
    print(j)

'''

names = {'subbu','naresh','dinesh','sahith','rishi','praneeth'}

for i in names:
    print(i.upper())