running = True
while running:
print("welcome to the number analyzer")
num = int(input("Please input a number between 1 and 100"))

if num >=1 and num <= 100:
    even = num % 2 == 0
    if even :
        if num >=2 and num <=24:
            print ("Even and less than 25")
        elif num >=26 and num <= 60:
            print ("Even and between 26 and 60 inclusive.")
        elif num >= 60:
            print("Even and greater than 68.")
    else:
        if num < 60:
            print("odd and less than 60")
        elif num >= 60:
            print("Odd and greater than 60")
else:
    print(str(num) + " is not between 1 and 100")
repeat = input ("would you like to play again? (Input "Yes' or "No'*)
            if repeat == "Yes":
                    continue
            else:
                running = False