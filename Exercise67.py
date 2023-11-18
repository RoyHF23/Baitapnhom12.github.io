A = {
    "0-2": 0.00,
    "3-12": 14.00,
    "65+": 18.00,
    "others": 23.00
}
B = []
C = input("Enter the age of a guest (blank to stop): ")
while C != "":
    B.append(int(C))
    C = input("Enter the age of a guest (blank to stop): ")
D = 0.00
for C in B:
    if C <= 2:
        D += A["0-2"]
    elif C >= 3 and C <= 12:
        D += A["3-12"]
    elif C >= 65:
        D += A["65+"]
    else:C
D += A["others"]
print("Admission cost for the group: $%.2f" % D)