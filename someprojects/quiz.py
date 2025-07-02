print("Welcome to my Quiz game")
score = 0

playing= input("Do you want to play ? (yes/no): ").lower()
if playing != "yes":
    quit()

print("Okay! Let's play :)")
    
answer = input("What does CPU stand for ? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")
    
    
answer = input("What does RAM stand for ? ").lower()
if answer == "random access memory":                
    print("Correct!")  
    score += 1     
else:
    print("Incorrect! The correct answer is 'Random Access Memory'.")
    
answer = input("What device is used to type in a computer ? ").lower()      
if answer == "keyboard":
    print("Correct!")   
    score += 1
else:
    print("Incorrect! The correct answer is 'Keyboard'.")
answer = input("What does Wi-Fi stand for ? ").lower()
if answer == "wireless fidelity":
    print("Correct!")

else:
    print("Incorrect! The correct answer is 'Wireless Fidelity'.")
    
answer = input("What does HTML stand for ? ").lower()
if answer == "hypertext markup language":
    print("Correct!")     
    score += 1          
else:
    print("Incorrect! The correct answer is 'Hypertext Markup Language'.")
print("You have completed the quiz!")
print("Thanks for playing :)")

print("Your score is: ", score , "out of 5")
