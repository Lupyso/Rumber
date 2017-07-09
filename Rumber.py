import random
print("Rumber v.0.3.2")
print("Rumber gives you a random number from the range that you choose. It's under development.")
print("Main developer: Luis Morniroli")
def xagain():
    x=int(input("Insert the first number: "))
    y=int(input("Insert the second number: "))
    calc(x,y)
    answer()
    again=input("Press x to start again, y to create a new number with the same values, enter to close: ")
    if again is 'x':
     xagain()
    elif again is 'y':
     yagain()
def yagain():
    rumberthem = random.randrange(x,y)
    print(rumberthem)
    again=input("Press x to start again, y to create a new number with the same values, enter to close: ")
    if again is 'x':
     xagain()
    elif again is 'y':
     yagain()	
    
   
def change():
    if again is 'x':
     xagain()
    elif again is 'y':
     yagain()
    
def calc(x,y):
    rumberthem = random.randrange(x,y)
    print(rumberthem)
def answer():
    print("is your random number")
x=int(input("Insert the first number: "))
y=int(input("Insert the second number: "))

calc(x,y)
answer()
again=input("Press x to start again, y to create a new number with the same values, enter to close: ")
while again is 'x':
    x=int(input("Insert the first number: "))
    y=int(input("Insert the second number: "))
    calc(x,y)
    answer()
    again=input("Press x to start again, y to create a new number with the same values, enter to close: ")
    if again is 'x':
     xagain()
    elif again is 'y':
     yagain()	
while again is 'y':
    rumberthem = random.randrange(x,y)
    print(rumberthem)
    again=input("Press x to start again, y to create a new number with the same values, enter to close: ")
    if again is 'x':
     xagain()
    elif again is 'y':
     yagain()	
    
    	
	
	
	

	
    
    
    
        
