import random


class GrammaticalQuantity:
    
    # Constructor to initialize
    def __init__(self):
        self.determiners = ["A", "One", "The", "Some", "Many"]
        self.singular_nouns = ["cat", "man", "woman", "dog", "bird"]
        self.plural_nouns = ["birds", "boys", "cars", "cats", "children",
                             "dogs", "girls", "men", "rabbits", "women"]
        self.past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                           "ran", "slept", "talked", "walked", "wrote"]
        self.present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                              "runs", "sleeps", "talks", "walks", "writes"]
        self.future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                             "will think", "will run", "will sleep", "will talk",
                             "will walk", "will write"]

    # sample method 1
    def get_determiner(self):
        """Return a randomly chosen determiner. A determiner is
        a word like "the", "a", "one", "some", "many".
        If quantity is 1, this function will return either "a",
        "one", or "the". Otherwise this function will return
        either "some", "many", or "the".

        Parameter
            quantity: an integer.
                If quantity is 1, this function will return a
                determiner for a single noun. Otherwise this
                function will return a determiner for a plural
                noun.
        Return: a randomly chosen determiner.
        """
        return random.choice(self.determiners)

    # sample method 1
    def get_noun(self, quantity):
        """Return a randomly chosen noun.
        If quantity is 1, this function will
        return one of these ten single nouns:
            "bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"
        Otherwise, this function will return one of
        these ten plural nouns:
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"

        Parameter
            quantity: an integer that determines if
                the returned noun is single or plural.
        Return: a randomly chosen noun.
        """
        if quantity == 1:
            return random.choice(self.singular_nouns)
        else:
            return random.choice(self.plural_nouns)

    # sample method 1
    def get_verb(self, quantity, tense):
        """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"

        Parameters
            quantity: an integer that determines if the
                returned verb is single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.
        """
        if tense == "past":
            return random.choice(self.past_verbs)
        elif tense == "present":
            if quantity == 1:
                return random.choice(self.present_verbs)
            else:
                return random.choice(self.present_verbs).rstrip("s")
        elif tense == "future":
            return random.choice(self.future_verbs)
            
    # sample method 1
    def make_sentence(self, quantity=None, tense=None, verb=None):
        """Build and return a sentence with three words:
        a determiner, a noun, and a verb. The grammatical
        quantity of the determiner and noun will match the
        number in the quantity parameter. The grammatical
        quantity and tense of the verb will match the number
        and tense in the quantity and tense parameters.
        """
        determiner = self.get_determiner()
        if quantity is None:
            quantity = 1 if determiner in ["A", "One", "The"] else random.randint(2, 5)
        noun = self.get_noun(quantity)
        if tense is None:
            tense = random.choice(["past", "present", "future"])
        if verb is None:
            verb = self.get_verb(quantity, tense)

        determiner = determiner.capitalize()
        noun = noun.capitalize()
        return f"{determiner} {quantity} {noun} {verb}."
        
# Main method
def main():
    generator = GrammaticalQuantity()

    for _ in range(5):
        sentence = generator.make_sentence()
        print(sentence)


if __name__ == "__main__":
    main()