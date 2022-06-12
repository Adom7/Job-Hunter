from ast import If


print('Hello World !')

User = input('Choose Option 1 or 2 ')


def sfy(option):
    if option == "1":
        return print("You Chose Option 1")

    elif option == "2":
        return print('Oprion 2')

    else:
        print('Enter a correct Option')


sfy(User)
