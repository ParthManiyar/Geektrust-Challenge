class Train:
    station_dists = {'NGP': 400,
                     'ITJ': 700,
                     'BPL': 800,
                     'AGA': 1300,
                     'NDL': 1500,
                     'PTA': 1800,
                     'NJP': 2200,
                     'GHY': 2700,
                     'ENGINE': 2800}

    def __init__(self, name, bogies):
        self.name = name
        self.bogies = bogies
        if name == 'B':
            self.station_before_hyderabad = {'TVC', 'SRR', 'MAQ', 'MAO', 'PNE'}
        else:
            self.station_before_hyderabad = {'CHN', 'SLM', 'BLR', 'KRN'}
        self.bogies_arrived = []

    def bogies_arrived_hyderabad(self):
        for bogie in self.bogies:
            if bogie not in self.station_before_hyderabad:
                self.bogies_arrived.append(bogie)

        train_bogies = "ARRIVAL " + ' '.join(self.bogies_arrived)

        return train_bogies

    def merge_trains(self, bogies_arrived_b):
        bogiesab = []

        for bogie in self.bogies_arrived:
            if bogie in self.station_dists:
                bogiesab.append((self.station_dists[bogie], bogie))

        for bogie in bogies_arrived_b:
            if bogie in self.station_dists:
                bogiesab.append((self.station_dists[bogie], bogie))

        bogiesab.sort()
        bogiesab.reverse()
        trainab = "DEPARTURE TRAIN_AB"
        for bogie in bogiesab:
            trainab += " " + bogie[1]

        return trainab
