# get the values from the user.

name = input('Enter your name: ')
age = int(input('Enter your age: '))
gpa = float(input('Enter your gpa; GPA (0-5, can be decimals): '))
field_of_Interest = input('Enter your field of interest: ')
graduated = input('Graduated: ("yes" or "no")? ')

print()

# lower the graduated value
lower_case_Graduated = Graduated.lower()

# print the statements.

print('Your name is', Name + '.')
print('Your are', Age, 'years old.')
print('You have GPA', format(GPA, '.2f') + '.')
print('You are interested in', Field_of_Interest + '.')
print('Are you graduated? yes or no?', lower_case_Graduated + '.')
print()

# Check the eligible conditions to execute their body.

if (Age < 25 ) and (GPA >= 3.5) and (lower_case_Graduated == 'yes'):
    print(Name, 'is eligible for a scholarship')
elif (Age < 30) and (GPA >= 2.5):
    print(Name, 'is eligible for an internship')
else:
    print(Name, 'is recommended to apply again later.')