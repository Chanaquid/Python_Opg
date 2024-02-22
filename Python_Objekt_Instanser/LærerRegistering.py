from app import create_teacher,update_teacher, show_all_teachers

def main():
    while True:
        print('------------TEC-App-------------')
        print("[1] Opret lærer\n[2] Opdater lærer\n[3] Vis list af alle lærer\n[4] Afslut")
        choice = input("--------------------------------\nVælg 1, 2, 3 eller 4: ")
        if choice == "1":
            create_teacher()
        elif choice == "2":
            update_teacher()
        elif choice == "3":
            show_all_teachers()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("!!!!!!!!!!Invalid!!!!!!!!!!")

if __name__ == "__main__":
    main()
