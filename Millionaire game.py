questions = [
    ["1. What is the capital of India?", "Mumbai", "New Delhi", "Chennai", "Kolkata",2],
    ["2. Which planet is known as the Red Planet?","Earth","Jupiter"," Mars","Venus",3],
    ["3. Who is known as the Father of Computers?"," Alan Turing ","Charles Babbage"," Bill Gates","Steve Jobs",2],
    ["4. Which data type is used to store decimal numbers in Python?"," int", "str","float"," bool",3],
    ["5. Which gas is most abundant in Earth’s atmosphere?","Oxygen", "Carbon Dioxide", "Nitrogen","Hydrogen",3],
    ["6. What does CPU stand for?", "Central Processing Unit", "Computer Power Unit","Control Processing Unit","Central Program Utility",1], 
    ]  
prize_money = [1000,5000,10000,14000,19500,25000]
winnings = 0
i = 0

for question in questions:

    
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    a = int(input("Enter your Answer\n 1 for a\n 2 for b \n 3 for c\n 4 for d"))
    if(question[5] == a):
        print("Correct Answer")
        print(f"you won{prize_money[i]}")
        i+=1
        
    else:
        print("Incoreect Answer. The Answer is :",question[5]) 
        print("Better luck next time!")
        
        if i == 0:
            print("Oh.. NO..! YOU LOOSE")
        else:
        
            print(f"CONGRATULATIONS..! YOU WON  {prize_money[i-1]} RUPEES TILL NOW..")
        
        
        break
    



