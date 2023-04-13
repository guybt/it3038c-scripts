import json
import requests

def fetch_pokemon_data(pokemon):
    """This function calls the PokeAPI and returns name, Pokedex number, types, and weaknesses of 2 user declared Pokemon (all generations)."""
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")
    if r.status_code == 404: # This error indicates that the name may have been misspelled
        print("Pokemon not found. Check your spelling and try again.")
        return None
    else:
        data = r.json()
        name = data['name']
        pokedex_number = data['id']
        types = [type_data['type']['name'] for type_data in data['types']]
        weaknesses = []
        for type_data in data['types']:
            r = requests.get(type_data['type']['url'])
            type_info = r.json()
            for weak_to in type_info['damage_relations']['double_damage_from']:
                weaknesses.append(weak_to['name'])
        return {
            'name': name,
            'pokedex_number': pokedex_number,
            'types': types,
            'weaknesses': weaknesses
        }

# Prompt user for Pokemon1 name then fetch/return info to user
pokemon1 = input("Enter the first Pokemon name: ")
pokemon1_data = fetch_pokemon_data(pokemon1)
print("\nComparing Pokemon:")
print("\nPokemon 1: " + pokemon1_data['name'])
print("Pokedex Number:", pokemon1_data['pokedex_number'])
print("Types:", ", ".join(pokemon1_data['types']))
print("Weaknesses:", ", ".join(pokemon1_data['weaknesses']))

compare = input('\nWould you like to compare this Pokemon to another Pokemon?')

if compare.lower() == 'yes':
    # Prompt user for Pokemon2 name then fetch/return info to user
    pokemon2 = input("\nEnter the second Pokemon name: ")
    pokemon2_data = fetch_pokemon_data(pokemon2)
    print("\nPokemon 2: " + pokemon2_data['name'])
    print("Pokedex Number:", pokemon2_data['pokedex_number'])
    print("Types:", ", ".join(pokemon2_data['types']))
    print("Weaknesses:", ", ".join(pokemon2_data['weaknesses']))
elif compair.lower() == 'no':
    print("Okay!")
else:
    print("Type yes or no")