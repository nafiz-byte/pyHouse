print("---Presenting Python Weight Converter---")

weight = float(input("Enter Your Weight:"))
unit = input("Kilograms oR Pounds (K / L): ")




if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your Weight is : {round(weight, 1)} {unit}")



elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your Weight is : {round(weight, 1)} {unit}")



else:
    print(f"{unit} is Invalid Credential ! ")
    print(input("Enter Valid Input Please:"))



