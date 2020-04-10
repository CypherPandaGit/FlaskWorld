from basic import db, Pokemon

# CREATE #
my_pokemon = Pokemon('Mew', 10, 'psychic')
db.session.add(my_pokemon)
db.session.commit()

# READ #
all_pokemons = Pokemon.query.all() # list of Pokemon objects in the table
print(all_pokemons)

# SELECT BY ID #
pokemon_one = Pokemon.query.get(3)
print(pokemon_one.name)
print(pokemon_one.level)

# FILTERS #
# PRODUCE SOME SQL CODE #
pokemon_mew = Pokemon.query.filter_by(name='Mew')
print(pokemon_mew.all())
# Result: ["Pokemon Mew is level 10]

# UPDATE #
first_pokemon = Pokemon.query.get(1)
first_pokemon.level = 23
db.session.add(first_pokemon)
db.session.commit()
print(first_pokemon)
# Result: Pokemon Pikachu is level 23

# DELETE #
second_pokemon = Pokemon.query.get(2)
db.session.delete(second_pokemon)
db.session.commit()
# DELETES CHARIZARD

#
all_pokemons = Pokemon.query.all()
print(all_pokemons)
