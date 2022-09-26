
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

def jls_extract_def():
    return "lucky_numbers"


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name =  "Jackson"

        # example list of members
    jls_extract_var = jls_extract_def()
    self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name":  self.last_name,
            "age": 33,
            jls_extract_var: [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
        }
        ]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id']= self._generateId()
        member['last_name']= self.last_name
        self._members.append(member)

        return None
        

    def delete_member(self, id):
        # fill this method and update the return
         #Para corregir el index out of range del método pop, incluimos el largo del arreglo de objetos con los miembros de la familia**
        for person in range (len(self._members)):
            if self._members[person]['id'] == int(id):
                self._members.pop(person)
        return None    

    def get_member(self, id):
        # fill this method and update the return
         for person in self._members:
            if person['id'] == int(id):
                return person

         return person 

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
