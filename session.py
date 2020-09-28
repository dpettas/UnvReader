
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Unv Session Class
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


class UnvSession():

    def __init__(self, lines: str):
        self.lines = lines

    def gid(self): return int(self.lines[0])

