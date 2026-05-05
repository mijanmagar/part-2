

class PotItem:
    def __init__(self, pot_id, plant):
        self.pot_id = pot_id
        self.plant = plant


class PotModel:
    def __init__(self):
        self.__pots = {}

    def AddPot(self, pot_id, plant):
        if pot_id not in self.__pots.keys():
            new_pot = PotItem(pot_id, plant)
            self.__pots[pot_id] = new_pot
        else:
            raise KeyError

    def GetPot(self, pot_id):
        return self.__pots[pot_id]
    
    def GetAllPots(self):
        return self.__pots.values()
    
