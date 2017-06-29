import random
print("Rumber v.0.2.1")
print("Rumber gives you a random number from the range that you choose. It's under development.")
print("Main developer: Lupyso (Twitter: @Lupyso_)")
def calc(x,y):
    rumberthem = random.randrange(x,y)
    print(rumberthem)
def answer():
    print("is your random number")
x=int(input("Insert the first number: "))
y=int(input("Insert the second number: "))

calc(x,y)
answer()
again=input("Press a to start again or press enter to close: ")
while again is 'a':
    x=int(input("Insert the first number: "))
    y=int(input("Insert the second number: "))
    calc(x,y)
    answer()
    again=input("Press a to start again or press enter to close: ")
    
    
    
    
        
