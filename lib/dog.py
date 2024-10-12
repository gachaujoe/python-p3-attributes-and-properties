#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# class Dog:
#     pass

# lib/dog.py

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Unknown", breed="Mastiff"):
        self.name = name
        self.breed = breed

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    # Property for name
    name = property(get_name, set_name)

    # Getter for breed
    def get_breed(self):
        return self._breed

    # Setter for breed
    def set_breed(self, breed):
        if breed in self.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    # Property for breed
    breed = property(get_breed, set_breed)

