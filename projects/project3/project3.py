import requests

def getPokemonData(pokemon):
    """This function calls the PokeAPI and returns name, Pokedex number, types, and weaknesses of a user selected Pokemon (any generation)."""
    
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}") # Sends a GET request to PokeAPI and saves it
    
    if r.status_code == 404: # Page not found error
        print("Check your spelling and try again.")
        return None
    else:
        data = r.json() # Saves 'r' as a JSON variable
        name = data['name'] 
        pokedexNumber = data['id'] 
        types = [type_data['type']['name'] for type_data in data['types']] 
        weaknesses = []
        for type_data in data['types']:
            r = requests.get(type_data['type']['url'])
            type_info = r.json()
            for weak_to in type_info['damage_relations']['double_damage_from']:
                weaknesses.append(weak_to['name'])
        return {
            'name': name,
            'pokedex_number': pokedexNumber,
            'types': types,
            'weaknesses': weaknesses
        }

userPokemon = input("Enter the  Pokemon name: ")
pokemonData = getPokemonData(userPokemon)

print("\nPokemon: " + pokemonData['name'] , 
      "\nPokedex Number:", pokemonData['pokedex_number'] ,
      "\nTypes:", ", ".join(pokemonData['types']) , 
      "\nWeaknesses:", ", ".join(pokemonData['weaknesses']))