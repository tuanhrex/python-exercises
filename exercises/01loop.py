# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there



# Option 1: With prompts for statements and number of times
def p_times1():
    statement = input('What is your statement?\n')
    num = input('How many times would you like to make that statement?\n')


    for line in range(int(num)):
        p_times = statement
        print(p_times)
        
p_times1()

# Option 2: Method with two inputs
# def p_times2(input1, input2):
#     for line in range((input2)):
#         print(input1)

# p_times2('yo', 7)