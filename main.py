import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {code.letter:code.code for (letter, code) in df.iterrows()}
def fun():
    try:
        ui = input("Type your word").upper()
        new = [nato[i] for i in ui]
        print(new)
    except KeyError:
        print("Sorry only letters")
        fun()


fun()

