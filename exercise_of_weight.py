weight = int(input("Enter your weight: "))
type = input("Enter (P) Pound or (k) KG ")

if type.upper() == "P":
    converted = weight / 0.45
    print(f"your weight is {converted} in pound")

elif type.upper() == "K":
   converted = weight * 0.45
   print(f"your weight is {converted} in KG")

else:
    print ("enter the correct character")