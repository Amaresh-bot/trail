print("WELCOME TO THE FLAMES GAME GUYS")
name1 = input("enter your name")
name2 = input("enter your crush name")

name1 = name1.lower()
name2 = name2.lower()

combine_name = name1 + name2

common_name = set(name1) & set(name2)

unique_letters=[]
for letter in combine_name:
    if letter not in common_name:
        unique_letters.append(letter)

count_unique = len(unique_letters)

result_index = count_unique % 6

if result_index == 0:
    relationship = "Friends"
elif result_index == 1:
    relationship = "Lovers"
elif result_index == 2:
    relationship = "Affectionate"
elif result_index == 3:
    relationship = "Marriage"
elif result_index == 4:
    relationship = "Enemies"
elif result_index == 5:
    relationship = "Siblings"
else:
    relationship = "Unknown" 

print("Relationship", relationship)
