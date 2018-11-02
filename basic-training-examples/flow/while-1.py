#Python-3 "wile" example

print("\n*** Test your patience ***\n")

level = 0
answer = 'Y'

while answer.upper() != 'N':
    print(f"Your patience level = {level}.  Continue?[n - no]",end = "")
    level += 1
    answer = input()

