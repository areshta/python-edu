# Python-3 set example
# For example, we registrate some colored objects
# and whant to know how many colors was.

# was registrated:
colors = ["red","blue","red", "cyan", "black", "blue", "red", 
          "red", "orange", "black", "cyan", "red", "pink",
          "orange", "black", "cyan", "red", "pink", "blue",
          "red", "green", "blue", "red", "green", "blue", 
          "blue","red", "cyan", "black", "blue", "green"]

unique_colors = set(colors)
print("Colors: ", unique_colors)
print("Colors count = ", len(unique_colors))
