def update_missing_person_last_seen(missing):
    print("\nUpdate Last Seen for Missing Person:")
    id_to_update = input("Enter the ID of the person to update (or press ENTER to skip): ")
    if id_to_update.lower() == '':
        print("Skipped.")
        return
    for person in missing:
        if str(person.id) == id_to_update:
            new_last_seen = input("Enter new Last Seen : ")
            person.update_last_seen(new_last_seen)
            print("Last seen updated successfully.")
            return
    print("Person with ID not found.")

def update_gang_member_name(gang):
    print("\nUpdate Gang Name for Gang Member:")
    id_to_update = input("Enter the ID of the member to update (or press ENTER to skip): ")
    if id_to_update.lower() == '':
        print("Skipped.")
        return
    for member in gang:
        if str(member.id) == id_to_update:
            new_gang_name = input("Enter new Gang Name: ")
            member.update_gang(new_gang_name)
            print("Gang name updated successfully.")
            return
    print("Member with ID not found.")
