from learning_examples.Person import Person


def test_persons():
    print("")
    p = Person("Karolos", 35, "NYC")
    p2 = Person("Alexandros", 33, "Katakolo")
    p3 = Person("Elena", 30, "Katakolo")
    for p_ in [p,p2,p3]:
        print(p_.describe())