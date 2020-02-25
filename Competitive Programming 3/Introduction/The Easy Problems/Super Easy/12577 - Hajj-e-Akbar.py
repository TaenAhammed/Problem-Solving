counter = 1

while True:
    warship_type = input()
    if warship_type == '*':
        break

    if warship_type == 'Hajj':
        print(f'''Case {counter}: Hajj-e-Akbar''')
        counter += 1

    elif warship_type == 'Umrah':
        print(f'''Case {counter}: Hajj-e-Asghar''')
        counter += 1
