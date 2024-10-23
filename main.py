import random
import time 
words = ["dogs", "apple", "cherry", "grape", "cats", "fish", "know", "happy", "sad", "monkey", "blue", "soccer"]

def typing_trainer():
    rounds = 10
    right_resp = 0
    total_time = 0  
    
    print("Type the words you see!")
    

    for i in range(rounds):
        word = random.choice(words)
        print(f"Round {i+1}: Type '{word}'")
        
     
        start = time.time() 
        user_input = input("Your response: ").lower()
        end = time.time()    
        
      
        response = end - start
        total_time += response  
        
        if user_input == word:
            right_resp += 1
        else:
            print("That is not correct, you lose a point")
            right_resp -= 1

    print("Your score is: " + str(right_resp))
    print(f"Your total time was: {total_time:.2f} seconds")

typing_trainer()
