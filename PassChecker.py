print("--- Let's Check Your Password ---")

password = input("Enter Your Password Here: ")

result = {}

if len(password) >=8:
    result["length"] = True

else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit


uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

    result["upper-case"] = uppercase
print(result)


if all(result.values()):
    print("You put a Strong Password !...")

else:
    print("You put a weak Password !...")


