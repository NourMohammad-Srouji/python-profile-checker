# get the values from the user.

name = input('Enter your name: ')
age = int(input('Enter your age: '))
gpa = float(input('Enter your gpa; GPA (0-5, can be decimals): '))
field_of_interest = input('Enter your field of interest: ')
graduated = input('Graduated: ("yes" or "no")? ')

print()

# lower the graduated value
lower_case_graduated = graduated.lower()

# print the statements.

print('Your name is', name + '.')
print('Your are', age, 'years old.')
print('You have GPA', format(gpa, '.2f') + '.')
print('You are interested in', field_of_interest + '.')
print('Are you graduated? yes or no?', lower_case_graduated + '.')
print()

# Check the eligible conditions to execute their body.
if gpa > 0 and gpa < 5:
    if lower_case_graduated != 'yes' and lower_case_graduated  != 'no':
        print(graduated, 'is not a valid answer.')
    else:

        if (age < 25 ) and (gpa >= 3.5) and (lower_case_graduated == 'yes'):
            print(name, 'is eligible for a scholarship')
        elif (age < 30) and (gpa >= 2.5):
            print(name, 'is eligible for an internship')
        else:
            print(name, 'is recommended to apply again later.')
else:
    print(gpa, 'is not a valid GPA.')