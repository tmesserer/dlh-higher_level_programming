#!/usr/bin/env python3
"""Modul used for serialization and de-serialization"""
import csv
import json


def convert_csv_to_json(csv_file):
    """converts csv to json"""
    try:
        with open(csv_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True
    except Exception as e:
        print(e)
        return False
