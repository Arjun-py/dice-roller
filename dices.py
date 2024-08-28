import random

one = '''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️'''

two = '''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️'''
three = '''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️
⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️'''

foure = '''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️'''

five = '''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️'''
six = '''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️'''


start = input("enter any key to contune start\n")
while True:
    
   
    
    randomch=random.randint(1,6)
    if randomch==1:
        print(one)
            
    elif randomch==2:
        print(two)
        
    elif randomch==3:
        print(three)
        
    elif randomch==4:
        print(foure)
        
    elif randomch==5:
        print(five) 
        
    elif randomch==6:
        print(six)
        
    else:
        print("fuck")
        
    user = input("enter r for contune:\n")
    if user.lower()=="r":
        continue
    else:
        print("worng input")
        break
    
        




