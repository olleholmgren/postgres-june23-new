

class FriaMagnataOrdern:
    def __init__(self, name, title, age, color):
        self.name = name
        self.title = title
        self.age = age
        self.color = color

    def DescribePerson(self):
        return f"Namnet var {self.name}, med titeln {self.title}, {self.age} år gammal, färgen äro {self.color} och förblivo {self.color}."

member_1 = FriaMagnataOrdern('Sunnek', 'bas', 55, 'lila')
member_2 = FriaMagnataOrdern('Hasse', 'hundvakt', 28, 'brun')

print(member_1.DescribePerson())
print(member_2.DescribePerson())