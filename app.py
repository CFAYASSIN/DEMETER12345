
company_name = input("Enter insurance company name: ")

premium = float(input("Enter total premium: "))
claims = float(input("Enter total claims: "))

result = premium - claims
claims_ratio = (claims / premium) * 100

print("Company:", company_name)
print("Premium:", premium)
print("Claims:", claims)
print("Profit/Loss amount:", result)
print("Claims ratio:", round(claims_ratio, 2), "%")

if result > 0:
    print("Status: Surplus before expenses")
elif result == 0:
    print("Status: Break-even before expenses")
else:
    print("Status: Deficit before expenses")
