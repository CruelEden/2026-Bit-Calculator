def calc_text_bits():
    pass

    # get text
    response = input("Enter some text: ")

    #calculate bits
    num_chars = len(response)
    num_bits = num_chars * 8

    #set up answer
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer

# main routine here
text_ans = calc_text_bits()
print(text_ans)