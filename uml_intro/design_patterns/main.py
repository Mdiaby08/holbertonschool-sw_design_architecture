#!/usr/bin/env python3
def create(self, kind: str):
    if kind == "bus":
        return Bus()
    elif kind == "train":
        return Train()
    elif kind == "scooter":    # must edit here every time
        return Scooter()
