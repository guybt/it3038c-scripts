# Braiden Guy IT3038c Scripts
## Project 3
For Project 3, I wrote a python script that prompts the user for the name of a Pokemon to view info about it (Name, Pokedex Number, Types, and Weaknesses). 

### Inspiration
As a lifelong casual Pokemon player, I thought that it would be neat if I created a program that would help me during a playthrough of any Pokemon game. Although I have played almost every Pokemon game, I sometimes forget a Pokedex number (useful when trying to complete the Pokedex) and types/weaknesses (useful for determining if a move will be super effective, etc against an opponent during battle). I created this script to aid with determining these things on the fly (without having to use the internet)
This script calls the pokeapi, which can be found at https://pokeapi.co/, to retrieve info about user-selected pokemon. The name, pokedex number, types, and weaknesses are retrieved and output to the user. The user is also given the opportunity to compare this pokemon to another.

### What you need
Python

This script uses the following Python Modules:
- JSON (built-in with Python)
- Requests
``` 
pip install requests
```

### How to use it
- Use git to pull the files from my github down to your local machine
- Make sure you have python installed
- Install the requests module (command listed above)
- Run the project3.py file
- Enter the name of a Pokemon (Pikachu, Charmander, Eevee, etc) 
- Enter y or n if you would/would not like to compare that Pokemon to another
- If you said y, then enter the name of another Pokemon (Snorlax, Sudowoodo, Squirtle, etc) 
