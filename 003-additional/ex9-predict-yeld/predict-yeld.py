def my_generator(max):
    curr = 0
    predict = False
    while curr < max:
        if curr + 1 < max:
            predict = True
        else:
            predict = False
        yield curr, predict
        curr += 1

for i, predict in my_generator(10):
    print("Iteration = ", i, "The next is available = ", predict)
