#!/usr/bin/env python3

import random
import time
import pickle
import pathlib

loadName = "notefile.dat"
path = pathlib.Path(loadName)

ROAD_STRAIGHT = "|    |"
ROAD_LESS = "/    /"
ROAD_MORE = "\\    \\"
SPACE = " "
DITCH = "[]"

areaLeft = 24
numSpaces = 8
sections = 0
biasLeft = 0
biasRight = 0
simsRun = 0

if path.exists() & path.is_file():
    with open(loadName, "rb") as f:
        simsRun, biasLeft, biasRight = pickle.load(f)
    print("Loading...\n")

lastRoad = "straight"

print("*" * 46)
print("THE ROAD BUILDER")
print("Testing Bias in Python's Random Integer Method")
print("*" * 46)
print("Number of simulations run: " + (str(simsRun)))
if biasLeft == biasRight:
    print("Current bias: NONE")
elif biasLeft > biasRight:
    print("Current bias: LEFT (0)")
    print("Bias strength: %" + (str(int(abs(simsRun / (biasRight - biasLeft))))) + "00")
else:
    print("Current bias: RIGHT (2)")
    print("Bias strength: %" + (str(int(simsRun / abs(biasRight - biasLeft)))) + "00")
print("*" * 46)
print()
input("Press ENTER to begin...")

while numSpaces > 0 and numSpaces < 24:
    rando = random.randint(0,2)
    sections += 1
    if rando == 0:
        if lastRoad == "more":
            print(DITCH + (SPACE * numSpaces) + ROAD_STRAIGHT + (SPACE * (areaLeft - numSpaces) + DITCH))
        numSpaces -= 1
        print(DITCH + (SPACE * numSpaces) + ROAD_LESS + (SPACE * (areaLeft - numSpaces) + DITCH))
        lastRoad = "less"
    elif rando == 1:
        print(DITCH + (SPACE * numSpaces) + ROAD_STRAIGHT + (SPACE * (areaLeft - numSpaces) + DITCH))
        lastRoad = "straight"
    elif rando == 2:
        if lastRoad == "less":
            print(DITCH + (SPACE * numSpaces) + ROAD_STRAIGHT + (SPACE * (areaLeft - numSpaces) + DITCH))
        numSpaces += 1
        print(DITCH + (SPACE * numSpaces) + ROAD_MORE + (SPACE * (areaLeft - numSpaces) + DITCH))
        lastRoad = "more"
    time.sleep(0.25)
simsRun += 1
print("ROAD CRASHED after " + (str(sections)) + " sections.")
if numSpaces < 1:
    biasLeft += 1
    print("Random interger bias towards left (0) recorded.")
else:
    biasRight += 1
    print("Random interger bias towards right (2) recorded.")

with open(loadName, "wb") as f:
    pickle.dump([simsRun, biasLeft, biasRight], f, protocol=pickle.HIGHEST_PROTOCOL)
print("\nSaving...")

input("Press ENTER to exit...")

