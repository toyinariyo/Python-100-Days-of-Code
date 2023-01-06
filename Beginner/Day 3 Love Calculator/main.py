print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1 + name2
lowercase = combined_names.lower()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
true = t + r + u + e
l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
print(love_score)
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")
