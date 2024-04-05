from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.__capacity = capacity
        self.__pakuri_list = []

    def get_size(self):
        return len(self.__pakuri_list)

    def get_capacity(self):
        return self.__capacity

    def get_species_array(self):
        if not self.__pakuri_list:
            return None
        return [pakuri.get_species() for pakuri in self.__pakuri_list]

    def get_stats(self, species):
        for pakuri in self.__pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self.__pakuri_list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        if self.get_size() >= self.__capacity or any(
            p.get_species() == species for p in self.__pakuri_list
        ):
            return False
        self.__pakuri_list.append(Pakuri(species))
        return True

    def evolve_species(self, species):
        for pakuri in self.__pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
