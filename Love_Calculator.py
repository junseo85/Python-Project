
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
true = "true"
love = "love"
count_true = 0
count_love = 0
for a in true:
    if lower_case_name1.count(str(a)) > 0:
        count_true += lower_case_name1.count(str(a))
    if lower_case_name2.count(str(a)) > 0:
        count_true += lower_case_name2.count(str(a))
for b in love:
    if lower_case_name1.count(str(b)) > 0:
        count_love += lower_case_name1.count(str(b))
    if lower_case_name2.count(str(b)) > 0:
        count_love += lower_case_name2.count(str(b))
score = str(count_true) + str(count_love)
score = int(score)
if score < 10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")