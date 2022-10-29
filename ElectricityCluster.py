class ElectricityCluster:
    def __init__(self):
        self.collection = []

    def add_electricity(self, elec):
        self.collection.append(elec)

    def get_cluster(self):
        return self.collection
