# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2st number: "))
# num3 = float(input("Enter 3st number: "))

# average = num1 + num2 + num3 / 3
# # average =  sum(num1,num2,num3) /  3

# print("Average is: ",average)

#second method like dynamik

n = int(input("How many numbers? "))

numbers = []
for i in range(n):#yha per loop 0 se chl rha hai isko difine nhi krte ha tbh bhi 0 se chlta hai
    num = float(input(f'Enter number {i + 1}: '))
    numbers.append(num)

average = sum(numbers) / len(numbers)

print("The average is: ", average)