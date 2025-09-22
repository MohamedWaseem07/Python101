import time

# User age input and if function
usersage = input("How old are you?\n")
usersage = int(usersage)

if usersage > 18:
    print("You are an adult.")
    print("You can vote.")
elif 18>= usersage <=13:
    print("You are a teenager.")
    print("You can't vote.") 
else:
    print("You are a child.")
    print("You can't vote.")
time.sleep(5)
    
   