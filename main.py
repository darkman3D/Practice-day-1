class Vulnerability:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __str__(self):
        return f"Vulnerability: {self.name}, Rank: {self.rank}"

    def __eq__(self, other):
        if isinstance(other, Vulnerability):
            return self.name == other.name and self.rank == other.rank
        return False

    def __lt__(self, other):
        if isinstance(other, Vulnerability):
            return self.rank < other.rank
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vulnerability):
            return self.rank > other.rank
        return NotImplemented

    def increase_rank(self, amount=1):
        self.rank += amount

    def decrease_rank(self, amount=1):
        self.rank -= amount
        if self.rank < 0:
            self.rank = 0