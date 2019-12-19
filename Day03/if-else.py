import getpass

username = input("Please enter the username: ")
password = getpass.getpass("Please enter the password: ")

if username == 'admin' and password == '123456':
    print("You Passed!")
else:
    print("Authentication Failed!")

print("*******************")

# scale exchange
value = float(input('Please enter the length: '))
unit = input('Please enter the unit: ')

if unit == 'in':
    print("{0} inches = {1} centimeters".format(value, value * 2.54))
elif unit == 'cm':
    print("{0} inches = {1} centimeters".format(value, value / 2.54))
else:
    print('Please enter valid unit')


print("********************")

score = float(input('Please enter the score: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('Your score reflects:', grade)