# Question #3
# If this code were run, what would the output to the console?

class Cat:
    def __init__(self, name: str, breed: str, weight: float):
        self.name = name
        self.breed = breed
        self.weight = weight


if __name__ == "__main__":
    cat = Cat("Sparky", "British Shorthair", 6.33)

    print(cat.weight)
