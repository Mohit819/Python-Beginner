address = input("where are you shipping to?")
days = int(input("when do you need it shipped?"))
base_charge = (0)
if days == 0:
    base_charge = 15
elif days < 4:
    base_charge = 10
elif days < 7:
    base_charge = 4.5
else:
    base_charge = 2
item_weight = float(input("how heavy is your item?"))
charge_per_pound = (0)
if item_weight < 0.6:
    charge_per_pound = 0.1
elif item_weight < 1.1:
    charge_per_pound = 0.15
elif item_weight < 4:
    charge_per_pound = 0.25
else:
    charge_per_pound = 0.40
total_weight_charge = (item_weight * charge_per_pound)
gift_wrap_charge = (0)
input("do you want gift wrap")
if "yes":
    gift_wrap_charge = 2.5
total = (base_charge + total_weight_charge + gift_wrap_charge)
print (base_charge)
print(total_weight_charge)
print(gift_wrap_charge)
print(total)
