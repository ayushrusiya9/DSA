# check if a string contains only digits

def checkStringOnlyDigit(s):
    if s.isdigit():
        print('string is digit.')
    else:
        print('string is not digit. ')
    
checkStringOnlyDigit(input('Enter String: '))