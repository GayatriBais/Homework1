from main import hw3,Student

hw3.create_all()

gayatri = Student('Gayatri','Bais', 99)
john = Student('John','Doe', 80)
sat = Student('Sat','chandel', 96)

# #print('initially they will print none')
# print(gayatri.id)
# print(sat.id)

hw3.session.add_all([gayatri, john, sat])

hw3.session.commit()

print(gayatri.id)
print(john.id)
print(sat.id)
