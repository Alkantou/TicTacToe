from learning_examples.Person import Person


def test_persons():
    p = Person("Karolos", 35, "NYC")
    print(p.describe())