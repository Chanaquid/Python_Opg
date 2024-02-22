class Person:
    def __init__ (self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

class missing_person(Person):
    def __init__(self, id, firstname, lastname, last_seen='Unknown'):
        super().__init__(id, firstname, lastname)
        self.last_seen = last_seen
        
    def update_last_seen(self, new_last_seen):
        self.last_seen = new_last_seen
        
    def __str__(self):
        return f'ID: {self.id}] First Name: {self.firstname} \t| Last Name: {self.lastname}\t| Last seen: {self.last_seen}'

class gang_members(Person):
    def __init__(self, id, firstname, lastname, gang_name='Unknown'):
        super().__init__(id, firstname, lastname)
        self.gang_name = gang_name
        
    def update_gang(self, new_gang_name):
        self.gang_name = new_gang_name
        
    def __str__(self):
        return f'ID: {self.id}] First Name: {self.firstname} \t| Last Name: {self.lastname}\t| Gang: {self.gang_name}'