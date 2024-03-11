class City:
    postcodes = {
        "Helsinki": "00100",
        "Turku": "20100",
        "Tampere": "33100",
        "Rovaniemi": "96100",
        "Oulu": "90100"
    }

    def __init__(self, name):
        self.name = name

helsinki = City("Helsinki")
print(f"{helsinki.name}'s postcode: {City.postcodes[helsinki.name]}")
