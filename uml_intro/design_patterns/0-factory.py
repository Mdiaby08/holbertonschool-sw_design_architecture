#!/usr/bin/env python3

factory.register_kind("scooter", Scooter)

print(factory.create("scooter").mode())
