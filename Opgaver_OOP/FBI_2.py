#This is the part 1 of the FBI 
import csv 
from classes import missing_person, gang_members
from update import update_missing_person_last_seen, update_gang_member_name

def show_missing_person():
    missing = []
    id = 1
    with open('FBI.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[0]
            if "Missing Persons" in category:
                name = row[1].split(' ')
                firstname = name[0]
                lastname = ' '.join(name[1:]).split(' - ')[0]
                person = missing_person(id, firstname, lastname)
                missing.append(person) 
                id += 1
    return missing  
        

def show_gang_members():
    gang = []
    id = 1
    with open('FBI.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[0]
            if "Criminal Enterprise Investigations" in category:
                name = row[1].split(' ')
                firstname = name[0]
                lastname = name[1]
                member = gang_members(id, firstname, lastname)
                gang.append(member)
                id += 1
    return gang


def main():
    missing = show_missing_person()
    gang = show_gang_members()
    while True:
        print('\n-------FBI Database------- \nChoose an option:')
        print('_________________________')
        print('1. Show missing persons')
        print('2. Show gang members')
        print('3. Exit')
        print('_________________________')
        choice = input('\nEnter your choice: ')
        
        if choice == '1':
            print('_________________________')
            for person in missing:
                print(person)
            input('\nPress enter to continue.....')
            update_missing_person_last_seen(missing)  
        elif choice == '2':
            print('_________________________')
            for memeber in gang:
                print(memeber)
            input('\nPress enter to continue.....')
            update_gang_member_name(gang)  
        elif choice == '3':
            break
        else:
            print('\n!!!!Invalid choice!!!!!\n')
            continue
    print('\nGoodbye!\n')
    
if __name__ == '__main__':
    main()