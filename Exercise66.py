A = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}
D = []
K = input("Enter a letter grade (blank to stop): ")
while K != "":
    D.append(K)
    K = input("Enter a letter grade (blank to stop): ")
B = 0
H = 0
for K in D:
    if K in A:
        B += A[K]
        H += 1
if H > 0:
    E = B / H
else:
    E = 0.0
print("Grade Point Average (GPA): %.1f" % E)