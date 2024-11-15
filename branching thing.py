userAge = int(input("How old are you"))
if userAge < 13:
    print("your ticket will be $5")
elif userAge < 20:
    print("your ticket will be $10")
elif userAge < 65:
    print("your ticket will be $15")
elif userAge > 64:
    print("your ticket will be $7")
