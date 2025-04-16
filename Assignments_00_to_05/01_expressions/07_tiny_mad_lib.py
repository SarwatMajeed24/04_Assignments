# Define the beginning of the sentence as a constant
SENTENCE_START = "The adventurous"

def make_mad_lib():
    """Prompts the user for an adjective, noun, and verb, and then prints a fun sentence."""
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    fun_sentence = f"{SENTENCE_START} {adjective} {noun} decided to {verb} through the enchanted forest."
    print(fun_sentence)

if __name__ == "__main__":
    make_mad_lib()