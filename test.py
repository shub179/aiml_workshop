def shopping(amount):
    if(amount<=10000):
        amount=amount-amount*0.1
    elif(amount>10000 & amount<=20000):
        amount=amount-amount*0.2
    else:
        amount=amount-amount*0.25

    print("net amoiunt",amount)
amount=int(input("Enter the purchase amount:"))
shopping(amount)