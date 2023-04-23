import requests

def getPokemonData(pokemon):
    """This function calls the PokeAPI and returns name, Pokedex number, types, and weaknesses of a user selected Pokemon (any generation)."""
    
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}") # Sends a GET request to PokeAPI and saves it as a variable
    
    if r.status_code == 404: # Page not found error
        print("Check your spelling and try again.")
        return None
    else:
        data = r.json() # Saves the JSON data in 'r' as a dictionary
        name = data['name'] # Extracts the name from 'data' as a string
        pokedexNumber = data['id'] # Extracts the Pokedex number from 'data' as an integer
        types = [type_data['type']['name'] for type_data in data['types']] # Extracts the type(s) and saves as a list
        weaknesses = [] # Creates a list for weakness(es)
        for type_data in data['types']: # Might be more than 1
            r = requests.get(type_data['type']['url']) # Sends another GET request regarding the type and saves it as a variable
            type_info = r.json()
            for weak_to in type_info['damage_relations']['double_damage_from']: # Might be more than 1
                weaknesses.append(weak_to['name']) # Adds the weakness to the variable
        return {
            'name': name,
            'pokedex_number': pokedexNumber,
            'types': types,
            'weaknesses': weaknesses
        }

while True: # This loop allows the user to compare as many Pokemon as they would like, in case they would like to compare multiple
    userPokemon = input("Enter the  Pokemon name: ")
    pokemonData = getPokemonData(userPokemon)

    print("\nPokemon: " + pokemonData['name'] , 
        "\nPokedex Number:", pokemonData['pokedex_number'] ,
        "\nTypes:", ", ".join(pokemonData['types']) , 
        "\nWeaknesses:", ", ".join(pokemonData['weaknesses']))
    
    answer = input("Would you like to compare to another Pokemon? (y/n): ")
    if answer.lower() != "y":
        break

