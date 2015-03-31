import horntell

class App:

    def init(self, key = None, secret = None):
        horntell.key = key
        horntell.secret = secret

    def set_base(self, base = None):
        horntell.base = base

    def get_base(self):
        return horntell.base

    def get_key(self):
        return horntell.key

    def get_secret(self):
        return horntell.secret

    def set_version(self, version = None):
        horntell.version = version

    def get_version(self):
        return horntell.version
