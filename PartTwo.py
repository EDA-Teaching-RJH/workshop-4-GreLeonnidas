p = 75
x = 0

allowed_x = [5, 10, 20, 50]

while p > 0:

    x = int(input("Insert coin"))
    
    p = p - x 
    if x > p and p < 0:
       print("Your change is ",p * (-1))
    
    

     




