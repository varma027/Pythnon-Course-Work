pin = 1234

for i in range(5):
    epin = int(input("enter the pin : "))
    if epin == pin:
        print("Login")
        break
    else:
        print("don't login")
else:
    print("try again after some time")