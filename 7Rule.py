#This is a programm to determine, what age to date is appropriate without needing to use your calculating skills. It uses the your age divided by 2 plus 7 rule.

# opening dialogue
print("This is a programm to determine, which age spectrum is appropriate have a sexual or romantic relationship with.")
print("Please tell us your age as an integer:")
#input the age of a user and making it an integer for math
your_age = input()
#making the math stuff
oldest1 = (int(your_age) - 7) * 2
youngest = (int(your_age) / 2) + 7
#converting the oldest1 into a float because through the math stuff the youngest is already a float and we want it to look pretty
oldest = float(oldest1)
#print the shit
print("The oldest person whose age is appropriate for you to date is", oldest, "years old and the youngest is", youngest, "years old." )
