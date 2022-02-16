# Ask if user has played before
show_instructions = input ("Have you played this game before? ").lower()
# If they yes, output 'program continues'
if show_instructions =="yes": 
    print ("program continues")

elif show_instructions == "no":
    print("display instructions")

# If they say no, out 'display instructions'
else:
     print ("Please answer yes/no")

     print ("You chose {}" .format(show_instructions))