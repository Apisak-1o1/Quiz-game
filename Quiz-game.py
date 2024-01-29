print("Welcome to EZ math quiz! \n in this game you have to answer as fast as possible")
play=input("\nWant to start now? ")

if play.lower() != "yes":
    quit()

score=0

print("Question 1")
answer=input("what is 25*25 ? ")
if answer =="625":
    score +=1
print("Question 2")
answer=input("what is 123+123 ? ")
if answer =="246":
    score +=1
print("Question 3")
answer=input("what is 321+321 ? ")
if answer =="642":
    score +=1
print("Question 4")
answer=input("what is 999+99+1001 ? ")
if answer =="2099":
    score +=1
print("Question 5")
answer=input("what is 5*5 ? ")
if answer =="25":
    score +=1

print("Your score is "+str(score)+"/5!")
print(str((score/4)*100)+"%.")