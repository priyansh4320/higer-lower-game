#CREATED MAINpy FILE
#import files


from logo import logo,vs
import random
import os
from g_data import data
import time
from g_data import data
#print logo

print("WELCOME\n",logo)
time.sleep(3)
incorrect = "you are incorrect\nscore: "
correct = "you are correct\nscore:"
result = ''

def show(result):
    score=0
    second_acc = random.choice(data)
    while result != incorrect:
        
        
        first_acc = second_acc
        second_acc = random.choice(data)
        
        

        print('A: ', first_acc['name'], ', country: ', first_acc['country'], ', Description: ',
              first_acc['description'])
        print(vs)
        print('B:', second_acc['name'], ', country: ', second_acc['country'], ', Description: ',
              second_acc['description'])
        answer = input("Who has more Follower??? A or B:::   ")

        os.system('cls')
        print("\n",logo)
        if answer == 'A' or answer == 'a':
            if first_acc['follower_count'] > second_acc['follower_count']:
                score+=1
                result=correct
                print(result,score)

                continue
            else:
                result=incorrect
                print(result,score)
        elif answer=='B' or answer=='b':
            if first_acc['follower_count'] < second_acc['follower_count']:
                score += 1
                result=correct
                print(result,score)

                continue
            else:
                result=incorrect
                print(result,score)
        else:
            print("invalid input")
            answer=input("Who has more Follower??? A or B:::   ")
        print(f"game over \n score= (score)")

show(result)
