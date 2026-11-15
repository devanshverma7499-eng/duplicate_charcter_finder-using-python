text = input("Enter a word or sentence: ")

duplicates = []

for char in text.lower():
    if char != " " and text.lower().count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)

if duplicates:
    print("Duplicate Characters:", duplicates)
    print("Total Duplicates:", len(duplicates))
else:
    print("No Duplicate Characters Found!")