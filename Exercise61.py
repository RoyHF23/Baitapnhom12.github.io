H = 0
B = 0
while True:
        A = float(input("Enter a number (0 to quit): "))
        if B == 0 and A == 0:
                print("Error: You must enter at least one number")
                break
        if A == 0:
             break
        H += A
        B += 1
if B > 0:
    K = H / B
    print("The average of the numbers you entered is:", K)
