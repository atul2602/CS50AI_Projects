from logic import *

chars=['A', 'B', 'C']
roles=['Knight', 'Knave']

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
ASays = Symbol("ASays")
BSays = Symbol("BSays")
CSays = Symbol("CSays")


BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge = And()

#Every character has one role
for char in chars:
        knowledge.add(Or(Symbol(f"{char} is a {'Knight'}"), Symbol(f"{char} is a {'Knave'}")))

#Every person has exactly one role
for char in chars:
    for role1 in roles:
        for role2 in roles:
            if role1!=role2:
                knowledge.add(Implication(Symbol(f"{char} is a {role1}"), Not(Symbol(f"{char} is a {role2}"))))

# Puzzle 0
# A says "I am both a knight and a knave."

ASays=And(AKnave, AKnight)

knowledge0 = And(knowledge)
knowledge0.add(Or(And(ASays, AKnight), And(Not(ASays), AKnave)))
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASays = And(AKnave, BKnave)
knowledge1 = And(knowledge)
knowledge1.add(Or(And(ASays, AKnight), And(Not(ASays), AKnave)))

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
ASays=And(Implication(AKnight, BKnight), Implication(BKnight, AKnight))
BSays=And(Implication(AKnight, BKnave), Implication(BKnave, AKnight))


knowledge2 = And(knowledge)
knowledge2.add(Or(And(ASays, AKnight), And(Not(ASays), AKnave)))
knowledge2.add(Or(And(BSays, BKnight), And(Not(BSays), BKnave)))


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
ASays=Or(AKnight, AKnave)
#BSays=And(Or(And(AKnight, AKnave), And(AKnave, AKnight)))
BSays=And(Implication(ASays, AKnave), Implication(AKnave, ASays))
BSays.add(CKnave)
CSays=AKnight
knowledge3 = And(knowledge)

# for char in chars:
#     knowledge3.add(Or(And(Symbol(f"{char} is a Knight"), Symbol(f"{char}Says")), And(Symbol(f"{char} is a Knave"), Not(Symbol(f"{char}Says"))) ))
knowledge3.add(Or(And(ASays, AKnight), And(Not(ASays), AKnave)))
knowledge3.add(Or(And(BSays, BKnight), And(Not(BSays), BKnave)))
knowledge3.add(Or(And(CSays, CKnight), And(Not(CSays), CKnave)))


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
