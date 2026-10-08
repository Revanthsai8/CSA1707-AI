# Vacuum Cleaner Problem

room = {
    "A": "Dirty",
    "B": "Dirty"
}

position = "A"

while room["A"] == "Dirty" or room["B"] == "Dirty":

    print("Vacuum is at room", position)

    if room[position] == "Dirty":
        print("Cleaning room", position)
        room[position] = "Clean"

    elif position == "A":
        print("Moving to room B")
        position = "B"

    else:
        print("Moving to room A")
        position = "A"

print("Both rooms are clean.")
