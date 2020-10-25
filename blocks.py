name=input("please enter your name ")
age=int(input("what is your age MR. {}".format(name)))
print (age)

if (age < 18):
    print("you are not eligible to vote\n"
    "come back after {} years".format(18-age))
elif (age==900):
    print("not [possible]")
else:
    print("you are elligible to vote")
