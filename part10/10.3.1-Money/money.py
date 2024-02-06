class Money:
    def __init__(self, euros: int, cents: int):
        # Check if both euros and cents are integers and positive
        if not isinstance(euros, int) or not isinstance(cents, int):
            raise ValueError("Both euros and cents must be integers.")
        if euros < 0 or cents < 0:
            raise ValueError("Both euros and cents must be positive.")
        # Check if cents is between 0 and 99
        if cents > 99:
            raise ValueError("Cents must be between 0 and 99.")
        
        self.euros = euros
        self.cents = cents

    def __str__(self):
        return f"{self.euros}.{self.cents}"
