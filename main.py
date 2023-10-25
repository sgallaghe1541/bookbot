
def get_contents(filename):
    return filename.read()
    

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def counts_of_characters(file_contents):
    file_contents = file_contents.lower()

    character_counts = {}

    for char in file_contents:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def character_count_report(filename):

    with open(filename) as f:
        contents = f.read()

        words = count_words(contents)

        character_counts = counts_of_characters(contents)

        characters = []
        for char in character_counts.keys():
            if char.isalpha():
                characters.append(char)

        characters.sort()

        print(f"--- Begin report of {filename} ---")
        print(f"{words} words found in the document")

        for char in characters:
            print(f"the '{char}' character was found {character_counts[char]}")

        print("--- End of Report ---")


def main():
    filename = "books/frankenstein.txt"
    character_count_report(filename)

main()