name1 = input("Name 1: ").lower()
name2 = input("Name 2: ").lower()

matching_string = "true"
count1 = 0
for letter in matching_string:
    count1 += name1.count(letter)
    count1 += name2.count(letter)


matching_string = "love"
count2 = 0
for letter in matching_string:
    count2 += name1.count(letter)
    count2 += name2.count(letter)


score = int(str(count1) + str(count2))
print("The Love Calculator is calculating your score...")
print()

if 10 > score > 90:
    print(f"Your score is *{score}*, you go together like coke and mentos.")

elif 40 < score < 50:
    print(f"Your score is *{score}*, you are alright together.")

else:
    print(f"Your score is *{score}*")

