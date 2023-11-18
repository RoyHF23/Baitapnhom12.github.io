#71
x=int(input("x="))
guess=x/2
while (guess!=abs(guess*guess-x<=10**-12)):
    guess=(guess+x/guess)/2
    print(guess)
    break