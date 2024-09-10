# Pakudex

Pakudex is a Python-based application that simulates a Pokédex for fictional creatures called Pakuri. The project demonstrates key concepts of object-oriented programming (OOP) in Python, using classes to create, manage, and interact with Pakuri. Through a command-line interface (CLI), users can add new Pakuri, evolve them, view their stats, and sort their collection.

## Features

- **Add Pakuri**: Users can add Pakuri to their collection by specifying their species.
- **View Pakuri Stats**: Display the stats (Attack, Defense, Speed) for each Pakuri in the Pakudex.
- **Evolve Pakuri**: Upgrade the stats of a selected Pakuri through evolution.
- **Sort Pakuri**: Sort the Pakuri collection alphabetically by species name.
- **Interactive Menu**: A command-line interface that allows users to interact with the Pakudex via menu-driven options.

## File Structure

- `pakudex.py`: This file contains the `Pakudex` class, responsible for managing the list of Pakuri, adding new Pakuri, displaying their stats, sorting the collection, and handling evolution.
- `pakuri.py`: This file contains the `Pakuri` class, defining the individual Pakuri creatures, their attributes (species, attack, defense, speed), and their evolution logic.
- `pakuri_program.py`: This is the main driver program that interacts with the user through the command-line interface, providing options to add, view, sort, and evolve Pakuri.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dilsinnam/pakudex.git

2. Navigate to the project directory:
```bash
cd pakudex
```

3. Run the program:
```bash
python pakuri_program.py
```

How to Use

1. Upon starting the program, you will be presented with a menu to interact with the Pakudex.
2. Use the following options to manage your Pakuri collection:
    Add Pakuri: Enter a new species to add to the Pakudex.
    View Pakuri Stats: Display the stats of all Pakuri in the list.
    Evolve Pakuri: Choose a Pakuri to evolve and increase its stats.
    Sort Pakuri: Sort all Pakuri in alphabetical order.
    Quit: Exit the program.

Example
```bash
Pakuri Program
==============
1. Add Pakuri
2. Display Pakuri Stats
3. Evolve Pakuri
4. Sort Pakuri
5. Exit

What would you like to do? 
```

Project Structure and OOP Concepts
- Classes: The project uses Python classes to encapsulate the data and functionality for Pakuri (Pakuri class) and for managing the Pakudex (Pakudex class).
- Methods: Each class contains methods that allow interaction with Pakuri attributes and the Pakudex collection (e.g., add_pakuri(), evolve_pakuri(), sort_pakuri()).
- Data Encapsulation: Pakuri stats (attack, defense, speed) are managed as private attributes and modified via class methods.