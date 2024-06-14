import enchant
def spell_check(word):
    # Create an English dictionary instance
    d = enchant.Dict("en_US")

    # Check if the word is in the dictionary
    if d.check(word):
        print(f"{word} is spelled correctly.")
    else:
        suggestions = d.suggest(word)
        if suggestions:
            print(f"{word} is spelled incorrectly. Suggestions: {', '.join(suggestions)}")
        else:
            print(f"No suggestions for {word}.")

# Example usage
word_to_check = "helo"
spell_check(word_to_check)
