#Pethon-3 "for-else" exaple

print("\n*** Find if gas mixture is danger using circle  ***\n")

def print_danger_mixture (mixture):
    bOxigen = False
    bHidrogen = False
    words = mixture.split(" ")
    for gas in words:
        print(">>>>> " +gas)
        bOxigen = (gas == "oxygen") or bOxigen
        bHidrogen = (gas == "hydrogen") or bHidrogen
        if bOxigen and bHidrogen:
            print("Danger mixture!")
            break
    else:
        print("Mixture is not danger!")
      
mixtures = ["hydrogen helium nitrogen","oxygen hydrogen nitrogen","oxygen hydrogen nitrogen"]
for mix in mixtures:
    print("=== " + mix + " ===")
    print_danger_mixture (mix)
