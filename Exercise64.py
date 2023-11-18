A = 0
B = input("Enter the price (blank to stop): ")

while B != "":
    price = float(B)
    A += price
    B = input("Enter the price (blank to stop): ")

C = A % 5
if C < 2.5:
    D = A - C
else:
    D = A + (5 - C)
print("Total cost: $%.2f" % A)
print("Amount due (cash payment): $%.2f" % D)