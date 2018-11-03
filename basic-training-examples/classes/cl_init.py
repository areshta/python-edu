#Python - 3 Class init example

class Color:
    def __init__(self, r, g, b):
        self._verify(r, g, b)
        self._r, self._g, self._b = r, g, b

    def _verify(self, *args):
        for ar in args:
            if ar < 0 or ar > 255:
                raise ValueError('Bad color value: '+str(ar))

    def get_hex(self):
        return "0x"+format(self._r,'02x')+format(self._g,'02x')+format(self._b,'02x')

print("\n*** Class init example ***\n")

inp = input("Enter color's R G B: ")
r,g,b = inp.split(" ")
r,g,b = int(r), int(g), int(b)
print(f"You entered color (RGB): {r} {g} {b}")

try:
    cl = Color(r,g,b)
except ValueError as e:
    print(str(e)) 
else:
    print("Hex color value: " + cl.get_hex())

