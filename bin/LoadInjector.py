class LoadInjector:

    short_arguments = {"arguments": "a", "properties": "p"}
    long_arguments = {"arguments": "args", "properties": "props"}

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def run_test(self, args):
        pass

    def get_version(self):
        pass

    def validate_arguments(self, opts):
        pass