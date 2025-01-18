path_to_file = "books/frankenstein.txt"

def count_words(text):
    return (len(text.split()))

def count_characters(text):
    lowered_text = text.lower()
    character_counts = {}

    for c in lowered_text:
        if c in character_counts:
            character_counts[c] += 1
        else:
            character_counts[c] = 1
    
    return character_counts

def generate_report(book, text):
    word_count = count_words(text)
    character_count = count_characters(text)
    parsed_characters = []
    
    print(f"--- Begin report of book for {book} ---")
    print(f"{word_count} words found in the document.\n")
    
    for key, value in character_count.items():
        parsed_characters.append({'character': key, 'count': value})
    parsed_characters.sort(reverse=True, key=lambda x: x['count'])

    for pc in parsed_characters:
        character, count = pc.values()
        if (character.isalpha()):
            print(f"The '{character}' character was found {count} times.")

    print("--- End report ---")

with open(path_to_file) as f:
    file_contents = f.read()

generate_report("Frankenstein", file_contents)