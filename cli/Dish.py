'''

Assumptions for class Dish :
    1) Each Dish will be having a valid name
'''


class Dish:
    __slots__ = "name", "id","indegrents"
    def __init__(self,name, id,indegrents):
        """
        constructor
        :param name: string
        :param id: int
        """
        self.id = id
        self.name = name
        self.indegrents = indegrents
