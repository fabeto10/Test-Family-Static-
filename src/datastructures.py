
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
        self.last_name = last_name
        for member  in members:
            self.add_member(member)

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if 'id' not in member or member['id'] < 1:
            member['id'] = self._generateId()
        if not hasattr(self, "_members"):
            self._members =[]
        self._members.append(member)

    def get_member(self, member):
        value = False
        for aux in self._members: 
            if aux['id']==member:
                value = aux
                break
        return value

    def delete_member(self, member):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i-1]['id'] == member:
                del self._members[i-1]
        if(self.get_member(id)):
            return {"done": False}
        return {"done": True}
        

    # this method is done, it returns a list with all the family 
    def get_all_members(self):
        return self._members
