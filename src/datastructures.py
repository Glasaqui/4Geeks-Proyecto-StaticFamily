"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name, members):
        self.last_name =  last_name
        
        # example list of members
   
        self._members = members
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id']= self._generateId()
        member['last_name']= self.last_name
      #  self._members.append(member)

      #  return None
        self._members.append(member)
        
        return self
        

    def delete_member(self, id):
        # fill this method and update the return
       
        for person in range (len(self._members)):
            if self._members[person]['id'] == int(id):
                self._members.pop(person)
        return None    

    def get_member(self, id):
        # fill this method and update the return
         for person in self._members:
            if person['id'] == int(id):
                return person


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
