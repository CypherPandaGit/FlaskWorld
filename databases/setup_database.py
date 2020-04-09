from basic import db, Pokemon

# CREATES ALL THE TABLES Model ->> DB Table
db.create_all()

pikachu = Pokemon('Pikachu', 3)
charizard = Pokemon('Charizard', 4)

print(pikachu.id)
print(charizard.id)

db.session.add_all([pikachu, charizard])

# db.session.add(pikachu)
# db.session.add(charizard)

db.session.commit()

print(pikachu.id)
print(charizard.id)
