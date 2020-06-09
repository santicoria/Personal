from member import Member
from repository import Repository


class MemberService(Member):
    def create_member(self, name, surname, age, phone):
        name = input('Ingrese nombre: ')
        surname = input('Ingrese apellido: ')
        age = input('Ingrese age: ')
        phone = input('Ingrese phone: ')
        return Member(name, surname, age, phone)

    def add_member(self, member=None):
        if member is None:
            member = self.create_member()
        key = len(Repository.membersList)
        Repository.membersList[key] = member.__dict__

    def update_member(self, key=None, member=None):
        if key is None:
            key = int(input('Ingrese una llave: '))
        if member is None:
            member = self.create_member
        Repository.membersList[key] = member.__dict__

    def delete_member(self, key=None):
        if key is None:
            key = int(input('Ingrese una llave: '))
        del Repository.membersList[key]

    def update_member_value_error(self, legajo, name, surname, age, phone):
        pass
