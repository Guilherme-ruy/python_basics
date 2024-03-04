x = 1
y = 1

print (" X ")

while x <= 10:
    print (x)
    x = x + 1

print ("--------------")
print (" Y ")

while y <= 6:
    print (y)
    y += 1



option = -1
while option != 0:
    option = int(input("Choose an option: [1] Repeat [2] Repeat twice [0] Exit \n"))	

    if option == 1:
        print ("Repeat")
    elif option == 2:
        print ("Repeat twice")
    elif option == 0:
        print ("Exit")
    else:
        print ("Invalid option")
else:
    print("End")