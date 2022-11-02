class Plate:
    def __init__(self,value,row_col:tuple,parent=None):
        self.value = value
        self.pos = row_col
        self.parent = parent
        self.next = None
