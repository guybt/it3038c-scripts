import json
import requests

def fetch_pokemon_data(pokemon):
    """This function calls the PokeAPI and returns name, Pokedex number, types, and weaknesses of 2 user declared Pokemon (any generation)."""
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}") # Requests data for user-input Pokemon
    if r.status_code == 404: # Page not found error (likely misspelled)
        print("Pokemon not found. Check your spelling and try again.")
        return None
    else:
        data = r.json()
        name = data['name']
        pokedex_number = data['id'] # Creates a string for the Pokedex number
        types = [type_data['type']['name'] for type_data in data['types']] # Creates a list for the Pokemon's type(s)
        weaknesses = []
        for type_data in data['types']: # Loops through type(s) (Each Pokemon may have multiple)
            r = requests.get(type_data['type']['url']) # Requests data for each type
            type_info = r.json()
            for weak_to in type_info['damage_relations']['double_damage_from']: # Loops through type(s) that type will take double damage from (Each type may have multiple)
                weaknesses.append(weak_to['name']) # Adds type weakness(es) to weaknesses list
        return {
            'name': name,
            'pokedex_number': pokedex_number,
            'types': types,
            'weaknesses': weaknesses
        }

# Prompt user for Pokemon1 name then return info to user
pokemon1 = input("Enter the first Pokemon name: ")
pokemon1_data = fetch_pokemon_data(pokemon1)
print("\nComparing Pokemon:")
print("\nPokemon 1: " + pokemon1_data['name'] , 
      "\nPokedex Number:", pokemon1_data['pokedex_number'] ,
      "\nTypes:", ", ".join(pokemon1_data['types']) , 
      "\nWeaknesses:", ", ".join(pokemon1_data['weaknesses']))

compare = input('\nWould you like to compare this Pokemon to another Pokemon? (y/n)')
if compare.lower() == 'y':
    # Prompt user for Pokemon2 name then return info to user
    pokemon2 = input("\nEnter the second Pokemon name: ")
    pokemon2_data = fetch_pokemon_data(pokemon2)
    print("\nComparing Pokemon:")
    print("\nPokemon 2: " + pokemon2_data['name'] , 
        "\nPokedex Number:", pokemon2_data['pokedex_number'] ,
        "\nTypes:", ", ".join(pokemon2_data['types']) , 
        "\nWeaknesses:", ", ".join(pokemon2_data['weaknesses']))
elif compare.lower() == 'n':
    print("Okay!")
else:
    print("Type y or n")

