############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#   #function is suppoed to print 20 only when i = 20, but range() won't ever go to 20

# # # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
#   #randint() was occasionally returning 6, which is out of range of dice_imgs

# Play Computer
# year = int(input("What's your year of birth?: "))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
  #code block did not account for someone that was born in 1994. Added <= to line 20

# # Fix the Errors
# age = int(input("How old are you?"))
# if age >= 18:
#   print(f"You can drive at age {age}.")
#   #needed indentation at line 29, >= on line 28, convert str to int on line 27

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
  #== is used in if loops and check if one side equals another. Use = for assignment.

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
  #needed to indent line 46