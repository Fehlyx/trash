print("Hello! This is the date age check program. You can either find out, what your appropriate age range is")
print("to date or how long you have to wait to date some one with a nonappropriate age gap.")
print("If you want to know how long to wait, please type 'A'.")
print("If you want to know, what your appropriate age spectrum is, please type 'B'. ")
choice = input()
if choice == "A":
    print("So you want to know how long to wait or just go on with your life until your potential partner is in your age spectrum.")
    print("please tell us first your age as an integer...")
    your_age1 = int(input())
    print ("and now the age of your partner as an integer...")
    your_partner1 = int(input())
    upper_age = (your_age1 - 7) * 2
    lower_age = (your_age1 / 2) + 7
    if (your_partner1 <= upper_age) and (your_partner1 >= lower_age):
        print("You're already in their age spectrum! Get them (consensually!), tiger!")

    elif your_partner1 > your_age1:
        def Youyounger(your_age1, your_partner1):
            your_age2 = your_age1
            your_partner2 = your_partner1
            upper_border = (your_partner2 / 2) + 7
            while your_age2 < upper_border:
                your_partner2 = your_partner2 + 1
                your_age2 = your_age2 + 1
                upper_border = (your_partner2 / 2) + 7
            wait = your_age2 - your_age1
            return wait
        print("In", Youyounger(your_age1,your_partner1), "years, pursuing your relationship is socially acceptable.")

    elif your_age1 > your_partner1:
        def Themyounger(your_age1, your_partner1):
            your_age2 = your_age1
            your_partner2 = your_partner1
            upper_border = (your_age2 / 2) + 7
            while your_partner2 < upper_border:
                your_partner2 = your_partner2 + 1
                your_age2 = your_age2 + 1
                upper_border = (your_age2 / 2) + 7
            wait = your_partner2 - your_partner1
            return wait
        print("In", Themyounger(your_age1,your_partner1), "years, pursuing your relationship is socially acceptable.")
    else:
        print("You're either the same age or something went wrong- Oopsie-toodles!")


elif choice == "B":
    #This is a programm to determine, what age to date is appropriate without needing to use your calculating skills. It uses the your age divided by 2 plus 7 rule.
    # opening text
    print("So you want to know what your appropriate age spectrum is.")
    print("This is a programm to determine, people of which age spectrum are  appropriate to have a sexual AND/OR romantic relationship with.")
    # telling the user to input his age, seperated from actual input so it is in a new line in the terminal
    print("Please tell us your age as an integer:")
    #input the age of a user and making it an integer for math
    your_age = int(input())
    #adverse against people under 15 to use it because it wont work
    if your_age < 15:
        print("Please don't use this program to determine what age spectrum your romantic partner should be. You're too young for it to work. Also, trust me - a computer - hun: Please don't date.")
    else: #ruled out young teens, now making the math stuff
        #upper age border in a function
        def Oldest1(your_age):
            return (your_age - 7) * 2
            #lower age border function
        def Youngest1(your_age):
            return (your_age / 2) + 7
        #making it a float to be the same class with the lower border
        Oldest = float(Oldest1(your_age))
        #HELL IS EMPTY ALL THE DEVILS ARE HERE
        Youngest = Youngest1(your_age)
        #printing this bullshit for the user
        print("The oldest person whose age is appropriate for you to date is", Oldest, "years old and the youngest is", Youngest, "years old." )
