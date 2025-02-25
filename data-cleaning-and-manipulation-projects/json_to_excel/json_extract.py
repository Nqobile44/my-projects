import json

class ExtractFromJ:
    def __init__(self):
        with open(file="data/sample2.json") as file:
            self.data = json.load(fp=file)
