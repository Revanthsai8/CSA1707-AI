from itertools import permutations

words = ["SEND", "MORE"]
result = "MONEY"

letters = set("SENDMORY")
letters = list(letters)

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    # First letters cannot be zero
    if d["S"] == 0 or d["M"] == 0:
        continue

    SEND = d["S"]*1000 + d["E"]*100 + d["N"]*10 + d["D"]
    MORE = d["M"]*1000 + d["O"]*100 + d["R"]*10 + d["E"]
    MONEY = d["M"]*10000 + d["O"]*1000 + d["N"]*100 + d["E"]*10 + d["Y"]

    if SEND + MORE == MONEY:
        print("Solution found:")
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        print("\nLetter values:")
        
        for letter in sorted(d):
            print(letter, "=", d[letter])
        
        break
