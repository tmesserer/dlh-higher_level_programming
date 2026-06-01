#!/usr/bin/env python3
"""
Module for xml shenanigans
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serializes python dictionary to xml"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(
        filename,
        encoding="utf-8",
        xml_declaration=True
    )


def deserialize_from_xml(filename):
    """deserializes from xml back to Python"""
    tree = ET.parse(filename)
    root = tree.getroot()
    my_dict = {}

    for child in root:
        my_dict[child.tag] = child.text
    return my_dict
