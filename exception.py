class Specialcharacter(Exception):
    def __init__(self,arg):
        self.msg = arg

class Lengtherror(Exception):
    def __init__(self,arg):
        self.msg = arg