import os

os.system("clear")

my_file = open("fizzbuzz.txt", "w+")

number = int(input("What is the number you wish?"))

for num in range(1, number):
    if num % 3 == 0:
        my_file.write(str(num) + "\n")
    else:
        print("FIZZ", num)



my_file = open("fizzbuzz.txt", "w+")

number = int(input("What is the number you wish?"))

for num in range(1, number):
    if num % 5 == 0:
        my_file.write(str(num) + "\n")
    else:
        print("BUZZ", num)




my_file = open("fizzbuzz.txt", "w+")

number = int(input("What is the number you wish?"))

for num in range(1, number):
    if num % 5 == 0 and num % 3 ==0:
        my_file.write(str(num) + "\n")
    else:
        print("FIZZBUZZ", num)


