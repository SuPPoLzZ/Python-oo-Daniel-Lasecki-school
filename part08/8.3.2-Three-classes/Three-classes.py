class Checklist:
    def __init__(self, attribute_header: str, attribute_entries: list):
        self.attribute_header = attribute_header
        self.attribute_entries = attribute_entries

class Custormer:
    def __init__(self, attribute_id: str, attribute_balance: str, attribute_discount: int):
        self.attribute_id = attribute_id
        self.attribute_balance = attribute_balance
        self.atrribute_discount = attribute_discount
        
        
class Cable:
    def __init__(self, attribute_model: str, attribute_length: str, attribute_max_speed: float, attribute_bidirectional: bool):
        self.attribute_model = attribute_model
        self.attribute_length = attribute_length
        self.attribute_max_speed = attribute_max_speed
        self.attribute_bidirectional = attribute_bidirectional
