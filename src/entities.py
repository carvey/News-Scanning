from collections import Counter

entities = []

class Entity:
    """
    This class should represent one idea, person, or thing to analyze over a piece of text
    """
    def __init__(self, keys: str, active=True):
        self.name = keys
        self.keys = keys.lower().split()
        self.active = active

        self.count = 0

        if active:
            entities.append(self)

    def __str__(self):
        return self.name

    def add_key(self, key: str):
        self.keys.append(key)

    def matches(self, text: str):
        """
        For a given piece of text, ignore case and determine how many times the entity
        is mentioned over the piece of text
        :param text: a str to be searched through for the entities frequency
        :return:
        """
        word_count = Counter(text.lower().split())

        count = 0
        for key in self.keys:
            if key in word_count:
                count += word_count[key]

        return count


rubio = Entity("Marco Rubio")

sanders = Entity("Bernie Sanders")

trump = Entity("Donald Trump")

clinton = Entity("Hilary Clinton")

cruz = Entity("Ted Cruz")

carson = Entity("Ben Carson")

kasich = Entity("John Kasich")

scalia = Entity("Antonin Scalia")