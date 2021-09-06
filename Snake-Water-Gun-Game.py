print("THE ULTIMATE SNAKE,WATER & GUN GAME")
print("s:snake\nw:water\ng:gun\n")
i = 1
PC=0
Mihir=0
while i <= 10:
    import random
    list=["s","w","g"]
    random=random.choice(list)
    input_=input("Press s,w or g: ")

    if input_==random:
        print(f"Mihir select {input_} & PC select {random}")
        print("Tie 0 point to each\n")

    elif input_=="s" and random=="w":
        Mihir+=1
        print(f"Mihir select {input_} & PC select {random}")
        print("Mihir Win 1 point\n")
    elif input_=="w" and random=="s":
        PC+=1
        print(f"Mihir select {input_} & PC select {random}")
        print("Computer Win 1 point\n")
    elif input_=="w" and random=="g":
        Mihir+= 1
        print(f"Mihir select {input_} & PC select {random}")
        print("Mihir Win 1 point\n")
    elif input_=="g" and random=="w":
        PC+= 1
        print(f"Mihir select {input_} & PC select {random}")
        print("Computer Win 1 point\n")
    elif input_=="g" and random=="s":
        Mihir+= 1
        print(f"Mihir select {input_} & PC select {random}")
        print("Mihir Win 1 point\n")
    elif input_=="s" and random == "g":
        PC+= 1
        print(f"Mihir select {input_} & PC select {random}")
        print("PC Win 1 point\n")
    else:
        print("Invalid input, enter s,w or g\n")
    i+=1
print("Game Over\n")
print("Final Score of Mihir",str(Mihir))
print("Final Score of PC",str(PC))
if Mihir>PC:
    print("Mihir Won and PC loose")
elif Mihir==PC:
    print("Tie")
else:
    print("PC Won and Mihir loose")