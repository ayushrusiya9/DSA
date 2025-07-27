name = input('Enter your name: ')
age = int(input("Enter your age: "))

def vote_eligibility(your_name, your_age):

    your_name = your_name.title()

    if your_age >= 18:
        print(f'{your_name} you are eligible for vote')
    else:
        print(f'{your_name} you are not eligible for vote!')
    
    return

vote_eligibility(name,age)