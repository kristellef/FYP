import pickle

objects = []
with (open("100.pickle", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

pickle_in = open("100.pickle", "rb")
example_dict = pickle.load(pickle_in)
print(example_dict)

