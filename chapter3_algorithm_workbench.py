# Question 1
x = 120

if x > 100:
    y = 20
    z = 40
    print("Question 1")
    print("y =", y)
    print("z =", z)
    # Question 2
a = 5

if a < 10:
    b = 0
    c = 1
    print("Question 2")
    print("b =", b)
    print("c =", c)
    # Question 3
a = 15

if a < 10:
    b = 0
else:
    b = 99

print("Question 3")
print("b =", b)
# Question 4
score = 85
A_score = 90
B_score = 80
C_score = 70
D_score = 60

if score >= A_score:
    print("Your grade is A.")
else:
    if score >= B_score:
        print("Your grade is B.")
    else:
        if score >= C_score:
            print("Your grade is C.")
        else:
            if score >= D_score:
                print("Your grade is D.")
            else:
                print("Your grade is F.")
                # Question 5
amount1 = 50
amount2 = 30

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print("Greater amount:", amount1)
        else:
            print("Greater amount:", amount2)
            # Question 6
speed = 45

if speed >= 24 and speed <= 56:
    print("Speed is normal")
else:
    print("Speed is abnormal")