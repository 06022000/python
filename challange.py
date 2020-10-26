
low=0
high=5
p1="learn python"
p2="learn java"
p3="learn c++"
p4="learn cotlin"
p5="learn ruby"
p0="exit"

print("""1.learn python
2.learn java
3.learn c++
4.learn cotlin
5.learn ruby
0=exit""")

print("press enter the no.")
number=""


while number!=0:
    print("enter a number between {} and {}".format(low,high))
    number=int(input())
    if number==1:
        print("1",p1)
    if number==2:
        print("2",p2)
    if number==3:
        print("3",p3)
    if number==4:
        print("4",p4)
    if number==5:
        print("5",p5)
    if number not in range(0,6):
        print("""1.learn python
        2.learn java
        3.learn c++
        4.learn cotlin
        5.learn ruby
        0=exit""")

else:
    if number==0:
        print("you have left the game")

