import random

def random_name():
    def vowel():
        return random.choice(['a', 'e', 'i', 'o', 'u'])
    def consonant():
        return random.choice((['b', 'c', 'd', 'm', 'n', 'r', 's', 't'] * 4) +
            ['f', 'g', 'h', 'j', 'l', 'p', 'q', 'r', 'v', 'w', 'x', 'y', 'z'])
    return (random.choice([vowel(), '']) +
            ''.join([consonant()+vowel() for i in range(1, random.randint(2,4))])
            + random.choice([consonant(), ''])).capitalize()
