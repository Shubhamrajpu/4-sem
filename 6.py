totaldays =  int(input("total no of days\n"))
fine=0
if totaldays<=5:
    print("first five days charge:0.40")
    fine=totaldays*0.40
    print("fine of the book",fine)

elif totaldays<=10:
    print("five to tens days fine:0.65")
    totaldays=totaldays-5
    fine=totaldays*0.65
    temp = 0.40 * 5
    print("fine of the book",fine + temp)

elif totaldays<=16:
    print("ten to sixteen days:0.80")

    totaldays=totaldays-10
    fine=totaldays*0.80
    temp1= 0.40*5
    temp2=0.65*5
    print("fine of the book:",fine+temp1+temp2)

else:
    print("book returned in time")






