import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S
NP -> Det N | Det Adj N | Adj N | N | N PP | Det N PP | Det Adj N PP | N Conj N | NP Conj NP
VP -> V | V NP | V NP PP | V PP | Adv V | V Adv | V Conj V | VP Conj VP
PP -> P NP
AdjP -> Adj | Adj Conj Adj
AdvP -> Adv | Adv Conj Adv
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)

def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = sentence.lower() # Convert all characters to lowercase
    tokens = nltk.tokenize.word_tokenize(sentence) # split sentence into list of words
    # Remove any words not containing at least one alphabetic character (e.g '.' or '28')
    filtered = [token for token in tokens if token.isalpha()]
    return filtered


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Check, recursively, there are no smaller NP chunks within
    def recursive_check(subtree):
        for descendant in subtree.subtrees(lambda t: t != subtree): # Check second layer for NPs
            if descendant.label() == 'NP':
                return False # If subtree's subtrees contain NP, return False
        return True

    npChunks = [] # Initialise list of np chunks

    for subtree in tree.subtrees(lambda t: t.label()=="NP"): # Check for subtrees with NP label
        if all(child.label() != 'NP' for child in subtree): # Check there's no smaller NP
            if recursive_check(subtree): # Check subtree's subtrees
                npChunks.append(subtree) # Add subtree to list

    return npChunks

if __name__ == "__main__":
    main()
