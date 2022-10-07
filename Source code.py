print("PASSWORD GENERATOR USING PYTHON")
run = True
while run:
    import random

    check1 = True
    length = (input("Enter your password length: "))
    for i in length:
        if 48<=ord(i)<=57:
            check1 = True
        else:
            check1 = False
    if check1 == True:
        capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = 'abcdefghijklmnopqrstuvwxyz'
        number = '1234567890'
        character = '!@#$%^&*()_+=-{}[]|:;"<>,.?//*-~ '
        combined = capital + lower + number + character
        password = ''.join(random.sample(combined, int(length)))
        print(f"Your automated generated password is :{password}")
        check = input("Do you want to generate another ?(y/n): ")
        # check1 = check.lower()

        if check.lower()[0] == 'y':
            run = True
        else:
            run = False
    else:
        print("Wrong input. Try Again")
        run = True
print("CODED BY ISHMAM.")
