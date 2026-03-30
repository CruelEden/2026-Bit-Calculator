# Ask user for width and loop they
# enter a number that is more than zero
def int_check(question, low):

    error = f"please enter number that is more then or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def integer_calc():
    pass
    #ask for integer
    integer = int_check("Integer: ", 0)

    # convert to bin
    raw_binary = bin(integer)

    #remove 0b
    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

#main routine
integer_ans = integer_calc()
print(integer_ans)