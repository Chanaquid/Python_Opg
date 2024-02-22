from Teacher import Teacher
from Subject import Subject

subjects = [
    Subject(1, "IOT Embedded"),
    Subject(2, "Python"),
    Subject(3, "BigData 1"),
    Subject(4, "Softwaresikkerhed og test"),
    Subject(5, "Serversideprogrammering")
    ]

teachers = {}

def create_teacher():
    first_name = input("Fornavn: ")
    last_name = input("Efternavn: ")
    print("--------------------------------\nAngiv fag:\n")
    for subject in subjects:
        print(f"[{subject.id}] {subject.name}")
    subject_id = int(input("\nVælg et fag fra listen: "))
    selected_subject = next((subject for subject in subjects if subject.id == subject_id), None)
    if selected_subject:
        teacher = Teacher(first_name, last_name)
        teacher.add_subject(selected_subject)
        teacher_id = len(teachers) + 1
        teachers[teacher_id] = teacher
        print(f"{first_name.capitalize()} {last_name.capitalize()} er nu oprettet som lærer med følgende fag: --{selected_subject.name}--")
        input('')
    else:
        print("!!!!!!!!!!Invalid!!!!!!!!!!")

def update_teacher():
    if not teachers:
        print("Ingen lærer")
        return

    print("\nlist af alle lærer:")
    for id, teacher in teachers.items():
        print(f"[{id}] {teacher.first_name.capitalize()} {teacher.last_name.capitalize()}")
    teacher_id = int(input("Vælg en lærer fra listen: "))
    teacher = teachers.get(teacher_id, None)

    if teacher is None:
        print("Invalid teacher ID.")
        return

    print(f"\n[1] Tilføj flere fag for {teacher.first_name.capitalize()} {teacher.last_name.capitalize()}\n[2] Slet et fag.")
    option = input("Vælg 1 eller 2: ")

    if option == "1":
        print("\nAngiv fag:")
        for subject in subjects:
            print(f"[{subject.id}] {subject.name}")
        subject_id = int(input("Vælg et fag fra listen: "))
        selected_subject = next((subject for subject in subjects if subject.id == subject_id), None)
        if selected_subject:
            teacher.add_subject(selected_subject)
            print(f"{teacher.first_name.capitalize()} {teacher.last_name.capitalize()} er tilmeldt følgende fage: \n-{selected_subject.name}")
        else:
            print("!!!!!!!!!!Invalid!!!!!!!!!!")
    elif option == "2":
        if not teacher.subjects:
            print("Læren har ingen fag.")
            return
        print("\nAngiv fag for at slette:")
        for subject in teacher.subjects:
            print(f"[{subject.id}] {subject.name}")
        subject_id = int(input("\nVælg fag fra listen: "))
        subject_to_remove = next((subject for subject in teacher.subjects if subject.id == subject_id), None)
        if subject_to_remove:
            teacher.remove_subject(subject_id)
            print(f"Fag: {subject_to_remove.name} er blevet fjernet fra {teacher.first_name.capitalize()} {teacher.last_name.capitalize()}.")
        else:
            print("!!!!!!!!!!Invalid!!!!!!!!!!")
    else:
        print("Invalid option.")


def show_all_teachers():
    print("\nList af alle lærer:")
    if not teachers:
        print("\nNo teachers available.")
        return
    for id, teacher in teachers.items():
        subjects_str = ", ".join([subject.name for subject in teacher.subjects])
        print(f"\n{teacher.first_name.capitalize()} {teacher.last_name.capitalize()} \n  Fag: {subjects_str}")
        print('--------------------------------')
    input("")