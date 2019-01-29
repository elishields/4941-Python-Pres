###############
# fileRead.py #
###############

import json

def fileRead(path):

    f = open(path, "r")
    data = json.load(f)

    print()

    maxName = None
    maxIq = 0
    for key, value in data.items():
        print("Student" , key, "has IQ of", value, "...")

        if value > maxIq:
            maxName = key
            maxIq = value

    userIqRaw = input("\nWhat's your IQ?\n> ")
    userIq = int(userIqRaw)

    if userIq > maxIq:
        print("\nWoah! You're pretty smart! You beat Einstein!")
    else:
        print("\nYikes...")

    print()

fileRead("data.json")
