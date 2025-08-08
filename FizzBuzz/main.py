
# first_word = "Fizz"
# second_word = "Buzz"

# def func_num(start_number, end_number):
#     for i in range(start_number, end_number):
#         if(i % 3 == 0 and i % 5 == 0 ):
#             print(first_word + second_word)
#         elif(i % 3 == 0):
#             print(first_word)
#         elif(i % 5 == 0):
#             print(second_word)
#         else:
#             print(i)
        
# func_num(1,100)


def fizzbuzz(start_number, end_number, num1=3, word1="Fizz", num2=5, word2="Buzz"):
    for i in range(start_number, end_number + 1):
        output = ""
        if i % num1 == 0:
            output += word1
        if i % num2 == 0:
            output += word2
        print(output or i)

# Default Usage
fizzbuzz(1, 100)
