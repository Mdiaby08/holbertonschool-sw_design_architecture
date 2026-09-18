#!/usr/bin/env python3

def main():
    factory = VehicleFactory()

    # LIGNE À AJOUTER
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    # LIGNE À AJOUTER
    print(factory.create("scooter").mode())
