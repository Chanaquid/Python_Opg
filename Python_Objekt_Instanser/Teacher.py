from Person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject_id):
        self.subjects = [subject for subject in self.subjects if subject.id != subject_id]