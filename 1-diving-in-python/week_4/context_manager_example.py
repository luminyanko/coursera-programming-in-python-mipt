class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


with open_file('context_manager_example.txt', 'w') as f:
    f.write('Inside `open_file` context manager')
