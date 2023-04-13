# Braiden Guy IT3038c Scripts
## Project 3
For Project 3, I wrote a python script that prompts the user for 2 Pokemon to compare (Name, Pokedex Number, Types, and Weaknesses). 

### Inspiration
As a lifelong casual Pokemon player, I thought that it would be neat if I created a program that would help me during a playthrough of any Pokemon game. Although I have played almost every Pokemon game, I sometimes forget a Pokedex number (useful when trying to complete the Pokedex) and types/weaknesses (useful for determining if a move will be super effective, not very effective, etc against an opponent during battle). 
I created this script to aid with determining these things on the fly (without having to use the internet)


### How it Works
This script uses the following Python Modules:
JSON (Comes with Python)
Requests (pip install requests)

This script calls the pokeapi, which can be found at https://pokeapi.co/, to retrieve info about 2 user-selected pokemon. The name, pokedex number, types, and weaknesses of 2 pokemon are retrieved and output to the user.