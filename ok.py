
#die rolling simulator
#pro 1
"""using concepts
    1.rand
    2.loop"""
import random
while 1:
 response=input("do u wannna roll the dice say yes or no")

 if response=="yes":
    print("the dice is rolling to get")

    print(random.randrange(1,7,1))
 else: 
    print("ok thums up!!!")   
    break
