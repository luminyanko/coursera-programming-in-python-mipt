class IndexIterable:
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]


for letter in IndexIterable('this is a string'):
    print(letter)
