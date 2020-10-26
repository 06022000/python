# avilable_parts=["keyboard",
#                  "cpu",
#                  "monitor",
#                  "mouse",
#                  "mouse pad",
#                  "ram stick"
#                ]
# valid_choices=[]
# for i in range (1,len(avilable_parts)+1):
#     valid_choices.append(str(i))
# print(valid_choices)
#
# current_choices="-"
# computer_parts=[]
#
# while current_choices!="0":
#     if current_choices in valid_choices:
#         index = int(current_choices)-1
#         chosen_parts=avilable_parts[index]
#         if chosen_parts in computer_parts:
#             print("remove {}".format(current_choices))
#             computer_parts.remove(chosen_parts)
#         else:
#             print("adding {}".format(current_choices))
#             computer_parts.append(chosen_parts)
#         print("your list now includes the following parts : {}".format(computer_parts))
#     else:
#         print("please enter option from list below")
#         for number,parts in enumerate(avilable_parts):
#             print("{0}: {1}".format(number+1,parts))
#
#     current_choices=input()
#
# print(computer_parts)




# 2nd programmm  that is very very important.()++++++()


# data=[104,101,4,105,308,103,5,
#       107,100,306,106,102,112]
# min_valid=100
# max_valid=200
# for index in range(len(data)-1,-1,-1):
#     if data[index]<min_valid or data[index]>max_valid:
#         del data[index]
#
# print(index,data)



# 2nd way of doing the 2nd programmmm
# data=[104,101,4,105,308,103,5,
#       107,100,306,106,102,112]
# min_valid=100
# max_valid=200
# top_index=len(data)-1 #value is 12 and value of index is 0 from reverse order
# for index,value in enumerate(reversed(data)):
#     if value<min_valid or value>max_valid:
#         print(top_index-index,value)
#         del data[top_index-index]
# print(data)




# 3rd programmm  that is very very important................................()++++++()
# menu = [["egg", "chicken"],
#         ["egg", "chicken", "sausage"],
#         ["egg", "spam"],
#         ["egg", "spam", "chicken"],
#         ["egg", "chicken", "sausage", "spam"],
#         ["spam", "chicken", "sausage", "spam"],
#         ["spam", "egg", "spam", "spam", "chicken", "tomato", "spam"],
#         ["spam", "egg", "spam", "spam", "chicken", "spam"],
# ]
#
# for meal in menu:
#         while "spam" in meal:
#                 meal.remove("spam")
#         print(meal)
#
#


# menu = [["egg", "chicken"],
#         ["egg", "chicken", "sausage"],
#         ["egg", "spam"],
#         ["egg", "spam", "chicken"],
#         ["egg", "chicken", "sausage", "spam"],
#         ["spam", "chicken", "sausage", "spam"],
#         ["spam", "egg", "spam", "spam", "chicken", "tomato", "spam"],
#         ["spam", "egg", "spam", "spam", "chicken", "spam"],
#         ]
#
# for meal in menu:
#     for index in range((len(meal))-1,-1,-1):
#         if meal[index]=="spam":
#             del meal[index]
#     print(meal)
#


# menu = [["egg", "chicken"],
#         ["egg", "chicken", "sausage"],
#         ["egg", "spam"],
#         ["egg", "spam", "chicken"],
#         ["egg", "chicken", "sausage", "spam"],
#         ["spam", "chicken", "sausage", "spam"],
#         ["spam", "egg", "spam", "spam", "chicken", "tomato", "spam"],
#         ["spam", "egg", "spam", "spam", "chicken", "spam"],
#         ]
#
# for meal in menu:
#     for item in meal:
#         if item!="spam":
#             print(item, end=" ")
#     print()
