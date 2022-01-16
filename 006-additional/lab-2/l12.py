# Write a python program to find the longest words in a file

txt = """Муха, Муха-Цокотуха, Позолоченное брюхо! Муха по полю пошла, Муха денежку нашла. 
Пошла Муха на базар И купила самовар: Приходите, тараканы, Я вас чаем угощу! 
Тараканы прибегали, Все стаканы выпивали, А букашки — По три чашки 
С молоком И крендельком: Нынче Муха-Цокотуха Именинница!"""

# replace punctuation
txt = txt.replace(",","").replace(" — ", " ").replace(":","").replace(".","").replace("!","") \
    .replace("\n","")
txt = txt.lower()
words = txt.split(" ")
dict_words = dict()
for word in words:
    if len(word) not in dict_words:
        dict_words[len(word)] = set([word])
    else:
        dict_words[len(word)].add(word)

dict_words = dict(sorted(dict_words.items()))

for key in dict_words:
    print(key, dict_words[key])