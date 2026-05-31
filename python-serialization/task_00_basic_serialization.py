#!/usr/bin/env python3
"""Modul used for serialization and de-serialization"""
import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, "r") as f:
        deserialized_data = json.load(f)
    return(deserialized_data)
