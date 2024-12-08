class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception("Name must be a string")

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Invalid pet type")

        if owner is None or isinstance(owner, Owner):
            self.owner = owner
        else:
            raise Exception("Owner must be an instance of Owner class or None")

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception("Name must be a string")

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Pet must be an instance of Pet class")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
