class NumberSet100:
    def __init__(self):
        self.full_set = list(range(1, 101))
        self.current_set = self.full_set.copy()

    def extract(self, number: int):
        if not isinstance(number, int):
            raise ValueError("El número debe ser un entero.")
        if number < 1 or number > 100:
            raise ValueError("El número debe estar entre 1 y 100.")
        if number not in self.current_set:
            raise ValueError(f"El número {number} ya fue extraído o no existe.")
        self.current_set.remove(number)

    def find_missing_number(self):
        expected_sum = sum(self.full_set)
        current_sum = sum(self.current_set)
        return expected_sum - current_sum