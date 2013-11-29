# -*- coding: utf-8 -*-
"""
Helper module that spits out the cards and quartets, if needed in the game.
"""
__author__ = "1224270: Frank Kramer, 3402993: Sascha Reynolds"

import sys


def colour() -> list:
    if sys.stdin.encoding.lower() == "cp850": ## Windows console
        return ['\x03', '\x04', '\x05', '\x06']
    elif sys.stdin.encoding.lower() in ("utf-8", "cp1252"): ## Unix || IDLE
        return ['\u2665', '\u2666', '\u2663', '\u2660']
    else:
        return ['H', 'D', 'C', 'S']


def number() -> list:
    return ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def quartet() -> list:
    quartet = []
    numbers = number()
    colours = colour()
    for i in range(8):
        quartet.append([])
        for j in colours:
            quartet[i].append(numbers[i] + j)
    return quartet
