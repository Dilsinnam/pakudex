from pakudex import Pakudex


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        capacity = input("Enter max capacity of the Pakudex: ")
        if not capacity.isdigit():
            print("Please enter a valid size.")
            continue
        else:
            capacity = int(capacity)
            break
    dex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    while True:
        print(
            "\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit"
        )
        choice = input("What would you like to do? ")

        if not choice.isdigit():
            print("Unrecognized menu selection!")
            continue

        if choice == "1":
            species = dex.get_species_array()
            if species is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri in Pakudex:")  # Add this line
                for i, s in enumerate(species, 1):
                    print(f"{i}. {s}")
        elif choice == "2":
            species = input("Enter the name of the species to display: ")
            stats = dex.get_stats(species)
            if stats is None:
                print("Error: No such Pakuri!")
            else:
                print()
                print(
                    f"Species: {species}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}"
                )
        elif choice == "3":
            species_array = dex.get_species_array()
            if (
                species_array is not None and len(species_array) >= capacity
            ):  # Check if Pakudex is full
                print("Error: Pakudex is full!")
            else:
                species = input("Enter the name of the species to add: ")
                if dex.add_pakuri(species):
                    print(f"Pakuri species {species} successfully added!")

        elif choice == "4":
            species = input("Enter the species of the Pakuri to evolve: ")
            if dex.evolve_species(species):
                print(f"{species} has evolved!")
            else:
                print("Error: No such Pakuri!")
        elif choice == "5":
            dex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()
