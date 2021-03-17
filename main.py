print("welcome to my first Project in py!!")
name = input("What is your name?")
age = int(input("What is your age?"))

health = 15

if age >= 18:
    print("You are old enough")

    wants_to_play= input("Do you wanna play?").lower()
    if wants_to_play =="yes":
        print("Let's play!")
        
        left_or_right = input("First chouce... Left or Right(left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path a lake... Do swim across or go around?(across/around)? ")
            
            if ans =="around":
                print("You around and reached te other side of the lake.")
            elif ans == "across":
                print("you managed to get across, but were bit by a snake and lost 5 of health.")
                health -= 5
                
            ans = input("You notice a house and a river. Which do you go to(river/house)?")
            if ans == "house":
                print("You go to the house and got shot on the army by the owner...and you lose 5 health.")
                health -= 5
                 
                if health <= 0:
                    print("You now have 0 health You lose...") 
                else:
                    print("You have survived.")
                                
            else:
                print("You fell in the river and die...")        
       
        else:
            print("you fell dow and die")
    else:
        print("Cya...")
else:
    print("You are not old enough to play...")














# string "hello", "89", "hi"
# int 8, 5, 5 , 6
# float 6.4, 8.9
# bool true, false



