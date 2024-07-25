from random import shuffle
qms=[
    ("What is name of your country","india"),
    ("What is the capital of your country","new delhi"),
     ("What is the name of national flower","lotus"),
     ("What is the name of national animal","tiger"),
    ("What is the name of national bird","peacock"),
    ("What is the name of national flag","tiranga")
]
shuffle(qms)
right = 0
wrong = 0
for questions,right_ans in qms:
    ams = input(questions+" ")
    if ams.lower() == right_ans:
        right += 1
    else:
        print("No,the right answer is:",right_ans)
        wrong += 1
print("Congratulation!")
print("You got ",right,"right answers and",wrong,"wrong answers")