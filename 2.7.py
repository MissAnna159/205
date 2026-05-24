name = str (input("what is your name? "))
student_Id = str (input("what is your studentID? "))

secret_number = 5
tries = 0

guessNum = int (input("Please guess a number between 1 and 10? "))
tries += 1

while guessNum != secret_number:
    if guessNum < secret_number:
        print("You guessed too low")
    else:
        print("You guessed too high")

    guessNum = int (input("Please guess a bumber between 1 and 10? "))
    tries += 1


print(f"Congratulations, {name}! You guessed the number in {tries} tries!\n")
#while loop output
print("Output from the 'while' loop: ")
num = 5
increment = 1

while increment <= 5:
    print(f"{num} incremented by {increment} is {num + increment}")
    increment += 1

print()

#For loop output
print("Output from the 'for' loop: ")
num = 5

for increment in range (1,6):
    print(f"{num} incremented by {increment} is {num + increment}")
    
