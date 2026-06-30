l = [1,2,3,4,5,6,7,8,9]
k = int(input("enter the element: "))

for i in range(len(l)):
    if l[i] == k:
        print(f'{k} is found at index - {i}')
        break
else:
    print(f'{k} is not found')

    