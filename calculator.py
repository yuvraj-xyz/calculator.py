#Simple Calculator Program.

#Show The the Operations for No. 1/2/3/4 respectively.
print("Select the Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#if user selects any No. then CONTINUE to below Code.
while True:

#Take Choice 
    choice = input("Enter Choice (1/2/3/4) : ")

#If choice is from 1/2/3/4 then ask for Digits input.
    if choice in ("1", "2", "3", "4"):

        a = float(input("ENTER THE FIRST DIGIT : "))
        b = float(input("ENTER THE SECOND DIGIT : "))

#Add b/w 2 Digits
        if choice == '1':
            print("The Addition of two Digits is : " , a+b)
#Subtract b/w 2 Digits
        elif choice == '2':
            print("The Subtract of two Digits is : " , a-b)
#Multiplication b/w 2 Digits
        elif choice == '3':
            print("The Multiplication of two Digits is : " , a*b)
#Division b/w 2 Digits
        elif choice == '4':
            print("The DIvision of two digits is : " , a/b)

        break
#If User selects other then 1/2/3/4, Then Show this
    else:
        print("INVALID Input")
