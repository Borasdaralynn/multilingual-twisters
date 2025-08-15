import epitran

# English Latin script
epi = epitran.Epitran('eng-Latn')

twisters = [
    "She sells seashells by the seashore.",
    "Peter Piper picked a peck of pickled peppers.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
]

for t in twisters:
    print(f"Original: {t}")
    print(f"IPA: {epi.transliterate(t)}\n")

