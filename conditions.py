print('Tell me the last name and I tell you the remaining information.')


def Jennifer(full_name, nationality, age, marital_status):
    print("")
    print('The name of the person you searched for is:', full_name)
    print(full_name, 'is', nationality)
    print('He is', age, 'years old')
    print('His marital status was complicated before but now he is', marital_status)


while True:

    last_name = str(
        input('What is the last name of the person you want to know about?: '))

    if last_name == 'Jodick':
        print(Jennifer('Jodick Ndayisenga', 'Burundian', 25, 'Single'))

    elif last_name == 'Kimorata':

        print(Jennifer('Dennis Kimorata', 'Kenyan',
              22, 'Searching for new connections'))

    elif last_name == 'Abdi':

        print(Jennifer('Anisa Abdi Mohammed', 'Somali', 19, 'Complicated'))

    elif last_name == 'Kivaa':
        print('Benjamin Kivaa', 'Kenyan', 21, 'Trying his luck')

    else:
        print('I am sorry, I do not know the name you have entered')
