class MyFile:
    def __init__(self, name):
        self._fileObject = open(name, 'r')

    def reset(self):
        self._fileObject.seek(0)

    def read(self, num):
        return self._fileObject.read(num)

    def close(self):
        self._fileObject.close()

    def is_closed(self):
        return self._fileObject.closed

    def get_name(self):
        return self._fileObject.name

    def get_mode(self):
        return self._fileObject.mode