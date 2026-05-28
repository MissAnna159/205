print("carana9896")


def StudentID():
    print("carana9896")

def functionTwo():
    Num1 = int(input("Please enter a number: "))
    Num2 = int(input("Please enter a number: "))
    Answer = Num1 + Num2
    print(f'The sum of {Num1} and {Num2} is {Answer}.')
    return (Answer)

def functionThree(Answer):
    if Answer > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")

def main():
    StudentID()
    Answer = functionTwo()
    functionThree(Answer)
    ID = 9896
    print(f'functionThree returned the value of {ID}.')

main()

    
