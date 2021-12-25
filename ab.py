persons = []

def create_person():
    name = input('name: ')
    address = input('address: ')
    phone = input('phone: ')
    person = {'name': name,  'address': address, 'phone': phone}
    persons.append(person)

def list_person():
    for person in persons:
        print('%s,%s,%s' % (person['name'], person['address'], person['phone']))

def query_person():
    name = input('name: ')
    for person in persons:
        if person['name'] == name:
            print('%s,%s,%s' % (person['name'], person['address'], person['phone']))

def delete_person():
    name = input('name: ')
    for person in persons:
        if person['name'] == name:
            persons.remove(person)
            break                    

def get_choice():
    print('1. create person')
    print('2. list all persons')
    print('3. query person')
    print('4. delete person')
    print('5. quit')
    choice = input('Enter a number(1-5):')  
    return choice

def main():
    while True:
        choice = get_choice()

        if choice == '1':
            create_person()
        elif choice == '2':
            list_person()
        elif choice == '3':
            query_person()
        elif choice == '4':
            delete_person()
        elif choice == '5':
            break
        else:
            print('Invalid choice')  

main()       
