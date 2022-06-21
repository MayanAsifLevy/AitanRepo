
from DAL.Rec_DAL.growers_dal import GrowersDAL

class Growers:
    def __init__(self):
        self.growers_dal=GrowersDAL()
    
    def get_growers(self):
        growers_list=self.growers_dal.get_all_growers()
        return growers_list